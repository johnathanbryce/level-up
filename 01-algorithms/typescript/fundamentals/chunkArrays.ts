function chunk(arr: number[], chunks: number) {
  // while loop that goes to chunks
  let chunkedArr = [];
  while (arr.length > 0) {
    let chunk = arr.splice(0, chunks);
    chunkedArr.push(chunk);
  }
  console.log(chunkedArr);
  return chunkedArr;
}

chunk([1, 2, 3, 4, 5], 2);
// → [[1, 2], [3, 4], [5]]

chunk([1, 2, 3, 4, 5, 6], 3);
// → [[1, 2, 3], [4, 5, 6]]

chunk([1, 2, 3], 1);
// → [[1], [2], [3]]

// chunk([1, 2, 3], 10)
// → [[1, 2, 3]]
