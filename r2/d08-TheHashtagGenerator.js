/**
  The Hashtag Generator

  The marketing team is spending way too much time typing in hashtags.
  Let's help them with out own Hashtag Generator!

  Here's the deal:

    - It must start with a hashtag (#).
    - All words must have their first letter capitalized.
    - If the final result is longer than 140 chars it must return false.
    - If the input or the result is an empty string it must return false.

  Examples

    " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
    "    Hello     World   "                  =>  "#HelloWorld"
    ""                                        =>  false

  https://www.codewars.com/kata/52449b062fb80683ec000024/train/javascript
**/

const generateHashtag = str => {
  const result = str.split(' ')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join('')

  return (result.length > 0 && result.length < 140) ?
    '#' + result : false
}



console.log(generateHashtag(" Hello there thanks for trying my Kata"))
console.log(generateHashtag("    Hello     World   "))
console.log(generateHashtag(""))
