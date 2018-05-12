<?php
/*
  Primes in numbers

  Given a positive number n > 1 find the prime factor decomposition of n.
  The result will be a string with the following form :

    "(p1**n1)(p2**n2)...(pk**nk)"

  with the p(i) in increasing order and n(i) empty if n(i) is 1.

  Example:

    n = 86240 should return "(2**5)(5)(7**2)(11)"

  https://www.codewars.com/kata/primes-in-numbers/php
*/

// My Solution
function primeFactors($n) {
    $str = '';
    $arr = array();
    if ($n < 2) { return $n; }
    while ($n % 2 == 0) {
        $arr[2] = $arr[2] ? $arr[2] + 1 : 1;
        $n /= 2;
    }
    for ($i = 3; $i <= floor(sqrt($n)); $i += 2) {
        while($n % $i == 0) {
            $arr[$i] = $arr[$i] ? $arr[$i] + 1 : 1;
            $n /= $i;
        }
    }
    if ($n > 2) { $arr[$n] = 1; }
    foreach ($arr as $key => $value) {
        $str .= '('.($value > 1 ? ($key.'**'.$value) : $key).')';
    }
    return $str;
}

 ?>
