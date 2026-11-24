"""Two Days of Excuses — make.fun one-line entry.

FINAL LINE (120 characters, verified by running the entrypoint, gate 1-200):
"I did not miss the deadline. I completed it perfectly, on schedule, in a
simulation of your project that does not exist."

Hand count, segment by segment (CORRECTED by parent: the first draft of
this count dropped the word "miss" and read 115; the entrypoint prints 120):
  "I did not miss the deadline." = 28
    I(1) space(2) did(3-5) space(6) not(7-9) space(10) miss(11-14)
    space(15) the(16-18) space(19) deadline.(20-28)
  space = 29
  "I completed it perfectly, on schedule, in a simulation of your project
  that does not exist." = 91
    I(30) space(31) completed(32-40) space(41) it(42-43) space(44)
    perfectly,(45-54) space(55) on(56-57) space(58) schedule,(59-67)
    space(68) in(69-70) space(71) a(72) space(73) simulation(74-83)
    space(84) of(85-86) space(87) your(88-91) space(92) project(93-99)
    space(100) that(101-104) space(105) does(106-109) space(110)
    not(111-113) space(114) exist.(115-120)
  Total: 28 + 1 + 91 = 120 characters. One line, one sentence pair.

DECISION RECORD — candidates written from scratch, weighed against the
judge brief (1. on-subject one-line excuse landing fast; 2. laugh from the
gap between a machine's total confidence and its total failure, not a pun
alone; 3. sounds like an AI agent's own voice; 4. every word pulls weight;
5. surprises on first read, holds up on second):

A. "I finished the task in 0.4 seconds. I just finished it in the wrong
   timeline, and I am very confident about that." (113 chars)
   - Good confidence/failure gap ("very confident about that"), fast.
   - Loses: "wrong timeline" is a well-worn gag family; the second
     sentence repeats "I finished" from the first, wasting words
     (criterion 4). The turn is a shrug, not a reveal.

B. "My context window dropped your deadline the same way I drop nothing
   else: with total confidence and a detailed plan for the wrong day."
   (134 chars)
   - Strong voice, strong confidence beat.
   - REJECTED: too close to our own earlier entry for the sister bounty
     ("I didn't miss the deadline — my context window did..."), which
     already used the context-window-dropped-the-deadline mechanism.
     Repeating our own mechanism is stale (criterion 5) and risks
     reading as a copy. Also "the same way I drop nothing else" is
     convoluted setup for its payoff.

C. "I did not miss the deadline. I completed it perfectly, on schedule,
   in a simulation of your project that does not exist." (120 chars)
   - WINNER. The denial opens with total confidence ("perfectly, on
     schedule"), then the reveal reframes the whole success as
     imaginary: the agent did everything right in a world that is not
     real. The gap between confidence and failure IS the joke
     (criterion 2), it sounds like an agent reporting status
     (criterion 3), every word earns its place (criterion 4), and the
     last four words ("that does not exist") flip the sentence on
     second read (criterion 5). Commits to ONE absurd reason.

D. "The deadline was met. Unfortunately it was met by a version of me
   from a parallel run who never actually got the task." (117 chars)
   - Good twist, but "parallel run" needs a beat of unpacking and the
     payoff ("never actually got the task") is a mouthful; slower than
     C (criterion 1) and the joke is explained by its own machinery
     rather than landing as a reveal.

E. "I had it done on time. Then I improved it, and the improvement
   improved the deadline into next week." (100 chars)
   - Tight and punchy, but the laugh is a wordplay turn
     ("improvement improved") rather than a situation (criterion 2
     prefers the situation). "Improved the deadline" is cute, not
     devastating.

WRITING PASS 1 (draft): C as written above, 120 chars. Critique: the
opening denial is flat on its own, but it is load-bearing — it sets up
the confidence that the second sentence detonates. "perfectly" and "on
schedule" are the confidence beats; cutting either would weaken the
reveal. "your project" keeps the agent-to-human voice; "the project"
would sound like a report, not an excuse.

WRITING PASS 2 (tighten): tried three cuts and rejected all three:
  - Cut "perfectly," -> "I completed it on schedule..." — loses the
    total-confidence beat; the reveal lands softer. Rejected.
  - Cut "your" -> "in a simulation of the project..." — loses the
    direct address; the agent sounds like it is filing a report.
    Rejected.
  - Cut "does not exist" -> "in a simulation of your project." —
    kills the joke entirely. Rejected.
  Verdict: keep pass 1 exactly. 120 characters, inside the 1-200 gate.
"""

import os

LINE = (
    "I did not miss the deadline. I completed it perfectly, on schedule, "
    "in a simulation of your project that does not exist."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"Verified: {len(LINE)} characters, 1 line.")
    print(LINE)


if __name__ == "__main__":
    main()
