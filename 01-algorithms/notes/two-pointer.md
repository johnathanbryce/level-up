# Two Pointer Mental Modal

- a "pointer" here is **just an index variable**
- when we say "two pointers" we mean: _I am tracking two positions in the array/string at once, and moving them according to some rule_

There are two flavors:

1. **opposite direction**: one pointer starts at the left, one at the right, they walk toward each other until they meed in the middle
   - e.g. string palindrome
2. **same direction**: both start at the left pos, one walks faster than the other
   - e.g. move zeros to end of arr


e.g. using palindrome opposite direction:

```ts
const palindromeTwoPointer = (str: string): boolean => {
  let left = 0;
  let right = str.length - 1;

  while (left < right) {
    // compare str[left] and str[right]
    if (str[left] !== str[right]) return false;
    // otherwise move inward
    left++;
    right--;
  }

  return true;
};
```
