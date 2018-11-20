/**
  Simple Fun #159: Middle Permutation

  You are given a string s. Every letter in s appears once.

  Consider all strings formed by rearranging the letters in s.
  After ordering these strings in dictionary order, return the middle term.
  (If the sequence has a even length n,
   define its middle term to be the (n/2)th term.)

  Example

    For s = "abc", the result should be "bac".
    The permutations in order are:
      "abc", "acb", "bac", "bca", "cab", "cba"
    So, The middle term is "bac".

  Input/Output
    [input] string s
            unique letters (2 <= length <= 26)

    [output] a string
             middle permutation.

  https://www.codewars.com/kata/58ad317d1541651a740000c5/train/javascript
**/

const getFactorial = n => {
  if (n === 1) return 1
  return n * getFactorial(n - 1)
}

const divide = (dividend, divisor) => (
  [ Math.floor(dividend / divisor), dividend % divisor ]
)

const middlePermutation = s => {
  let arr = []
  let chars = s.split('').sort()
  let order = 0
  let dividend = getFactorial(s.length) / 2

  for (let i = s.length - 1; i > 0; i--) {
    [order, dividend] = divide(dividend, getFactorial(i))

    if (!dividend) {
      arr.push(chars[order - 1])
      chars.splice(order - 1, 1)
      arr = arr.concat(chars.reverse())
      chars = []
      console.log(arr);
      break
    }

    arr.push(chars[order])
    chars.splice(order, 1)
    console.log(i, order, dividend, getFactorial(i), chars, arr)
  }
  if (chars[0]) arr.push(chars[0])
  console.log(arr.join(''));
  return arr.join('')
}



// middlePermutation("abc")
// middlePermutation("abcd")
// middlePermutation("abcdx")
// middlePermutation("abcdxg")
middlePermutation("fqyljwgkrpsxuzndhctoebmvi")
