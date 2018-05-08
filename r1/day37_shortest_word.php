<?php
/*
  Shortest Word

  Simple, given a string of words, return the length of the shortest word(s).

  String will never be empty and you do not need to account for different data
  types.

  http://www.codewars.com/kata/shortest-word/php
*/

// My Solution
function findShort($str) {
  $words = explode(' ', $str);
  $min = strlen($words[0]);
  foreach($words as $word) {
    if (strlen($word) < $min) {
      $min = strlen($word);
    }
  }
  return $min;
}

// Other Solutions
// function findShort($str){
//    return min(array_map('strlen', (explode(' ', $str))));
// }

 ?>
