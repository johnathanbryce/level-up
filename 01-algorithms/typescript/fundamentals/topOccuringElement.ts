const topOccuringElements = (nums: number[], k: number): number[] => {
  const numsMap = new Map();
  for (const num of nums) {
    // does num exist in map? increment it
    if (numsMap.has(num)) {
      // it exists, increment it
      let currNumCount = numsMap.get(num) || 0;
      numsMap.set(num, ++currNumCount);
    } else {
      numsMap.set(num, 1);
    }
    // else, add to map
  }

  const topKNums = [...numsMap]
    .sort((a, b) => b[1] - a[1])
    .slice(0, k)
    .map((pair) => pair[0]);

  return topKNums;
};

// Input: ((nums = [1, 1, 1, 2, 2, 3]), (k = 2));
// Output: [1, 2];

// Input: ((nums = [1]), (k = 1));
// Output: [1];

let nums = [1, 1, 1, 2, 2, 3];

topOccuringElements(nums, 2);
