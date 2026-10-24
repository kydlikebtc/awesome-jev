"""Speculative fan-out: ask more than you need, use what turned out relevant.

The state is read once and all questions are evaluated in parallel against it.
So the marginal cost of one more question is roughly its own tokens, not another
round trip. That inverts the usual instinct to ask the minimum: here you ask
everything that *might* matter in one request, and let code pick.

This example routes a browser action. It asks which operation to perform AND,
speculatively, the target for each operation it might have chosen. Only one
target gets used. The alternative — decide the operation, then make a second
call for its target — doubles the latency of every single step.

Run:
    pip install typesafe-sdk
    export TYPESAFE_API_KEY=...
    python main.py
"""

from __future__ import annotations

from typesafe_sdk import Choice, Noul, TypeSafeClient

GOAL = "Find a one-way flight from Zurich to London next Friday"

# This example uses page text from an accessibility tree or serialised DOM.
# Native Jev also accepts experimental images with an explicit opt-in; this
# text example needs neither image assets nor that header. See:
# https://docs.typesafe.ai/images
ELEMENTS = {
    "e1": "text input, label 'Where from?', value 'Zurich'",
    "e2": "text input, label 'Where to?', value empty",
    "e3": "button, label 'Departure date'",
    "e4": "button, label 'Search'",
    "e5": "link, label 'Sign in'",
}

OPERATIONS = {
    "click": "Press a button or link",
    "type_text": "Type into a text input",
    "done": "The goal is already achieved",
    "blocked": "Cannot proceed from here",
}


def main() -> None:
    client = TypeSafeClient()

    state = {"goal": GOAL, "elements": ELEMENTS, "history": []}

    # One request, four questions. Two of them are speculative: we ask for a
    # click target and a typing target before knowing which operation wins.
    response = client.system_one(
        state=state,
        questions={
            "operation": Choice(
                instructions="Which single operation moves us toward the goal next",
                criteria=OPERATIONS,
            ),
            "click_target": Choice(
                instructions="If clicking, which element should be clicked",
                criteria=ELEMENTS,
            ),
            "type_target": Choice(
                instructions="If typing, which input should receive the text",
                criteria=ELEMENTS,
            ),
            # Cheap insurance: a separate read on whether we are already done,
            # so a wrong `operation` cannot loop forever.
            "already_done": Noul(
                instructions="The goal has already been achieved on this page",
            ),
        },
    )

    operation = response.answers["operation"]
    done = response.answers["already_done"]

    print(f"operation      {operation.choice}  (confidence {operation.confidence:.2f})")
    print(f"already_done   {done.noul:.2f}")

    # Read only the speculative answer the operation made relevant. The other
    # one was still paid for, and was still cheaper than a second round trip.
    if operation.choice == "click":
        target = response.answers["click_target"]
        print(f"-> click {target.choice}: {ELEMENTS[target.choice]}")
    elif operation.choice == "type_text":
        target = response.answers["type_target"]
        print(f"-> type into {target.choice}: {ELEMENTS[target.choice]}")
        # The model does not generate text. Whatever gets typed comes from your
        # own code, or from a small generative model called only for this step.
        print("   (the text itself must come from code or a generative model)")
    else:
        print(f"-> {operation.choice}, no target needed")

    # Fan-out's default budget is 64k tokens per request, and 32k for the state plus
    # the single longest question. Speculative questions are cheap, not free.
    # Native experimental long context raises both limits to 262k via
    # TypeSafe-Danger-Zone-Long-Context: true, with lower speed and accuracy.
    # This example keeps the defaults: https://docs.typesafe.ai/models


if __name__ == "__main__":
    main()
