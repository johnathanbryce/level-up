const containsDuplicates = (nums: number[]): boolean => {
  if (nums.length <= 1) return false;

  const seen = new Set<number>();

  for (const n of nums) {
    // does this number already exist in the hash map? return true if so
    if (seen.has(n)) return true;
    seen.add(n);

    // otherwise, add the number to the seen map
  }

  return false;
};

let nums1 = [1, 2, 3, 1];
let nums2 = [1, 2, 3, 4];
let nums3 = [1, 1, 1, 3, 3, 4, 3, 2];
let emptyArr: number[] = [];

console.log(containsDuplicates(emptyArr));
// console.log(containsDuplicates(nums2));
