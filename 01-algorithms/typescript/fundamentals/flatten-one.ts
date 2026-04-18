type NestedNumber = number | NestedNumber[];

const flattenOne = (numsArr: NestedNumber[]): number[] => {
  let flattenedNumbers: number[] = [];
  // loop over array, if just a number, add to the flattenedNumbers arr
  for (const item of numsArr) {
    if (Array.isArray(item)) {
      // easy approach:
      for (const nested of item) {
        flattenedNumbers.push(nested as number);
      }
    } else {
      flattenedNumbers.push(item);
    }
  }
  console.log(flattenedNumbers);
  return flattenedNumbers;
};

flattenOne([1, [2, 3], 4, [5, [6, 7]]]);
// → [1, 2, 3, 4, 5, [6, 7]]
flattenOne([[], [1], [2, 3]]);
// // → [1, 2, 3]

flattenOne([1, 2, 3]);
// // → [1, 2, 3]
