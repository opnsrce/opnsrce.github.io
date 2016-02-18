---
id: 320
title: JsLint Unexpected Continue Error Explained
date: 2013-11-04T12:00:50+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=320
permalink: /jslint-unexpected-continue-error-explained/
icy_video_embed_code:
  - 
dsq_thread_id:
  - 4586109439
categories:
  - Programming / Web Development
tags:
  - JavaScript
  - JsLint
---
If you&#8217;ve ever had the &#8220;pleasure&#8221; of running your JavaScript code through JSLint, you&#8217;ve probably encounter the following message.

> Unexpected continue

Recently, I encountered this message when checking some code I&#8217;d written. In an attempt to gain some clarity on what the problem was, I checked out the <a href="http://javascript.crockford.com/code.html" target="_blank">JS Lint Documentation</a> which tells me to

> [a]void use of the continue statement. It tends to obscure the control flow of the function.

<!--more-->

While this highlights how `continue` (and `continue`) can reduce code clarity, I still don&#8217;t feel that&#8217;s a very good explanation. If you check out <cite>JavaScript: The Good Parts</cite> Douglas Crockford doesn&#8217;t provide much help either:

> The continue statement jumps to the top of the loop. I have never seen a piece of code that was not improved by refactoring it to remove the continue statement. 

<cite>Crockford, Douglas (2008-12-17). JavaScript: The Good Parts: The Good Parts (Kindle Locations 2861-2864). OReilly Media &#8211; A. Kindle Edition.</cite>

Not exactly helpful (and a little arrogant, if you ask me). After doing some more research, I&#8217;ve discovered that what JsLint (and Crockford, by extension) wants you to do is invert your logic so that the `continue>` statement is no longer needed.

For example this code:

<pre class="brush: jscript; title: ; notranslate" title="">var i = 0,
    names = ['james', 'sally', 'ray',  'charles', 'kevin', 'dan'],
    numNames = names.length;


for(i = 0; i &lt; numNames; i++) {
    if(names === 'sally') {
        continue;
    }
    // process data
}
</pre>

Can be refactored to not use the `continue` statement by inverting the conditional:

<pre class="brush: jscript; title: ; notranslate" title="">var i = 0,
    names = ['james', 'sally', 'ray',  'charles', 'kevin', 'dan'],
    numNames = names.length;


for(i = 0; i &lt; numNames; i++) {
    if(names != 'sally') {
        // process data
    }
}
</pre>

Hopefully, I&#8217;ve provided some clarity regarding JsLint&#8217;s rather cryptic error messages. Is there another message you can&#8217;t seem to wrap your head around or just plain don&#8217;t agree with? Leave a comment below.