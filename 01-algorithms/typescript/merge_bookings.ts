/*
 * Warm-up — 2026-06-10 (JS logic, not the type system)
 *
 * A room-booking system stores reservations as [start, end] pairs on a 24h
 * clock (integers, start < end). Some bookings overlap or touch. Write
 * mergeBookings(bookings) that returns a new list of non-overlapping bookings,
 * merging any that overlap OR touch at an edge.
 *
 * Examples:
 *   mergeBookings([[9, 11], [10, 12], [14, 15]])
 *     -> [[9, 12], [14, 15]]          // [9,11] and [10,12] overlap -> [9,12]
 *
 *   mergeBookings([[1, 3], [3, 5]])
 *     -> [[1, 5]]                      // touching at 3 counts as mergeable
 *
 *   mergeBookings([[5, 6], [1, 2]])
 *     -> [[1, 2], [5, 6]]             // input not sorted; output is sorted
 *
 *   mergeBookings([])  -> []
 *   mergeBookings([[8, 9]]) -> [[8, 9]]
 *
 * Notes:
 *   - input is NOT guaranteed sorted
 *   - "touching" (prev end === next start) merges into one booking
 *   - return a new array; don't mutate the input
 */

function mergeBookings(bookings: number[][]): number[][] {
  const sortedBookings = [...bookings].sort((a, b) => a[0] - b[0]);

  const result: any[] = [];
  for (const booking of sortedBookings) {
    const lastEntry = result[result.length - 1];

    if (result.length === 0 || booking[0] > lastEntry[1]) {
      result.push([...booking]);
    } else {
      lastEntry[1] = Math.max(booking[1], lastEntry[1]);
    }
  }

  return result;
}

// ---- test harness (don't edit) ----
function check(actual: number[][], expected: number[][]) {
  const ok = JSON.stringify(actual) === JSON.stringify(expected);
  console.log(`${ok ? "PASS" : "FAIL"}: got ${JSON.stringify(actual)}`);
  if (!ok) console.log(`      expected: ${JSON.stringify(expected)}`);
}

check(
  mergeBookings([
    [9, 11],
    [10, 12],
    [14, 15],
  ]),
  [
    [9, 12],
    [14, 15],
  ],
);
check(
  mergeBookings([
    [1, 3],
    [3, 5],
  ]),
  [[1, 5]],
);
check(
  mergeBookings([
    [5, 6],
    [1, 2],
  ]),
  [
    [1, 2],
    [5, 6],
  ],
);
check(mergeBookings([]), []);
check(mergeBookings([[8, 9]]), [[8, 9]]);
check(
  mergeBookings([
    [1, 4],
    [2, 3],
  ]),
  [[1, 4]],
); // fully contained
