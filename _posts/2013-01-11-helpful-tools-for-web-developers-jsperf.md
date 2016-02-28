---
title: 'Helpful Tools For Web Developers: JsPerf'
date: 2013-01-11T00:00:06+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
categories:
  - Programming / Web Development
  - Tools
tags:
  - JavaScript
  - jsperf
  - performance
---
When it comes to front-end development, performance tweaking is often a forgotten step. However, as web applications become larger and more and more complex, maintaining and tweaking the performance of your application becomes more important. Unfortunately, this is not as easy as it sounds. How do you know that the code you&#8217;ve refactored is actually more efficient than the original? That&#8217;s where tools like <a href="http://www.jsperf.com" target="_blank">JsPerf</a> come in.

<!--more-->

JsPerfs allows you to compare the efficiency of two pieces of code. Take the following for example:

<pre class="brush: jscript; title: ; notranslate" title="">Array.prototype.loopBackward = function(searchString) {
    var me = this,
    numItems = this.length,
    i, returnArray = [];

    for (i = numItems - 1; i &gt;= 0; i--) {
        returnArray.push(me[i]);
    }
    return returnArray;
}

Array.prototype.loopForward = function(searchString) {
    var me = this,
    numItems = this.length,
    i, returnArray = [];

    for (i = 0; i &lt;= numItems - 1; i++) {
        returnArray.push(me[i]);
    }

    return returnArray;
}
</pre>

Here I&#8217;ve added two methods to the `Array` object: `loopForward` and `loopBackward`. One iterates through an array from 0 to its length and the other goes from its length down to 0.

When I set these tests up in JsPerf, here&#8217;s what I found out:

<a href="http://www.levihackwith.com/?attachment_id=173" rel="attachment wp-att-173"><img class="aligncenter size-full wp-image-173" alt="jsperf-test" src="http://www.levihackwith.com/wp-content/uploads/2013/01/jsperf-test1.png" width="959" height="197" /></a>

Looping through an array backwards is faster than looping through it forwards. With this is mind, if your application has to loop through a lot of large datasets, it would be more efficient for you to loop through them backwards.

Granted this is only a small sampling of the kinds of tests you can run on JsPerf. I highly recommend it for anyone looking for a good comparison tool to use when trying to increase the performance of their web applications.