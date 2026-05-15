/*
 * PROBLEM: Overtime Flagging
 *
 * You're building a shift-scheduling tool for a staffing agency. Every time an
 * employee works a shift, their ID gets appended to a log array. At the end of
 * the week, managers need to know which employees hit a minimum shift threshold
 * so they can be flagged for overtime review.
 *
 * Write a function that accepts:
 *   shifts    — string[] of employee IDs (one entry per shift worked, with duplicates)
 *   minShifts — integer minimum threshold (inclusive)
 *
 * Return a sorted string[] of employee IDs who worked AT LEAST minShifts shifts.
 * If no employees meet the threshold, return [].
 *
 * Constraints:
 *   - 0 <= shifts.length <= 10,000
 *   - 1 <= minShifts
 *   - Employee IDs are non-empty strings
 *   - Return value must be sorted ascending
 *
 * Examples:
 *   frequentWorkers(["E1","E2","E1","E3","E2","E1"], 2)  →  ["E1","E2"]
 *   frequentWorkers(["E1","E2","E1","E3","E2","E1"], 3)  →  ["E1"]
 *   frequentWorkers(["E1","E2","E3"], 2)                 →  []
 */

function frequentWorkers(shifts: string[], minShifts: number): string[] {
  // 1. create a map of each employee ID with a count of how many shifts they had

  const shiftMap = new Map();
  for (const shift of shifts) {
    // get the shift, if it doesn't exist, set it as zero, if it does exist + 1 to it
    shiftMap.set(shift, (shiftMap.get(shift) || 0) + 1);
  }

  // 2. from this map, determine for each employee if their shift count >= minShifts, and if so, add that worker to an array
  const flaggedEmployees = Array.from(shiftMap.entries())
    .filter(([_, count]) => count >= minShifts)
    .map(([id]) => id)
    .sort();

  return flaggedEmployees;
}

// --- tests ---
console.log(
  JSON.stringify(frequentWorkers(["E1", "E2", "E1", "E3", "E2", "E1"], 2)),
); // expected: ["E1","E2"]
console.log(
  JSON.stringify(frequentWorkers(["E1", "E2", "E1", "E3", "E2", "E1"], 3)),
); // expected: ["E1"]
console.log(JSON.stringify(frequentWorkers(["E1", "E2", "E3"], 2))); // expected: []
console.log(JSON.stringify(frequentWorkers([], 1))); // expected: []
console.log(JSON.stringify(frequentWorkers(["A", "A", "A"], 3))); // expected: ["A"]
