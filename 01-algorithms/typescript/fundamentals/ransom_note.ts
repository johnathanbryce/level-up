function canConstruct(ransomNote: string, magazine: string): boolean {
  const magazineMap = new Map();

  for (const char of magazine) {
    magazineMap.set(char, (magazineMap.get(char) || 0) + 1);
  }

  for (const char of ransomNote) {
    const count = magazineMap.get(char);
    if (!count) return false;
    magazineMap.set(char, count - 1);
  }

  return true;
}

// Test cases
console.log(canConstruct("a", "b"));        // expected: false
console.log(canConstruct("aa", "ab"));      // expected: false
console.log(canConstruct("aa", "aab"));     // expected: true
console.log(canConstruct("abc", "cbad"));   // expected: true
console.log(canConstruct("", "anything")); // expected: true
