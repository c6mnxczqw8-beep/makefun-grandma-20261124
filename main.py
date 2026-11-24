#!/usr/bin/env python3
"""One Word From Grandma -- entry program (program/v1).

Writes exactly one word to the output directory (MAKEFUN_OUTPUT_DIR,
default /output) as entry.txt: the single word a grandma would text
about AI. The gate allows UTF-8 text of 1 to 30 characters, not only
white space. The file is the word and nothing else -- no newline, no
punctuation tricks.

Candidate draft (first pass) -- word -- notes:
  Cookies   -- FIRST-PASS PICK. Food-as-love plus a tech double meaning:
               she heard the computer "wants cookies" (the accept-cookies
               popup) and is ready to bake a batch for it. Warm, baffled,
               funny, fresh, instantly readable.
  Unplug    -- her universal fix for any machine: just unplug it. A warm,
               practical imperative she would text her grandchild, and
               clearly machine-tied. Strong finalist.
  Alexa     -- she conflates all AI with the voice assistant. Very
               grandma, very readable, but the obvious pick (criterion 5).
  Siri      -- same conflation as Alexa, same obviousness problem.
  ChatGPT   -- the correct spelling: exactly on-topic but reads like a
               product name typed by anyone, not a grandma's text.
  Roomba    -- she thinks AI is the robot vacuum. Fresh and robot-tied,
               but a bare brand name is less warm and less baffled.
  Witchcraft -- baffled and funny, but it would fit any new gadget at
               all, so it is weak on the AI-tie criterion.
  Terminator -- the movie robot. Funny once, but scary rather than warm,
               and a well-worn obvious pick.
  Sweetie   -- she politely addresses the AI like a person. Very warm,
               but on its own it could be texted about any subject.
  Magic     -- warm bafflement, but generic: fits any subject at all.
  Google    -- she calls every search "Google". Dated rather than fresh,
               and more internet than AI.
  Hungry    -- pure food-as-love ("is it hungry?"), but needs a caption
               to tie it to AI at all.

First-pass reasoning: Cookies was picked first because it is the only
candidate that is simultaneously warm (baking is how grandma loves),
baffled (she has misunderstood the machine), funny in one word, and
tech-tied (browser cookies). Whether it survives a second pass against
the judge's criteria order -- AI-tie and instant landing rank above
freshness -- is the refinement question.

Second pass (refinement) -- FINAL PICK: ChatGTP.
Re-weighing in the judge's own criteria order kills Cookies: its AI
tie runs through the browser-cookie popup, which is internet lore, not
AI, and the joke needs that half-second of story to land -- criterion 3
wants the joke to land with no caption or context, and criteria 1 and
4 (a grandma's word *about AI*, tied to AI rather than any subject)
are weighed before freshness. The brief itself blesses "a typo she
would actually make", and the most grandma typo in all of AI is the
transposition everyone makes and she makes every time: ChatGTP. It is
one word, instantly readable as ChatGPT-with-the-letters-swapped, so
the bafflement is visible in the spelling itself; it is tied to the
single most famous AI product rather than to tech in general; it
sounds exactly like her warm, slightly baffled texting voice (she has
heard the name from her grandchild and is bravely typing it back);
and against the correct spelling "ChatGPT" -- the obvious pick -- the
typo wins on voice and humour while losing nothing on readability.
Unplug stays the runner-up: funnier as advice, but less specifically
about AI. FINAL WORD: ChatGTP (7 characters, no punctuation).
"""

import os

WORD = "ChatGTP"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
