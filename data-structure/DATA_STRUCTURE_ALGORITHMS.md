# Data Structure & Algorithms


## Efficiency

* Algorithmic efficiency
  - In computer science, algorithmic efficiency is a property of an algorithm which relates to the number of computational resources used by the algorithm. An algorithm must be analyzed to determine its resource usage, and the efficiency of an algorithm can be measured based on usage of different resources. Algorithmic efficiency can be thought of as analogous to engineering productivity for a repeating or continuous process.
  - For maximum efficiency we wish to minimize resource usage. However, different resources such as time and space complexity cannot be compared directly, so which of two algorithms is considered to be more efficient often depends on which measure of efficiency is considered most important.


* Big O Notation
  - In computer science, big O notation is used to classify algorithms according to how their running time or space requirements grow as the input size grows.
  - [Big O Cheat Sheat](http://bigocheatsheet.com/)
  - ex) O(n), O(log(n)), O(n^3), O(1) = O(0n + 1)


* Approximation
  - Some number of computations must be performed for EACH letter in the input


* Example: O(3n + 2) -> O(n)
```
function decode(input):
    create output string
    for each letter in input
        get new_letter from letters location in cipher
        add new_letter to output
    return output
```



## List-Based Collections

* Arrays
  - value, index
  - It's difficult to insert/delete in the middle of array.


* Linked Lists
  - value, reference


* Stacks
* Queues
