/*
  Find the divisors

    Create a function named divisors/Divisors that takes an integer and
    returns an array with all of the integer's divisors
    (except for 1 and the number itself).

    If the number is prime return the string '(integer) is prime' (null in C#)
    (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

  Example:
    divisors(12); // should return [2,3,4,6]
    divisors(25); // should return [5]
    divisors(13); // should return "13 is prime"

    You can assume that you will only get positive integers as inputs.

  https://www.codewars.com/kata/find-the-divisors/javascript
*/

// My Solution
function divisors(integer) {
  let divs = [];
  for (i = 2; i <= Math.sqrt(integer); i++) {
    if (integer % i == 0) {
      divs.push(i);
    }
  }
  let divs2 = [];
  for (i = divs.length - 1; i >= 0; i--) {
    const num = integer / divs[i];
    if (num !== divs[i]) {
      divs2.push(num);
    }
  }
  return divs.length !== 0 ? divs.concat(divs2) : integer + " is prime";
};
