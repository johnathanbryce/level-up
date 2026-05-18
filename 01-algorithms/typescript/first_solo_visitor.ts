/**
 * First Solo Visitor
 *
 * A website logs each visitor by ID in the order they arrived.
 * Some visitors come back multiple times in the same session;
 * others visit only once.
 *
 * Return the INDEX of the first visitor in the log who appears
 * exactly once. If every visitor appears more than once, return -1.
 *
 * Constraints:
 *  - visitors is a non-empty array of strings (visitor IDs)
 *  - case-sensitive ("abc" !== "ABC")
 *  - return the index (number), not the visitor ID
 *
 * Examples:
 *  ["a", "b", "c", "a", "b"]       → 2   (c is the first to appear exactly once)
 *  ["x", "y", "z", "x", "y", "z"]  → -1  (everyone appears twice)
 *  ["a", "a", "b"]                 → 2   (b appears once; a appears twice)
 *  ["only"]                        → 0   (single visitor appears once)
 */

function firstSoloVisitor(visitors: string[]): number {
  // loop over visitors and get a count of each visitor  with key-value of

  const visitorsMap = new Map();

  for (const visitor of visitors) {
    visitorsMap.set(visitor, (visitorsMap.get(visitor) || 0) + 1);
  }

  // if a visitor's count === 1, find that visitor in the original array and return the index of it
  const flaggedVisitors = Array.from(visitorsMap.entries()).find(
    ([key, count]) => count === 1,
  );

  if (flaggedVisitors) {
    const firstSoloVisitor = flaggedVisitors[0];
    return visitors.indexOf(firstSoloVisitor);
  }

  return -1;
}

// --- tests (John's version) ---
console.log(firstSoloVisitor(["a", "b", "c", "a", "b"])); // expect 2
console.log(firstSoloVisitor(["x", "y", "z", "x", "y", "z"])); // expect -1
console.log(firstSoloVisitor(["a", "a", "b"])); // expect 2
console.log(firstSoloVisitor(["only"])); // expect 0

// ---------------------------------------------------------------------------
// Reference solution — canonical "count then walk" two-pass pattern.
// Differences vs John's version:
//   1. Pass 2 walks the ORIGINAL array (visitors), not the Map's entries.
//      This is the canonical pattern: build the lookup in pass 1, consume
//      it from the original array in pass 2.
//   2. No need for Array.from(map.entries()).find(...) + visitors.indexOf(...).
//      That detour is O(n) extra space + two extra scans.
//   3. Correctness doesn't rely on Map insertion order being preserved
//      (it IS preserved per spec, but the canonical version doesn't care).
// ---------------------------------------------------------------------------

function firstSoloVisitorCanonical(visitors: string[]): number {
  const counts = new Map<string, number>();

  for (const v of visitors) {
    counts.set(v, (counts.get(v) || 0) + 1);
  }

  for (let i = 0; i < visitors.length; i++) {
    if (counts.get(visitors[i]) === 1) return i;
  }

  return -1;
}

// Even tighter, idiomatic JS using .findIndex:
function firstSoloVisitorTerse(visitors: string[]): number {
  const counts = new Map<string, number>();
  for (const v of visitors) counts.set(v, (counts.get(v) || 0) + 1);
  return visitors.findIndex(v => counts.get(v) === 1);
}

// --- tests (reference) ---
console.log("--- canonical ---");
console.log(firstSoloVisitorCanonical(["a", "b", "c", "a", "b"])); // expect 2
console.log(firstSoloVisitorCanonical(["x", "y", "z", "x", "y", "z"])); // expect -1
console.log(firstSoloVisitorCanonical(["a", "a", "b"])); // expect 2
console.log(firstSoloVisitorCanonical(["only"])); // expect 0
