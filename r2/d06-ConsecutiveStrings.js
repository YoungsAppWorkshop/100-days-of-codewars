/**
  Consecutive strings

  You are given an array strarr of strings and an integer k. Your task is to
  return the first longest string consisting of k consecutive strings taken
  in the array.

  #Example:
    longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2)
     --> "abigailtheta"

  n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

  https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/javascript
**/

function longestConsec(strarr, k) {
  let [i, result] = [0, ""]
  // let result = ""
  while (i + k <= strarr.length && k > 0) {
    const consecutiveStr = strarr.slice(i, i+k).join("")
    if (consecutiveStr.length > result.length) {
      result = consecutiveStr
    }
    i++
  }
  return result
}

console.log(longestConsec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2))
console.log(longestConsec([], 2))
