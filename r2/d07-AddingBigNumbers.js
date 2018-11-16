/**
  Adding Big Numbers

  We need to sum big numbers and we require your help.

  Write a function that returns the sum of two numbers. The input numbers
  are strings and the function must return a string.

  Example:
    add("123", "321"); -> "444"
    add("11", "99"); -> "110"

  Notes:
    - The input numbers are big.
    - The input is a string of only digits
    - The numbers are positives

  https://www.codewars.com/kata/525f4206b73515bffb000b21/train/javascript
**/

function add(a, b) {
  const len = a.length > b.length ? a.length : b.length
  let result = ""
  let up = 0

  a = a.padStart(len, '0')
  b = b.padStart(len, '0')

  for (var i = len - 1; i >= 0; i--) {
    const sum = Number(a[i]) + Number(b[i]) + up
    up = Math.floor(sum / 10)
    dividend = sum % 10
    result = dividend + result
    // console.log(i, Number(a[i]), Number(b[i]), sum, up, dividend, result)
  }

  return up ? up + result : result
}

// Other Solution
// function add (a, b) {
//   var res = '', c = 0
//   a = a.split('')
//   b = b.split('')
//   while (a.length || b.length || c) {
//     c += ~~a.pop() + ~~b.pop()
//     res = c % 10 + res
//     c = c > 9
//   }
//   return res
// }

add('63829983432984289347293874', '90938498237058927340892374089')
