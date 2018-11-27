/**
  Text align justify

  Your task in this Kata is to emulate text justification in monospace font.
  You will be given a single-lined text and the expected justification width.
  The longest word will never be greater than this width.

  Here are the rules:

  - Use spaces to fill in the gaps between words.
  - Each line should contain as many words as possible.
  - Use '\n' to separate lines.
  - Gap between words can't differ by more than one space.
  - Lines should end with a word not a space.
  - '\n' is not included in the length of a line.
  - Large gaps go first, then smaller ones
      ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
  - Last line should not be justified, use only one space between words.
  - Last line should not contain '\n'
  - Strings with one word do not need gaps ('somelongword\n').

  Example with width=30:

    Lorem  ipsum  dolor  sit amet,
    consectetur  adipiscing  elit.
    Vestibulum    sagittis   dolor
    mauris,  at  elementum  ligula
    tempor  eget.  In quis rhoncus
    nunc,  at  aliquet orci. Fusce
    at   dolor   sit   amet  felis
    suscipit   tristique.   Nam  a
    imperdiet   tellus.  Nulla  eu
    vestibulum    urna.    Vivamus
    tincidunt  suscipit  enim, nec
    ultrices   nisi  volutpat  ac.
    Maecenas   sit   amet  lacinia
    arcu,  non dictum justo. Donec
    sed  quam  vel  risus faucibus
    euismod.  Suspendisse  rhoncus
    rhoncus  felis  at  fermentum.
    Donec lorem magna, ultricies a
    nunc    sit    amet,   blandit
    fringilla  nunc. In vestibulum
    velit    ac    felis   rhoncus
    pellentesque. Mauris at tellus
    enim.  Aliquam eleifend tempus
    dapibus. Pellentesque commodo,
    nisi    sit   amet   hendrerit
    fringilla,   ante  odio  porta
    lacus,   ut   elementum  justo
    nulla et dolor.

  https://www.codewars.com/kata/537e18b6147aa838f600001b/train/javascript
**/


const str = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut maximus, augue fringilla varius luctus, purus lorem mollis purus, ac vulputate diam nibh et diam. Suspendisse eget bibendum justo. Phasellus aliquet, lectus eu tincidunt lacinia, turpis risus ornare mauris, vel venenatis elit tortor non odio. Quisque condimentum sapien in mauris finibus sodales. Integer vel sapien non ante tempor varius eget aliquam odio. Cras commodo quis neque at placerat. Integer dignissim tellus gravida turpis malesuada sodales. Duis aliquet luctus purus, sed elementum mi volutpat id. Ut congue, turpis vel laoreet finibus, est tellus congue massa, in scelerisque sem sapien a nibh. Aenean sem leo, rutrum et sodales non, scelerisque quis arcu. Phasellus sit amet blandit neque, et finibus orci. Aenean viverra urna quis est porta vestibulum. Maecenas maximus feugiat risus, eu tempor lacus tincidunt a. Aliquam non sem non mi dapibus interdum. Phasellus eget neque lorem.'

/**
 * @param {String} str - inital string
 * @param {Number} len - line length
 */
const justify = (str, len) => {
  let words = str.split(' '), lines = [], line = []
  let sum = 0

  for (const word of words) {
    if (line.join(' ').length + word.length + 1 <= len) {
      line.push(word)
    } else {
      lines.push(line)
      line = [ word ]
    }
  }
  lines.push(line)

  for (let i = 0; i < lines.length - 1; i++) {
    let str = ''
    const line = lines[i]
    const gap = len - line.map(word => word.length).reduce((a, c) => a + c, 0)
    let space = Math.floor(gap / (line.length - 1)), adjust = gap % (line.length - 1)

    for (let j = 0; j < line.length - 1; j++) {
      str += line[j] + ' '.repeat(space + (adjust > 0 ? 1 : 0))
      adjust--
    }

    str += line[line.length - 1]
    lines[i] = str
  }

  lines[lines.length - 1] = lines[lines.length - 1].join(' ')

  return lines.join('\n')
};

// TODO: Replace examples and use TDD development by writing your own tests

// These are some CW specific test methods available:
//    Test.expect(boolean, [optional] message)
//    Test.assertEquals(actual, expected, [optional] message)
//    Test.assertSimilar(actual, expected, [optional] message)
//    Test.assertNotEquals(actual, expected, [optional] message)

// NodeJS assert is also automatically required for you.
//    assert(true)
//    assert.strictEqual({a: 1}, {a: 1})
//    assert.deepEqual({a: [{b: 1}]}, {a: [{b: 1}]})

// You can also use Chai (http://chaijs.com/) by requiring it yourself
// var expect = require("chai").expect;
// var assert = require("chai").assert;
// require("chai").should();

// describe("Solution", function() {
//   it("should test for something", function() {
//     Test.assertEquals("actual", "expected", "This is just an example of how you can write your own TDD tests");
//   });
// });

justify(str, 30)
