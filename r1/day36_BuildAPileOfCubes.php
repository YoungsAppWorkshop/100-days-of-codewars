<?php
/*
  Build a pile of Cubes

  Your task is to construct a building which will be a pile of n cubes.
  The cube at the bottom will have a volume of n^3, the cube above will
  have volume of (n-1)^3 and so on until the top which will have a volume
  of 1^3.

  You are given the total volume m of the building. Being given m can you
  find the number n of cubes you will have to build?

  The parameter of the function findNb (find_nb, find-nb, findNb) will be
  an integer m and you have to return the integer n such as n^3 + (n-1)^3
  + ... + 1^3 = m if such a n exists or -1 if there is no such n.

  Examples:
    findNb(1071225) --> 45
    findNb(91716553919377) --> -1

  https://www.codewars.com/kata/build-a-pile-of-cubes/php
*/

// My Solution
function findNb($m) {
  $i = 1;
  while ( ( $i * ($i + 1) / 2 ) ** 2 < $m ) {
    $i++;
  }
  if (( $i * ($i + 1) / 2 ) ** 2 == $m ) {
    return $i;
  } else {
    return -1;
  }
}

// Other Solutions
// function findNb($m) {
//   $n = 0;
//   while ($m > 0) $m -= ++$n**3;
//   return $m ? -1 : $n;
// }

// function findNb($m) {
//     $n = (sqrt(8 * sqrt($m) + 1) - 1) / 2;
//
//     return $n == (int)$n ? $n : -1;
// }

// Sample Test
// class PileOfCubesCases extends TestCase
// {
//     private function revTest($actual, $expected) {
//         $this->assertEquals($expected, $actual);
//     }
//     public function testBasics() {
//         $this->revTest(findNb(4183059834009), 2022);
//         $this->revTest(findNb(24723578342962), -1);
//         $this->revTest(findNb(135440716410000), 4824);
//     }
// }

 ?>
