/*
  Linked Lists - Push & BuildOneTwoThree

  Write push() and buildOneTwoThree() functions to easily update and initialize
  linked lists. Try to use the push() function within your buildOneTwoThree()
  function.

  Here's an example of push() usage:

    var chained = null
    chained = push(chained, 3)
    chained = push(chained, 2)
    chained = push(chained, 1)
    push(chained, 8) === 8 -> 1 -> 2 -> 3 -> null

  The push function accepts head and data parameters, where head is either a
  node object or null/None/nil. Your push implementation should be able to
  create a new linked list/node when head is null/None/nil.

  The buildOneTwoThree function should create and return a linked list with
  three nodes: 1 -> 2 -> 3 -> null



  https://www.codewars.com/kata/linked-lists-push-and-buildonetwothree/train/javascript
**/

function Node(data) {
  this.data = data
  this.next = null
}

function push(head, data) {
  const newNode = new Node(data)
  newNode.next = head

  return newNode
}

function buildOneTwoThree() {
  let chained = null
  chained = push(chained, 3)
  chained = push(chained, 2)
  chained = push(chained, 1)

  return chained
}


// Other Solutions
// var push = (head, data) => new Node(data, head);
// var build = (...args) => args.reduce(push, null);
// var buildOneTwoThree = build.bind(null, 3, 2, 1);
// var Node = (data, next = null) => ( {data, next} );



/*
  Linked Lists - Length & Count

  Implement Length() to count the number of nodes in a linked list.

    length(null) => 0
    length(1 -> 2 -> 3 -> null) => 3

  Implement Count() to count the occurrences of an integer in a linked list.

    count(null, 1) => 0
    count(1 -> 2 -> 3 -> null, 1) => 1
    count(1 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> null, 2) => 4

  I've decided to bundle these two functions within the same Kata since they
  are both very similar.

  The push()/Push() and buildOneTwoThree()/BuildOneTwoThree() functions do not
  need to be redefined.


  https://www.codewars.com/kata/linked-lists-length-and-count/train/javascript
**/

function length(head) {
  let count = 0
  while (head) {
    count++
    head = head.next
  }
  return count
}

function count(head, data) {
  let count = 0
  while (head) {
    if (head.data === data) count++
    head = head.next
  }
  return count
}

// Other Solutions
// function length(head) {
//   return head ? 1 + length(head.next) : 0
// }
//
// function count(head, data) {
//   if (!head) return 0
//   return (head.data === data ? 1 : 0) + count(head.next, data)
// }




/*
  Linked Lists - Get Nth

  Implement a GetNth() function that takes a linked list and an integer index
  and returns the node stored at the Nth index position. GetNth() uses the C
  numbering convention that the first node is index 0, the second is index 1,
  ... and so on. So for the list 42 -> 13 -> 666, GetNth() with index 1 should
  return Node(13)

    getNth(1 -> 2 -> 3 -> null, 0).data === 1
    getNth(1 -> 2 -> 3 -> null, 1).data === 2

  The index should be in the range [0..length-1]. If it is not, GetNth() should
  throw/raise an exception (ArgumentException in C#, InvalidArgumentException
  in PHP). You should also raise an exception (ArgumentException in C#,
  InvalidArgumentException in PHP) if the list is empty/null/None.


  https://www.codewars.com/kata/linked-lists-get-nth-node/train/javascript
**/


function getNth(node, index) {
  let count = 0
  while (node) {
    if (count === index) return node
    count++
    node = node.next
  }
  throw "Error"
}



/*
  Linked Lists - Insert Nth Node

  Implement an InsertNth() function (insert_nth() in PHP) which can insert a
  new node at any index within a list.

  InsertNth() is a more general version of the Push() function that we
  implemented in the first kata listed below. Given a list, an index 'n' in
  the range 0..length, and a data element, add a new node to the list so that
  it has the given index. InsertNth() should return the head of the list.

    insertNth(1 -> 2 -> 3 -> null, 0, 7) === 7 -> 1 -> 2 -> 3 -> null)
    insertNth(1 -> 2 -> 3 -> null, 1, 7) === 1 -> 7 -> 2 -> 3 -> null)
    insertNth(1 -> 2 -> 3 -> null, 3, 7) === 1 -> 2 -> 3 -> 7 -> null)

  You must throw/raise an exception (ArgumentOutOfRangeException in C#,
  InvalidArgumentException in PHP) if the index is too large.

  The push() and buildOneTwoThree() (build_one_two_three() in PHP) functions
  do not need to be redefined. The Node class is also preloaded for you in PHP.


  https://www.codewars.com/kata/linked-lists-insert-nth-node/train/javascript
**/


function insertNth(head, index, data) {
  let node = head, prev = null, count = 0

  if (!head && index === 0) return new Node(data)

  while (node) {
    if (count === index) {
      const newNode = new Node(node.data)
      newNode.next = node.next
      node.data = data
      node.next = newNode
      return head
    }
    count++
    prev = node
    node = node.next
  }

  if (count === index) {
    node = new Node(data)
    prev.next = node
    return head
  }
  throw "Error"

}

// Other Solutions
// function insertNth(head, index, data) {
//   if(index == 0) return new Node(data, head);
//   if(head && index > 0) {
//     head.next = insertNth(head.next, index - 1, data);
//     return head;
//   }
//   throw "Error";
// }


/*
  Linked Lists - Sorted Insert

  Write a SortedInsert() function which inserts a node into the correct
  location of a pre-sorted linked list which is sorted in ascending order.
  SortedInsert takes the head of a linked list and data used to create a
  node as arguments. SortedInsert() should also return the head of the list.

    sortedInsert(1 -> 2 -> 3 -> null, 4) === 1 -> 2 -> 3 -> 4 -> null)
    sortedInsert(1 -> 7 -> 8 -> null, 5) === 1 -> 5 -> 7 -> 8 -> null)
    sortedInsert(3 -> 5 -> 9 -> null, 7) === 3 -> 5 -> 7 -> 9 -> null)

  The push() and buildOneTwoThree() functions do not need to be redefined.


  https://www.codewars.com/kata/linked-lists-sorted-insert/train/javascript
**/


function sortedInsert(head, data) {

}
