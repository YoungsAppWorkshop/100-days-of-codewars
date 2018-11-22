/**
  Breadcrumb Generator

  As breadcrumb menùs are quite popular today, I won't digress much on
  explaining them, leaving the wiki link to do all the dirty work in my place.

  What might not be so trivial is instead to get a decent breadcrumb from your
  current url. For this kata, your purpose is to create a function that takes
  a url, strips the first part (labelling it always HOME) and then builds it
  making each element but the last a <a> element linking to the relevant path;
  last has to be a <span> element getting the active class.

  All elements need to be turned to uppercase and separated by a separator,
  given as the second parameter of the function; the last element can terminate
  in some common extension like .html, .htm, .php or .asp; if the name of the
  last element is index.something, you treat it as if it wasn't there, sending
  users automatically to the upper level folder.

  A few examples can be more helpful than thousands of words of explanation,
  so here you have them:

    generateBC("mysite.com/pictures/holidays.html", " : ") == '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>'
    generateBC("www.codewars.com/users/GiacomoSorbi", " / ") == '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>'
    generateBC("www.microsoft.com/docs/index.htm", " * ") == '<a href="/">HOME</a> * <span class="active">DOCS</span>'

  Seems easy enough?

  Well, probably not so much, but we have one last extra rule: if one element
  (other than the root/home) is longer than 30 characters, you have to shorten
  it, acronymizing it (i.e.: taking just the initials of every word); url will
  be always given in the format this-is-an-element-of-the-url and you should
  ignore words in this array while acronymizing:

  ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"];

  a url composed of more words separated by - and equal or less than 30
  characters long needs to be just uppercased with hyphens replaced by spaces.

  Ignore anchors (www.url.com#lameAnchorExample) and parameters
  (www.url.com?codewars=rocks&pippi=rocksToo) when present.

  Examples:

    generateBC("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.htm", " > ") == '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > <span class="active">EXAMPLE</span>'
    generateBC("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + ") == '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>'

  You will always be provided valid url to webpages in common formats, so you
  probably shouldn't bother validating them.

  If you like to test yourself with actual work/interview related kata, please
  also consider this one about building a string filter for Angular.js.

  Special thanks to the colleague that, seeing my code and commenting that I
  worked on that as if it was I was on CodeWars, made me realize that it could
  be indeed a good idea for a kata :)

  https://www.codewars.com/kata/563fbac924106b8bf7000046/train/javascript
**/


const generateBC = (url, separator) => {
  const paths = url.replace(/^https?:\/\//, '').replace(/\/$/, '').split('/')

  const ignore = ['THE', 'OF', 'IN', 'FROM', 'BY', 'WITH', 'AND', 'OR', 'FOR', 'TO', 'AT', 'A']
  let breadcrumb = []
  let uri = ''
  let text = ''

  if( paths[paths.length - 1].match(/^index\./i) ) paths.pop()

  for (let i = 0; i < paths.length; i++) {
    if (i === 0) {
      text = 'HOME'
    } else {
      uri += paths[i]
      text = paths[i].replace(/[\.\?#].+$/g, '').replace(/-/g, ' ').toUpperCase()
      if (text.length > 30) {
        text = text
          .split(' ')
          .map(word => (ignore.indexOf(word) > -1) ? '' : word[0])
          .join('')
      }
    }
    uri += '/'

    if (i < paths.length - 1) {
      breadcrumb.push(`<a href="${uri}">${text}</a>`)
    } else {
      breadcrumb.push(`<span class="active">${text}</span>`)
    }
    // console.log(paths[i], text, uri, breadcrumb[i]);
  }

  // console.log(breadcrumb.join(separator));
  return breadcrumb.join(separator)
}


generateBC("https://www.linkedin.com/in/giacomosorbi", " : ")
// generateBC("mysite.com/pictures", " : ")
// generateBC("mysite.com/pictures/holidays.html", " : ")
// generateBC("www.codewars.com/users/GiacomoSorbi", " / ")
// generateBC("www.microsoft.com/docs/index.htm", " * ")
// generateBC("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.htm", " > ")
// generateBC("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + ")


// &lt;a href="/"&gt;HOME&lt;/a&gt; * &lt;a href="/in/"&gt;IN&lt;/a&gt; * &lt;span class="active"&gt;GIACOMOSORBI&lt;/span&gt;
// &lt;a href="/"&gt;HOME&lt;/a&gt; * &lt;a href="//"&gt;&lt;/a&gt; * &lt;a href="//www.linkedin.com/"&gt;WWW&lt;/a&gt; * &lt;a href="//www.linkedin.com/in/"&gt;IN&lt;/a&gt; * &lt;span class="active"&gt;GIACOMOSORBI&lt;/span&gt;
