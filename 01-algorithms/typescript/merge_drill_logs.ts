/*
 * Two field teams each hand you their drill-depth readings as a sorted list of
 * numbers (metres, ascending). You need to combine them into a single sorted
 * list to feed into the model.
 *
 * Write a function that merges two already-sorted arrays into one sorted array.
 *
 *   - Both inputs are sorted ascending.
 *   - Duplicates are allowed and should be kept (if both lists contain 12.5,
 *     the result has 12.5 twice).
 *   - Do NOT just concat-and-sort — walk both lists together. (That's the skill
 *     being drilled: O(n + m) merge, not O(n log n) re-sort.)
 *
 * Examples:
 *   mergeDrillLogs([1, 3, 5], [2, 4, 6])   -> [1, 2, 3, 4, 5, 6]
 *   mergeDrillLogs([1, 2, 2], [2, 3])      -> [1, 2, 2, 2, 3]
 *   mergeDrillLogs([], [4, 8])             -> [4, 8]
 *   mergeDrillLogs([7], [])                -> [7]
 */

function mergeDrillLogs(a: number[], b: number[]) {
  let i = 0;
  let j = 0;
  const result = [];

  while (i < a.length && j < b.length) {
    if (a[i] <= b[j]) {
      result.push(a[i]);
      i++; // only advance the pointer we consumed
    } else {
      result.push(b[j]);
      j++;
    }
  }
  // one array is now exhausted — append the leftovers from the other
  result.push(...a.slice(i));
  result.push(...b.slice(j));
  return result;
}

// --- test cases ---
console.log(mergeDrillLogs([1, 3, 5], [2, 4, 6]));
console.log(mergeDrillLogs([1, 2, 2], [2, 3]));
console.log(mergeDrillLogs([], [4, 8]));
console.log(mergeDrillLogs([7], []));
