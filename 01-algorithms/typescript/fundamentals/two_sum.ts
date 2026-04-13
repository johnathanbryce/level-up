function twoSumSimple(nums: number[], target: number): number[] {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) return [i, j];
    }
  }
  return [];
}

const nums = [2, 7, 11, 15];
const target = 9;

// console.log(twoSumSimple(nums, target));

function twoSum(nums: number[], target: number): number[] {
  const seen = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const n = nums[i];
    const complement = target - n;

    if (seen.has(complement)) {
      return [seen.get(complement)!, i];
    }

    seen.set(n, i);
  }

  return [];
}

console.log(twoSum(nums, target)); // [0, 1]
console.log(twoSum([3, 2, 4], 6)); // [1, 2]
console.log(twoSum([3, 3], 6)); // [0, 1]
