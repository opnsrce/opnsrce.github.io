---
title: Mustache.js Render is Not Defined
date: 2013-02-18T00:00:21+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
dsq_thread_id:
  - 4586111931
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - JavaScript
  - Lessons Learned
  - Mustache
  - templating
---
I ran into the above-mentioned error while trying to learn about lambdas in Mustache. According to the documentation, if your data looks like this:

<pre class="brush: jscript; title: ; notranslate" title="">{
  "name": "Willy",
  "wrapped": function() {
    return function(text) {
      return "&lt;b&gt;" + render(text) + "&lt;/b&gt;"
    }
  }
}
</pre>

<!--more-->



And your template looks like this:

<pre class="brush: xml; title: ; notranslate" title="">{{#wrapped}}
  {{name}} is awesome.
{{/wrapped}}
</pre>

You should get something like this as output:

<pre class="brush: xml; title: ; notranslate" title="">&lt;b&gt;Willy is awesome.&lt;/b&gt;
</pre>

However, when you run this you get something like this in your JS console:

<pre class="brush: jscript; title: ; notranslate" title="">Uncaught ReferenceError: render is not defined
</pre>

This is because the documentation fails to show you where the `render` method is defined. In reality, your data should look like this:

<pre class="brush: jscript; title: ; notranslate" title="">{
  "name": "Willy",
  "wrapped": function() {
    return function(text,render) {
      return "&lt;b&gt;" + render(text) + "&lt;/b&gt;"
    }
  }
}
</pre>

What the documentation forgets to mention is that the `render` method is passed in along with the `text`. Hopefully this helps someone avoid some frustration.