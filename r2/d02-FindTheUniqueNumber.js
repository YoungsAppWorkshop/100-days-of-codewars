/*
Find the unique number

  There is an array with some numbers. All numbers are equal except for one.
  Try to find it!

    findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
    findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55

  It’s guaranteed that array contains more than 3 numbers.
  The tests contain some very huge arrays, so think about performance.

  This is the first kata in series:

    Find the unique number (this kata)
    Find the unique string
    Find The Unique

  https://www.codewars.com/kata/find-the-unique-number-1/train/javascript
 */


const sum = arr => arr.reduce((a, c) => a + c, 0)


const findUniq = arr => {
  const len = Math.floor(arr.length / 3)
  const remain = arr.length % 3

  const arr0 = arr.slice(0, len)
  const arr1 = arr.slice(len, len * 2)
  const arr2 = arr.slice(len * 2, arr.length - remain)

  const sum1 = sum(arr0)
  const sum2 = sum(arr1)
  const sum3 = sum(arr2)

  if (sum1 === sum2 && sum1 === sum3) {
    return findUniq(arr.slice(arr.length -3))
  } else if (sum2 === sum3) {
    if (len === 1) {
      return arr0[0]
    } else if (len === 2) {
      arr0.push(arr1[0])
      return findUniq(arr0)
    } else {
      return findUniq(arr0)
    }
  } else if (sum1 === sum3) {
    if (len === 1) {
      return arr1[0]
    } else if (len === 2) {
      arr1.push(arr2[0])
      return findUniq(arr1)
    } else {
      return findUniq(arr1)
    }
  } else {
    if (len === 1) {
      return arr2[0]
    } else if (len === 2) {
      arr2.push(arr0[0])
      return findUniq(arr2)
    } else {
      return findUniq(arr2)
    }
  }
}


/*
  Other Solutions

    function findUniq(arr) {
      arr.sort((a,b)=>a-b);
      return arr[0]==arr[1]?arr.pop():arr[0]
    }

    function findUniq(arr) {
      return arr.find(n => arr.indexOf(n) === arr.lastIndexOf(n));
    }

 */

findUniq([1, 1, 2])
findUniq([2, 1, 1, 1])
findUniq([1, 1, 1, 2])
findUniq([1, 1, 1, 2, 1])
findUniq([1, 1, 1, 1, 2])
findUniq([1, 2, 1, 1, 1])
findUniq([1, 2, 1, 1, 1, 1, 1])
findUniq([1, 1, 1, 1, 2, 1, 1])
