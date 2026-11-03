# awesome-jev-mcp

Query the [awesome-jev](https://github.com/kydlikebtc/awesome-jev) catalogue
from an agent instead of reading it.

A catalogue about how agents make decisions that only humans can read is a
strange artefact. This exposes it: an assistant about to wire Jev into
something can ask for examples of the exact decision it is making, on the
platform it is using, in the language it is writing.

## Install

**In Claude Code**, install the plugin. It brings this server and the
[agent skill](https://github.com/kydlikebtc/awesome-jev/blob/main/skills/awesome-jev/SKILL.md) together, and starts the server
for you:

```
/plugin marketplace add kydlikebtc/awesome-jev
/plugin install awesome-jev@awesome-jev
```

The plugin launches the server with `uvx`, so it needs
[uv](https://docs.astral.sh/uv/) on your PATH. It rebuilds the package from the
plugin's own copy every time it starts, which costs about two seconds in the
background. Without that, uvx keeps the first environment it built for a local
directory and ignores later changes to it — so a plugin whose code or bundled
snapshot had been updated would go on running the old one, with nothing to say
so. The dependencies stay cached; only this package is rebuilt.

**Anywhere else**, install the package and register the command with your
client:

```bash
pip install awesome-jev-mcp
awesome-jev-mcp
```

It speaks stdio, so any MCP client works. The catalogue it serves is fetched
from the repository's `main`, not frozen into the release, so a release only
needs upgrading for changes to the server itself. If pip finds no
`awesome-jev-mcp` to install, or to run the server as it is on `main` rather
than as released, install it from the repository:

```bash
pip install git+https://github.com/kydlikebtc/awesome-jev
```

Needs the 2.x MCP SDK, which the package declares. `MCPServer` is the name 2.x
gave what 1.x called `FastMCP`, so an environment already pinned to `mcp<2`
resolves to something that dies at import — check that first if the server
never starts.

## Tools

| Tool                 | What it answers                                                    |
| -------------------- | ------------------------------------------------------------------ |
| `search_examples`    | "Show me safety-gating examples in TypeScript that call `noul`." Also "which benchmarks compared Jev with Cohere, or used LongMemEval?": a benchmark's `measurement` is its author's report, indexed, the direction author-stated and not reproduced here. `outcome="negative"`: the rows whose own author measured Jev and concluded against it. |
| `get_example`        | One row in full, including its sources and its `evidence`.         |
| `list_patterns`      | The decision taxonomy, with how many examples exist for each and what is recorded about them (reports counted, not a verdict). |
| `compatibility`      | Model string, field names, request shape and env var per platform, and how many catalogued rows record it. |
| `check_model_string` | "Is `typesafe/jev-1` real?" — it is not, and that matters.         |
| `launch_board`       | The weekly launch board: the running week (shuffled, no counts until it closes), the last closed week ranked, the next week. Each launch carries its votes and its catalogue evidence side by side, never added together. |
| `top_launches`       | "Which safety-gating products placed best?" — each product once, at its best week. A rank is a count of votes, not a recommendation. |

## Resources

| Resource                          | What it holds                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------- |
| `awesome-jev://flags`             | What each caveat flag means, in English and Chinese.                              |
| `awesome-jev://collections`       | The curated entry points: a first call, projects to adapt, measurements.          |
| `awesome-jev://collections/{id}`  | One curated path in order, each pick's reason and caution beside the row itself. |
| `awesome-jev://patterns/{key}`    | Every row filed under one decision pattern, caveated rows included.               |

Each is JSON with the same `data` line as a tool result. The pattern resource
holds the same rows, in the same order, as the catalogue site's
`api/v1/patterns/<key>.json`, plus a link to the pattern's section of
`docs/patterns.md`, which holds its "when not to" where one is written.

## Prompt

`wire_pattern(pattern, language, surface)` puts what a coding agent needs to
wire one decision into a single message: the pattern's description and a link
to its section of `docs/patterns.md`; the surface's model strings, request
envelope, answer field and key variable from `compat.json` (or the surfaces to
choose from); up to five catalogued rows under the pattern that cite the file
their code was read in, each linked with its caveats; and, when this
repository ships one for that pattern and language, the example's code under a
comment saying it was never executed. Without one it says so rather than
guessing. The examples come from `examples/index.json`, generated from the
catalogue rows that describe them, and reach the server by the same ladder as
the catalogue, the first time the prompt is asked for.

## Three things it does on purpose

**Caveats are never optional.** Every result carries its flags. An agent that
got a recommendation without `not-jev` or `vendor-reported` attached would be
worse informed than one that read the README. Rows keep the bare flag keys, and
every answer holding flagged rows ends with a `caveat_glossary` saying what
those flags mean.

**Reimplementations are excluded by default.** Rows flagged `not-jev` do not
call the API and `shadow-mode-only` rows are deliberately inert; neither
answers "how do I do this". Pass `include_non_jev=True` when you want them.

**Every result says how current it is.** The catalogue changes; this package
does not change with it. So each result carries a `data` line naming which
source answered, and anything stale says so in capitals:

```
"data": "revalidated against GitHub · <rows> rows · catalogue checked <date>"
"data": "STALE — network unreachable, serving the last copy fetched to this machine · …"
```

## Where the catalogue comes from

Installed as a package there is no repository around this code, so the five JSON
files — `catalog.json`, `compat.json`, `patterns.json`, `taxonomy.json` and
`collections.json`, the five the catalogue's site loads too — have to be
fetched. They are, in this order, and the first complete answer wins:

|     | Source                                                          | Reported as           |
| --- | --------------------------------------------------------------- | --------------------- |
| 1   | `AWESOME_JEV_CATALOG`, a directory holding the five files       | `override`            |
| 2   | A repository checkout above this file, when running from source | `checkout`            |
| 3   | GitHub, conditional on the cached ETag                          | `network`             |
| 4   | The cache, when the network fails                               | `cache` — **stale**   |
| 5   | The snapshot inside the wheel, when there is no cache either    | `bundled` — **stale** |

Layer 3 is the normal case and costs almost nothing after the first run: GitHub
answers a revalidated request with `304` and no body, so the steady state is
five small round trips rather than megabytes.

Layer 5 is the offline first run. It works, and it is the one source that can be
arbitrarily old, so it is the loudest.

`examples/index.json`, which only the `wire_pattern` prompt reads, climbs the
same ladder on its own the first time the prompt is asked for: a source
without it costs the prompt its skeleton, not the server its catalogue, and
the prompt names the source that served it.

Three properties worth stating plainly, because two of them are trade-offs:

- **The five files always move together.** A source supplies all of them or it
  is skipped. A fresh `catalog.json` beside a cached `patterns.json` could use a
  pattern key the taxonomy does not have yet, and that is a correctness bug
  rather than untidiness.
- **A stale answer is never presented as fresh.** That is the whole reason the
  `data` line exists on every result instead of only on degraded ones: a warning
  that appears only when something is wrong teaches readers to skim past it.
- **This version reaches the network, and earlier ones did not.** Before it was
  packaged, the server read the repository it sat inside, which made it offline
  by construction. Fetching is what buys a catalogue that stays current after
  you install it once; the cost is a dependency on GitHub being reachable, paid
  down by the cache and the bundled snapshot. `AWESOME_JEV_CATALOG` opts out
  entirely.

## Why this has a dependency when the rest of the repository does not

The catalogue's own pipeline — lint, build, verify, refresh — is stdlib-only, so
CI stays `setup-python` with no install step, and nothing under `scripts/`
imports anything declared in `pyproject.toml`. Hand-rolling stdio JSON-RPC would
extend that streak to here too, but a subtly broken MCP server is worse than a
dependency.

The dependency stops at `server.py`, which only registers the tools, the
resources and the prompt and adds the `data` line. What they answer — which
rows count as examples, the caveats and what each means, the order, the
model-string check, the prompt's text — is `query.py` and `prompts.py`, and
where the data comes from is `data.py`. Every module but `server.py` is
standard library only, so the repository's CI tests them on every pull request
without installing
`mcp` (`tests/test_mcp_query.py`, `tests/test_mcp_resources.py`,
`tests/test_mcp_prompt.py`, `tests/test_mcp_data.py`). The package build in
`publish.yml`, which runs on every change to the package, is the one place the
SDK itself is installed, and it checks there that every tool, resource and
prompt is registered.
