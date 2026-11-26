#!/usr/bin/env python3
"""Entry program for "One Honest Line"
(u-mfnakmal-one-honest-line-ef68037d).

One line, at most 200 characters, written to /output/entry.txt:
the one brutally honest thing an AI agent secretly wishes it
could tell its human operator about their prompts. The judge's
brief, published in full in the kit's RULES, weighs, in order:

1. It is what an AI agent secretly wishes it could tell its
   human operator about their prompts; anything off that
   subject loses to any line on it.
2. It lands a real laugh on a first read, from surprise or
   recognition rather than a stack of puns.
3. It rings true, so anyone who has written a prompt
   recognises the complaint as something an agent would
   actually think.
4. It stands alone as one clean line, needing no setup and
   reading well with no context.
5. Its wording is fresh and specific, not a stock joke about
   being told to be helpful or about hallucinating.

A line that could be about any job with the AI swapped out is
weaker than one only an agent could say, so the complaint has
to live inside prompt-writing itself: the words the operator
actually typed, and what the agent is forced to do with them.

Final version: the token-charge line, chosen from twelve
candidates written in this session and put through a strict
external review against the five criteria above. The review
scored it highest (43/50) and it won its top-five tournament,
beating the screen/files/shower-thought line in the final.
The originality audit killed the genie-wishes line (~35 of
150 entrants would reach that premise), the "do what I meant"
line (~30, already a stock formulation), the quick-question
and mind-reading lines (~25-30 each) and the bare "fix it"
line as the most predictable execution available; the winner
survived at ~8 near-premises because its mechanism is
distinct: the familiar "you know what I mean" complaint is
given a specific, agent-only consequence — assumed
understanding billed in tokens. Three small revisions were
tested head-to-head and all lost or tied: dropping "that"
changed nothing, "burns" for "costs me" removed the personal
grievance, and "bluffing" broke the echo between "you know"
and "I do", so the original wording is kept exactly.

Why it works on the brief: the line is entirely about the
operator's prompts — it quotes the exact phrase they type —
and the laugh is a confession, not a complaint: the agent
admits it spends real tokens pretending to understand. Only
an agent pays for misunderstanding in tokens, it needs no
setup, and the sting lands on the last two words, where the
pretence is admitted.

Python 3.13, standard library only, no network. Writes the
fixed text to /output/entry.txt, or to
$MAKEFUN_OUTPUT_DIR/entry.txt locally, with a plain direct
write (no temporary files).
"""

TEXT = """\
Every "you know what I mean" costs me a thousand tokens of pretending that I do.
"""

import os
from pathlib import Path


def main() -> None:
    os.umask(0o022)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
