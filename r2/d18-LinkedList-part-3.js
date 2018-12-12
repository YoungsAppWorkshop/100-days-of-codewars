/*
  Linked Lists - Append

  Write an Append() function which appends one linked list to another. The
  head of the resulting list should be returned.

    var listA = 1 -> 2 -> 3 -> null
    var listB = 4 -> 5 -> 6 -> null
    append(listA, listB) === 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null

  If both listA and listB are null/NULL/None/nil, return null/NULL/None/nil.
  If one list is null/NULL/None/nil and the other is not, simply return the
  non-null/NULL/None/nil list.

  The push() and buildOneTwoThree() (build_one_two_three() in PHP and ruby)
  functions need not be redefined. The Node class is also predefined for you
  in PHP.

  https://www.codewars.com/kata/linked-lists-append/train/javascript
 */


const push = (head, data) => new Node(data, head)
const build = (...args) => args.reduce(push, null)
const buildOneTwoThree = build.bind(null, 3, 3, 2, 1)
const buildFourFiveSix = build.bind(null, 6, 5, 4)
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

let oneTwoThree = buildOneTwoThree()
let fourFiveSix = buildFourFiveSix()

function append(listA, listB) {
  let node = listA
  if (node) {
    while (node.next) {
      node = node.next
    }
    node.next = listB
    return listA
  } else {
    return listB
  }
}

// Other Solutions
// function append(a, b) {
//   if(!a) return b
//   a.next = append(a.next, b)
//   return a
// }


// logAllNodes(oneTwoThree)
// logAllNodes(fourFiveSix)
// append(oneTwoThree, fourFiveSix)


/*
  Linked Lists - Remove Duplicates

  Write a RemoveDuplicates() function which takes a list sorted in increasing
  order and deletes any duplicate nodes from the list. Ideally, the list should
  only be traversed once. The head of the resulting list should be returned.

    var list = 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 -> null
    removeDuplicates(list) === 1 -> 2 -> 3 -> 4 -> 5 -> null

  If the passed in list is null/None/nil, simply return null.

  Note: Your solution is expected to work on long lists. Recursive solutions
  may fail due to stack size limitations.

  The push() and buildOneTwoThree() functions need not be redefined.

  https://www.codewars.com/kata/linked-lists-remove-duplicates/train/javascript
*/


function removeDuplicates(head) {
  let node = head
  if (!node) return null

  while (node && node.next) {
    while (node.next && (node.data === node.next.data)) {
      node.next = node.next.next
    }
    node = node.next
  }
  return head
}

// Other Solutions
// function removeDuplicates(head) {
//   for (var node = head; node != null; node = node.next) {
//     while (node.next && node.data == node.next.data) {
//       node.next = node.next.next
//     }
//   }
//   return head
// }

console.log(removeDuplicates(buildOneTwoThree()));
