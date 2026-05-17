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

// --- tests ---
console.log(firstSoloVisitor(["a", "b", "c", "a", "b"])); // expect 2
console.log(firstSoloVisitor(["x", "y", "z", "x", "y", "z"])); // expect -1
console.log(firstSoloVisitor(["a", "a", "b"])); // expect 2
console.log(firstSoloVisitor(["only"])); // expect 0
