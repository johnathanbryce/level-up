const palindrome = (str: string): boolean => {
  const reversedStr = [...str].reverse().join("");
  return reversedStr === str;
};

// console.log(palindrome("racecar")); // true
// console.log(palindrome("hello")); // false
// console.log(palindrome("a")); // true
// console.log(palindrome("")); // true

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

console.log(palindromeTwoPointer("racecar"));
console.log(palindromeTwoPointer("hello"));
