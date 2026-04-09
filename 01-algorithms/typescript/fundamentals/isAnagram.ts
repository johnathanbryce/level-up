function isAnagram(str1: string, str2: string): boolean {
  // organize each str into a map with a count of letters

  const strOneMap = new Map<string, number>();
  const strTwoMap = new Map<string, number>();

  for (const c of str1) {
    // if c exists, add +1 to it in the map
    if (strOneMap.has(c)) {
      let currCharCount = strOneMap.get(c);
      currCharCount! += 1;
      strOneMap.set(c, currCharCount!);
    } else {
      // else add to the map
      strOneMap.set(c, 1);
    }
  }

  for (const c of str2) {
    // if c exists, add +1 to it in the map
    if (strTwoMap.has(c)) {
      let currCharCount = strTwoMap.get(c);
      currCharCount! += 1;
      strTwoMap.set(c, currCharCount!);
    } else {
      // else add to the map
      strTwoMap.set(c, 1);
    }
  }

  // if strOneMap === strTwoMap return True else False
  if (strOneMap.size !== strTwoMap.size) return false;

  for (const [key, value] of strOneMap) {
    if (strTwoMap.get(key) !== value) return false;
  }

  return true;
}

// console.log(isAnagram("anagram", "nagaram")); // true
// console.log(isAnagram("rat", "car")); // false
// console.log(isAnagram("aacc", "ccac")); // false
// console.log(isAnagram("a", "ab")); // false

// --- Elegant single-map version ---
function isAnagramSingleMap(str1: string, str2: string): boolean {
  if (str1.length !== str2.length) return false;

  const counts = new Map<string, number>();

  for (const c of str1) {
    counts.set(c, (counts.get(c) || 0) + 1);
  }

  for (const c of str2) {
    const count = counts.get(c);
    if (!count) return false;
    counts.set(c, count - 1);
  }

  return true;
}

console.log("--- single map ---");
console.log(isAnagramSingleMap("anagram", "nagaram")); // true
console.log(isAnagramSingleMap("rat", "car")); // false
console.log(isAnagramSingleMap("aacc", "ccac")); // false
console.log(isAnagramSingleMap("a", "ab")); // false
