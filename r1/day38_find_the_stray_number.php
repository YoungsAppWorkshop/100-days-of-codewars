<?php
/*
  Find the stray number

  You are given an odd-length array of integers, in which all of them are
  the same, except for one single number.

  Complete the method which accepts such an array, and returns that single
  different number.

  The input array will always be valid! (odd-length >= 3)

  Examples
    [1, 1, 2] ==> 2
    [17, 17, 3, 17, 17, 17, 17] ==> 3

  https://www.codewars.com/kata/find-the-stray-number/php
*/

// My Solution
function stray($arr) {
  $same = $arr[0] == $arr[1] ? $arr[0] : ($arr[0] == $arr[2] ? $arr[0] : $arr[1]);
  foreach($arr as $num) {
    if ($num != $same) { return $num; }
  }
}

// Other Solutions
// function stray(array $arr) {
//   return array_search(1, array_count_values($arr));
// }

 ?>
