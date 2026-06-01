/**
 * Given two strings `s` and `t`, return true if `t` is an anagram of `s`,
 * false otherwise.
 *
 * An anagram is a word formed by rearranging the letters of another —
 * using all the original characters exactly once.
 *
 * Examples:
 *   s = "listen",  t = "silent"   -> true
 *   s = "rat",     t = "car"      -> false
 *   s = "anagram", t = "nagaram"  -> true
 *
 * Constraints:
 *   - Only lowercase English letters
 *   - 1 <= s.length, t.length <= 5 * 10^4
 *
 * Target: O(n) time, O(1) space (alphabet is bounded → constant space).
 */

function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false;
  // count the numb of individual chars
  const charMap = new Map();
  for (const char of s) {
    charMap.set(char, (charMap.get(char) || 0) + 1);
  }

  for (const char of t) {
    const currCharOppositeStr = charMap.get(char);
    if (!currCharOppositeStr) return false; // if the letter doesn't exist with a count, its not an anagram, return F immediately
    const updatedCharValue = currCharOppositeStr - 1;
    if (updatedCharValue < 0) return false;
    charMap.set(char, updatedCharValue);
  }

  return true;
}

// Test cases
console.log(isAnagram("listen", "silent")); // true
console.log(isAnagram("rat", "car")); // false
console.log(isAnagram("anagram", "nagaram")); // true
console.log(isAnagram("a", "a")); // true   (edge: same single char)
console.log(isAnagram("ab", "abc")); // false  (edge: different lengths)
