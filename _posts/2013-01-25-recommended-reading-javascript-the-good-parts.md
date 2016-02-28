---
title: 'Recommended Reading: JavaScript: The Good Parts'
date: 2013-01-25T00:00:57+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
categories:
  - Books
  - Programming / Web Development
tags:
  - Douglas Crockford
  - JavaScript
---
Let&#8217;s be honest, as we gain more experience as JavaScript developers we often pick up bad programming habits along the way. For some, that could be loading up our scripts with global variables. For others, it&#8217;s declaring objects and arrays with the &#8220;new&#8221; keyword instead of their literal counterparts. Whatever the problem may be, Douglas Crockford&#8217;s book <cite>JavaScript: The Good Parts</cite> attempts to help the reader break those bad habits by diving deep into the JavaScript language and giving an in-depth look at some of the best (and worst) ways to go about developing in JavaScript. One of the most interesting sections (at least for me) covers exactly why the `new` operator should not be used when declaring things like arrays or objects:

<!--more-->

> JavaScript&#8217;s new operator creates a new object that inherits from the operand&#8217;s prototype member, and then calls the operand, binding the new object to this. This gives the operand (which had better be a constructor function) a chance to customize the new object before it is returned to the requestor. If you forget to use the new operator, you instead get an ordinary function call, and this is bound to the global object instead of to a new object. That means that your function will be clobbering global variables when it attempts to initialize the new members. That is a very bad thing. There is no compile-time warning. There is no runtime warning.

<cite>Crockford, Douglas (2008-12-17). JavaScript: The Good Parts: The Good Parts (Kindle Locations 2947-2953). OReilly Media &#8211; A. Kindle Edition. </cite>

I&#8217;ll warn you now that this book is pretty technical in terms of the material it covers. It dives into everything from object instantiation to prototypical inheritance and doesn&#8217;t really lighten up. If you&#8217;re looking for a good introduction to the JavaScript language, this book may not be for you. However, if you&#8217;re really seeking an in-depth look at how JavaScript functions as a language and what parts of it you should avoid, you can grab a copy over at <a href="http://www.amazon.com/JavaScript-Good-Parts-Douglas-Crockford/dp/0596517742" target="_blank">Amazon</a>