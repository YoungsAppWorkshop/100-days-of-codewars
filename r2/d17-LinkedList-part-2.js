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

const push = (head, data) => new Node(data, head)
const build = (...args) => args.reduce(push, null)
const buildOneTwoThree = build.bind(null, 3, 2, 1)
const buildThreeTwoOne = build.bind(null, 1, 2, 3)
function Node(data, next = null) {
  this.data = data
  this.next = next
}

function logAllNodes(head) {
  let node = head
  while (node) {
    console.log(node.data)
    node = node.next
  }
}

function sortedInsert(head, data) {
  if(!head || data < head.data) {
    return new Node(data, head)
  } else {
    head.next = sortedInsert(head.next, data)
    return head
  }
}


// let oneTwoThree = buildOneTwoThree()
// logAllNodes(sortedInsert(oneTwoThree, 4.5))


/*
  Linked Lists - Insert Sort

  Write an InsertSort() function which rearranges nodes in a linked list so
  they are sorted in increasing order. You can use the SortedInsert() function
  that you created in the "Linked Lists - Sorted Insert" kata below. The
  InsertSort() function takes the head of a linked list as an argument and must
  return the head of the linked list.

    var list = 4 -> 3 -> 1 -> 2 -> null
    insertSort(list) === 1 -> 2 -> 3 -> 4 -> null

  If the passed in head node is null or a single node, return null or the
  single node, respectively. You can assume that the head node will always be
  either null, a single node, or a linked list consisting of multiple nodes.

  https://www.codewars.com/kata/linked-lists-insert-sort/train/javascript
 */

function insertSort(head) {
  let newHead = null
  let node = head
  while (node) {
    newHead = sortedInsert(newHead, node.data)
    node = node.next
  }
  return newHead
}

// let threeTwoOne = buildThreeTwoOne()
// logAllNodes(insertSort(threeTwoOne))

// Other Solutions
// function insertSort(head) {
//   if (!head) { return null; }
//   return sortedInsert(insertSort(head.next), head.data);
// }
