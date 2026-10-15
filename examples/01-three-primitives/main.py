"""The three core primitives in one request.

The state is ingested once and every question is evaluated against it in
parallel, so asking three things costs about what asking one costs plus the
question tokens. That is the property the rest of the examples build on.

Run:
    pip install typesafe-sdk
    export TYPESAFE_API_KEY=...
    python main.py

No key yet? The official system-one-adapter package is a drop-in replacement
backed by ordinary LLM APIs. The shapes match; the calibration does not, so do
not tune a threshold against it.
"""

from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

TICKET = (
    "I've been trying to connect my payment provider for three days and the "
    "integration keeps failing. I'm losing sales. Please help ASAP."
)


def main() -> None:
    client = TypeSafeClient()

    response = client.system_one(
        state=TICKET,
        questions={
            # Choice: one option out of a closed set. Max 255 options.
            # The criteria descriptions do the work — they are where your
            # domain knowledge and boundary cases belong.
            "department": Choice(
                instructions="Which team should handle this",
                criteria={
                    "billing": "Payment or subscription issues",
                    "technical": "Bugs or integration problems",
                    "sales": "Pricing or account questions",
                },
            ),
            # Score: a position on an ORDERED scale, 2 to 10 levels, 0-indexed.
            # Use this only when the levels genuinely have an order. Unordered
            # categories wearing numbers belong in a Choice.
            "frustration": Score(
                instructions="How frustrated the customer appears",
                criteria=[
                    "Calm, just stating facts",
                    "Frustrated but civil",
                    "Very angry, strong language",
                ],
            ),
            # Noul: a yes-no probability. Note there is no separate confidence
            # on a noul answer — the probability IS the answer.
            "is_urgent": Noul(
                instructions="The message conveys urgency or time-sensitivity",
            ),
        },
    )

    department = response.answers["department"]
    frustration = response.answers["frustration"]
    urgent = response.answers["is_urgent"]

    print(f"model            {response.model}")
    print(
        f"department       {department.choice}  (confidence {department.confidence:.2f})"
    )
    print(f"                 {department.probabilities}")

    # A score is probability-weighted, so it lands BETWEEN levels. Do not
    # assume an integer and do not round it before you have decided why.
    print(
        f"frustration      {frustration.score:.2f}  (confidence {frustration.confidence:.2f})"
    )
    print(f"                 legend {frustration.legend}")

    # No .confidence here — reaching for one returns nothing.
    print(f"is_urgent        {urgent.noul:.2f}")


if __name__ == "__main__":
    main()
