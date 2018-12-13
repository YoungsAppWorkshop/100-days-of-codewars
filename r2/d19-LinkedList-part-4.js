/***
  Linked Lists - Move Node

  Write a MoveNode() function which takes the node from the front of the
  source list and moves it to the front of the destintation list. You
  should throw an error when the source list is empty. For simplicity, we
  use a Context object to store and return the state of the two linked
  lists. A Context object containing the two mutated lists should be
  returned by moveNode.

  MoveNode() is a handy utility function to have for later problems.

    var source = 1 -> 2 -> 3 -> null
    var dest = 4 -> 5 -> 6 -> null
    moveNode(source, dest).source === 2 -> 3 -> null
    moveNode(source, dest).dest === 1 -> 4 -> 5 -> 6 -> null

  https://www.codewars.com/kata/linked-lists-move-node/train/javascript
***/

const push = (head, data) => new Node(data, head)
const build = (...args) => args.reduce(push, null)
const buildOneTwoThree = build.bind(null, 3, 2, 1)
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

function Context(source, dest) {
  this.source = source
  this.dest = dest
}

function moveNode(source, dest) {
  if (!source) throw new Error()

  return new Context(source.next, push(dest, source.data))
}


let one = buildOneTwoThree()
let two = buildOneTwoThree()

const a = moveNode(one, two)
logAllNodes(a.source)
console.log();
logAllNodes(a.dest)
