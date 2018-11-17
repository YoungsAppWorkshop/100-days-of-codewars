/**
  A maximal subarray

  The input is an array of numbers, e.g. arr = [1, -2, 3, 4, -9, 6].

  The task is: find the contiguous subarray of arr with the maximal sum of items.

  Write the function getMaxSubSum(arr) that will return that sum.

  For instance:

    getMaxSubSum([-1, 2, 3, -9]) = 5 (the sum of highlighted items)
    getMaxSubSum([2, -1, 2, 3, -9]) = 6
    getMaxSubSum([-1, 2, 3, -9, 11]) = 11
    getMaxSubSum([-2, -1, 1, 2]) = 3
    getMaxSubSum([100, -9, 2, -3, 5]) = 100
    getMaxSubSum([1, 2, 3]) = 6 (take all)

  If all items are negative, it means that we take none (the subarray is empty), so the sum is zero:

    getMaxSubSum([-1, -2, -3]) = 0

  Please try to think of a fast solution: O(n2) or even O(n) if you can.
**/

const getMaxSubSum = arr => {
  let sum = 0
  let max = 0
  for (i = 0; i < arr.length; i++) {
    if (sum > max) { max = sum }
    if (arr[i] < 0) {
      if (arr[i-1] && arr[i+1] && (arr[i-1] + arr[i] > 0) && (arr[i] + arr[i+1] >0)) {
        sum = sum + arr[i] + arr[i+1]
      } else if (arr[i+1] && (arr[i+1] > 0)) {
        sum = arr[i+1]
      }
    } else {
      if (!arr[i-1]) {
        sum = arr[i]
      }
      if (arr[i+1] && (arr[i+1] > 0)) {
        sum += arr[i+1]
      }
    }
    // console.log(`i: ${i}\tnum: ${arr[i]}\tsum: ${sum}\tmax: ${max}`);
  }
  return max
}

// Other Solutions
// countBits = n => n.toString(2).split('0').join('').length;

// var countBits = function(n) {
//   return n.toString(2).replace(/0/g,'').length;
// }

console.log(getMaxSubSum([-1, 2, 3, -9]))
console.log(getMaxSubSum([2, -1, 2, 3, -9]))
console.log(getMaxSubSum([-1, 2, 3, -9, 11]))
console.log(getMaxSubSum([-2, -1, 1, 2]))
console.log(getMaxSubSum([100, -9, 2, -3, 5]))
console.log(getMaxSubSum([1, 2, 3]))
