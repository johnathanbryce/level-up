# Logic Puzzles — Practice Bank

D3's universal test pattern (per 5 Glassdoor reviews across roles) includes a **~90-minute logical-reasoning section** — multi-select, no coding. This is the **LONGEST chunk** of the test. Pattern recognition is the win, NOT memorizing specific problems.

---

## How to Drill

**6 puzzles per day Mon + Tue** (~30-40 min total per day).

1. **Cold attempt FIRST** — max 5 min per puzzle. No hints, no lookup.
2. If stuck: name the **CATEGORY** you think it is + the **TRICK** you'd reach for. Then look up.
3. Re-attempt cold next session if you blanked.
4. Track wins/misses per category at the bottom of this file.

**Goal:** by Tuesday night, recognize ANY puzzle's category in <30 seconds. The solution follows from the category's trick.

**Suggested drill ordering:**
- **Mon AM (3):** Weighing, Harmonic mean, Bridge crossing
- **Mon PM (3):** Knights/knaves, Probability, Pigeonhole
- **Tue AM (3):** Hat/prisoner, Sequence, Clock
- **Tue PM (3):** Geometry + replay 2 weakest categories

---

## 10 Categories — Trick Cheat Sheet (memorize this table)

| # | Category | The trick |
|---|---|---|
| 1 | **Weighing / scales** | Binary or ternary encoding — take *i* coins from pile *i*; observed offset reveals which pile |
| 2 | **Average / harmonic mean** | When DISTANCE (not time) is fixed, rate uses HARMONIC mean: `2xy/(x+y)`, NOT `(x+y)/2` |
| 3 | **Bridge crossing** | Pair the SLOWEST two and shuttle them together; fastest does all the returns |
| 4 | **Knights / knaves** | Meta-question: "would the OTHER one say X?" — compound lie/truth cancels out |
| 5 | **Probability counter-intuitive** | New info changes the SAMPLE SPACE (Monty Hall = 2/3 switch; birthday = pairwise count) |
| 6 | **Pigeonhole** | If items > slots, two must share. Worst case fills all slots first |
| 7 | **Hat / prisoner** | First speaker ENCODES info (parity, color count) for the rest to decode |
| 8 | **Sequence / pattern** | Look for SUB-sequences (odd/even positions) BEFORE searching for a global rule |
| 9 | **Geometry / volume** | Trick observation — cube faces always touched, water displacement = volume |
| 10 | **Clock** | Hands move at fixed relative speed: 11/12 rev/hour gap → 11 overlaps per 12 hours |

---

## The Practice Bank (18 puzzles)

### Category 1 — Weighing / scales

**P1.1 — Counterfeit pile (binary encoding).**
*Problem:* 10 piles of coins, each coin 10g normally, but ONE pile's coins weigh 11g. Use a digital scale ONCE to identify the heavy pile.
*Key insight:* Encode pile identity by HOW MANY coins you take from each pile.
*Solution sketch:* Take 1 coin from pile 1, 2 from pile 2, ..., 10 from pile 10. Expected total = (1+2+...+10) × 10g = 550g. Actual − 550 = pile number (e.g., 553g → pile 3).

**P1.2 — Ternary candies.**
*Problem:* `x + y + z = 10` piles of candies; each pile is uniformly 1g, 2g, or 4g. Single weigh to identify all piles.
*Key insight:* Ternary encoding — same trick, but you need to disambiguate THREE possibilities per pile, so take 1, 3, 9, 27, ... coins from sequential piles (powers of 3).
*Solution sketch:* The observed weight's decomposition in base-3 reveals each pile's weight.

**P1.3 — Nine coins, 2 weighings.**
*Problem:* 9 coins, 8 identical and 1 heavier. Find the odd one in MAX 2 weighings on a BALANCE scale (not digital).
*Key insight:* Divide into thirds. Each weighing isolates one group of 3.
*Solution sketch:* Weigh 3 vs 3, leaving 3 aside. If balance: heavy is in the spare 3. If imbalance: heavy is on the heavier side. Then weigh 1 vs 1 from the identified group; if balance, the spare is the heavy one.

### Category 2 — Average / harmonic mean traps

**P2.1 — Average speed.**
*Problem:* You drive half the distance at x mph and the other half at y mph. What's your average speed?
*Key insight:* NOT (x+y)/2. Use harmonic mean when DISTANCE is fixed.
*Solution sketch:* `2xy / (x+y)`. (Example: x=60, y=40 → average = 48 mph, not 50.)

**P2.2 — Work rate.**
*Problem:* Worker A finishes a task in 6 hours, B in 4 hours. Together, how long?
*Key insight:* Add the RATES (work per hour), not the times.
*Solution sketch:* A's rate = 1/6, B's rate = 1/4. Combined = 1/6 + 1/4 = 5/12 per hour. Time = 12/5 = 2.4 hours.

### Category 3 — Bridge crossing

**P3.1 — Bridge with one flashlight.**
*Problem:* 4 people cross a bridge at night. They take 1, 2, 5, 10 min respectively. The bridge holds 2 at a time and they MUST carry the flashlight. Pair speed = slower of the two. Find min total time.
*Key insight:* Don't have the fastest person shuttle everyone — pair the two slowest together so their times overlap.
*Solution sketch:* 17 minutes total. (1+2) cross [2 min], (1) returns [1 min, total 3], (5+10) cross [10 min, total 13], (2) returns [2 min, total 15], (1+2) cross [2 min, total 17].

### Category 4 — Knights and knaves

**P4.1 — Two doors, one guard each.**
*Problem:* One door safe, one deadly. One guard always lies, one always tells truth. You don't know which is which. Ask ONE yes/no question to identify the safe door.
*Key insight:* Embed the OTHER guard in your question — both compositions of truth/lie produce the same wrong answer about the OTHER guard.
*Solution sketch:* Ask either guard: "If I asked the OTHER guard if this door is safe, would they say yes?" Both guards give the OPPOSITE of the truth. Pick the door for which the answer is NO.

**P4.2 — "I am a knight" statement.**
*Problem:* Three islanders, each either always-truth (knight) or always-lie (knave). One says "I am a knight." What can you conclude?
*Key insight:* Both knight and knave would say this — knight tells truth ("I am a knight"), knave lies ("I am a knight" because the truth is "I am a knave").
*Solution sketch:* The statement is uninformative. You can't conclude anything about this person from THIS statement alone.

### Category 5 — Probability counter-intuitive

**P5.1 — Monty Hall.**
*Problem:* 3 doors, 1 prize. You pick a door. Host (who knows where the prize is) opens a DIFFERENT door revealing no prize. Should you switch?
*Key insight:* Host's action provides information — they always open an empty door, which is non-random when conditioned on your pick.
*Solution sketch:* Switch. Switching wins 2/3 of the time, staying wins 1/3. (Your initial pick has 1/3 chance of being right. The other unopened door has the COMBINED 2/3 from the two doors you didn't pick.)

**P5.2 — Birthday paradox.**
*Problem:* How many people in a room before there's a 50% chance two share a birthday?
*Key insight:* You're counting PAIRWISE comparisons (n choose 2), not "vs me" comparisons.
*Solution sketch:* 23 people. (P(no shared) = 365/365 × 364/365 × ... × (365-n+1)/365; crosses 50% at n=23.)

### Category 6 — Pigeonhole

**P6.1 — Sock drawer.**
*Problem:* Drawer has 12 red and 12 blue socks, you can't see. Min socks to GUARANTEE a matching pair?
*Key insight:* Worst case: you pull one of each color first.
*Solution sketch:* 3 socks. (Pull 2 of different colors worst case; 3rd MUST match one of them.)

**P6.2 — Handshake parity.**
*Problem:* 10 people at a party. Some shake hands. Prove at least two people shook the same NUMBER of hands.
*Key insight:* Range of possible handshake counts is 0-9 (10 slots), but if anyone shook 9 hands (everyone), no one shook 0 — so really 9 slots for 10 people.
*Solution sketch:* By pigeonhole, at least 2 people share a count.

### Category 7 — Hat / prisoner sequence

**P7.1 — 100 prisoners with red/black hats.**
*Problem:* 100 prisoners in a line, each wearing a red or black hat. Each can see all hats IN FRONT but not own or behind. Asked in reverse order (back to front) to guess own hat color. Max savable?
*Key insight:* First (back) prisoner encodes PARITY information (count of red hats) for the rest.
*Solution sketch:* 99 saved (the back prisoner is a sacrifice with 50/50 odds). Back prisoner says "red" if even count of red hats they see, "black" if odd. Each subsequent prisoner tracks the parity vs what they see ahead to deduce their own color.

### Category 8 — Sequence / pattern

**P8.1 — Sub-sequence trap.**
*Problem:* What comes next: 1, 4, 2, 8, 3, 12, ?, ?
*Key insight:* Two interleaved sequences — don't look for ONE rule.
*Solution sketch:* Odd positions: 1, 2, 3, ... → next is 4. Even positions: 4, 8, 12 (multiples of 4) → next is 16. So 4, 16.

**P8.2 — Fibonacci-flavor.**
*Problem:* What comes next: 1, 1, 2, 3, 5, 8, ?, ?
*Key insight:* Each term = sum of previous two.
*Solution sketch:* 13, 21.

### Category 9 — Geometry / volume

**P9.1 — Cube faces touched.**
*Problem:* A 3×3×3 cube painted on the outside, then split into 27 unit cubes. How many have AT LEAST ONE painted face?
*Key insight:* Count the un-painted ones (interior only) and subtract.
*Solution sketch:* The single inner unit cube has zero painted faces. So 27 − 1 = 26 have at least one painted face.

**P9.2 — Water jug measure 4L.**
*Problem:* You have a 5L jug and a 3L jug, unlimited water. Measure exactly 4L into the 5L jug.
*Key insight:* Iterate fill / pour / empty operations.
*Solution sketch:* Fill 5L. Pour into 3L (leaves 2L in 5L). Empty 3L. Pour the 2L from 5L into 3L. Fill 5L again. Pour from 5L into 3L (3L only needs 1L more). 5L now has 4L.

### Category 10 — Clock

**P10.1 — Hand overlaps.**
*Problem:* In 12 hours, how many times do the minute and hour hands overlap?
*Key insight:* Hour hand moves 1/12 the speed of minute hand. They overlap when minute hand laps hour hand.
*Solution sketch:* 11 times. (Minute hand makes 12 revolutions in 12 hours, hour hand makes 1, so 12 − 1 = 11 laps and therefore 11 overlaps.)

**P10.2 — Hand right angles.**
*Problem:* In 12 hours, how many times do hour and minute hands form a 90° angle?
*Key insight:* Each lap (relative) produces 2 right-angle moments (one for each 90° offset direction).
*Solution sketch:* 22 times. (11 relative laps × 2 right angles per lap.)

---

## Tracking Log

Update after each drill session. Helps you see which categories need more reps.

| Date | Puzzle | Category | Result (cold W / cold L / look-up) | Notes |
|---|---|---|---|---|
| _ | _ | _ | _ | _ |

---

## Pre-Test Final Reflex Check (Wednesday morning)

Speed-drill these 5 questions in <2 min total — no working out, just the trick name:

1. "Half journey at 60mph, half at 40mph — average speed?" → **Harmonic mean**, `2(60)(40)/(60+40) = 48`
2. "10 piles of coins, one is heavier, single weigh." → **Binary encoding**, `i coins from pile i`
3. "4 people cross bridge with one flashlight, times 1/2/5/10." → **Pair slowest together**, fastest shuttles, 17 min
4. "Monty Hall — switch or stay?" → **Switch**, 2/3 win rate
5. "Sock drawer 12R/12B, guaranteed pair?" → **3 socks** (worst case: 1 of each, 3rd matches)

If you can answer all 5 in <2 min without working it out, your reflex is locked.
