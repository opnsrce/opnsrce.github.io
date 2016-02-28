---
title: How to Quickly Convert a JavaScript Date Object Into a Timestamp
date: 2013-02-11T00:00:37+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - Dates
  - JavaScript
  - tips
---
One of things we often have to do in JavaScript is compare dates to see how much time has passed. To this, you would usually do something like this:

<pre class="brush: jscript; title: ; notranslate" title="">var start,
    stop,
    elapsedMilliseconds;


    start = new Date();
    someProcess();
    stop = new Date();
    elapsedMilliseconds = stop.getTime() - start.getTime();
    document.write(elapsedMilliseconds + " Milliseconds have passed");
</pre>

However, there&#8217;s a simpler way:

<pre class="brush: jscript; title: ; notranslate" title="">var start,
    stop;

    start = +new Date();
    someProcess();
    stop = +new Date();
    document.write(stop-start + " Milliseconds have passed");
</pre>

When you add the plus-sign infront of the `new` operator, the date returned is automatically converted into a timestamp allowing you to quickly assess the amount of milliseconds that have passed.

What other time-saving shortcuts do you know about in JavaScript? Feel free to share them in the comments below.