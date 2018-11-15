/**
  Pascal's Triangle

  Wikipedia article on Pascal's Triangle:
    http://en.wikipedia.org/wiki/Pascal's_triangle

  Write a function that, given a depth (n), returns a single-dimensional
  array/list representing Pascal's Triangle to the n-th level.

  For example:

    pascalsTriangle(4) == [1,1,1,1,2,1,1,3,3,1]

  https://www.codewars.com/kata/5226eb40316b56c8d500030f/train/javascript
**/

// function getPascalsNumber(row, col) {
//   if (row === 0 && col === 0) {
//     return 1
//   } else if (row < 0 || col < 0) {
//     return 0
//   } else {
//     return getPascalsNumber(row - 1, col - 1) + getPascalsNumber(row - 1, col)
//   }
// }
//
// function pascalsTriangle(n) {
//   const arr = []
//   for (let row = 0; row < n; row++) {
//     for (let col = 0; col < row + 1; col++) {
//       arr.push(getPascalsNumber(row, col))
//     }
//   }
//   return arr
// }

function pascalsTriangle(n) {
  const arr0 = []
  for (let r = 0; r < n; r++) {
    const arr1 = []
    for (let c = 0; c <= r; c++) {
      const pascalNumber = arr0[r-1] ? (
        (arr0[r-1][c-1] || 0) + (arr0[r-1][c] || 0)
      ) : 1
      arr1.push(pascalNumber)
    }
    arr0.push(arr1)
  }
  return [].concat.apply([], arr0)
}

// Other Solutions
// function pascalsTriangle(n) {
//   var pascal = [];
//   var idx = 0;
//
//   for ( var i = 0; i < n; i++ ) {
//     idx = pascal.length - i;
//     for ( var j = 0; j < i+1; j++ ) {
//       if ( j === 0 || j === i ) {
//         pascal.push(1);
//       } else {
//         pascal.push( pascal[ idx+j ] + pascal[ idx+j-1 ] );
//       }
//     }
//   }
//
//   return pascal;
// }

console.log(pascalsTriangle(1));
console.log(pascalsTriangle(2));
console.log(pascalsTriangle(3));
console.log(pascalsTriangle(4));
console.log(pascalsTriangle(5));
