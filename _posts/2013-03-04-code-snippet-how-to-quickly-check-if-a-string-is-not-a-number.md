---
id: 246
title: 'Code Snippet: How to Quickly Check if a String is Not a Number'
date: 2013-03-04T00:00:51+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=246
permalink: /code-snippet-how-to-quickly-check-if-a-string-is-not-a-number/
icy_video_embed_code:
  - 
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - Conversion
  - Datatypes
  - isNaN
  - JavaScript
---
Here&#8217;s how to quickly check if a string value is a number or not:

<pre class="brush: jscript; title: ; notranslate" title="">var someString = "This is not a number",
    someNumber = "200";

if(isNaN(+someString) === true) {
    alert(someString + " is not a number");
} else {
    alert(someString + " is a number");
}

if(isNaN(+someNumber) === true) {
    alert(someNumber + " is not a number");
} else {
    alert(someNumber + " is a number");
}
</pre>

Adding a `+` to the front of a string forces JavaScript to try and convert it into a number.