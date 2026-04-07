function reverseString(str: string): string {
  if (str.length === 1) return str;

  const reverseStr = [...str].reverse().join("");
  return reverseStr;
}

// use without .reverse( )
function reverseStringManual(str: string): string {
  let reverseStr = "";

  const strArr = [...str];

  for (let i = strArr.length - 1; i >= 0; i--) {
    reverseStr += strArr[i];
  }

  console.log(reverseStr);
  return reverseStr;
}

reverseStringManual("hello"); // "olleh"
reverseStringManual("JavaScript"); // "tpircSavaJ"
reverseStringManual("a b c"); // "c b a"
reverseStringManual("x"); // "x"
