---
title: Are We Becoming jQuery Developers Instead Of JavaScript Developers?
date: 2013-03-27T00:00:38+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
categories:
  - Culture
  - Programming / Web Development
tags:
  - JavaScript
  - jQuery
---
Recently, a fellow web developer asked me an interesting question: how strong are your JavaScript skills _without_ frameworks like jQuery, YUI, etc.? While I am fairly confident in my JavaScript skills as a whole, it did make me step back and think: because of it&#8217;s prevalence, am I becoming less of a JavaScript developer and more of a jQuery developer? Are jQuery&#8217;s abstractions causing us (as developers) to forget how to work some of the more low-level areas of the language? For example, to stop even propagation in jQuery, you only need to do something like this:

<!--more-->

<pre class="brush: jscript; title: ; notranslate" title="">$('#someElement').on('click', function(e) {
    e.stopPropagation();
});
</pre>

However, because of the different ways IE and other browsers handle events, you&#8217;d need to do some additional checking in vanilla JavaScript:

<pre class="brush: jscript; title: ; notranslate" title="">document.getElementById('someElement').onclick = function(e) {
    e = e || window.event;
    e.cancelBubble = true;

    if (e.stopPropagation !== undefined) {
        e.stopPropagation();
    }
}
</pre>

Now you might be asking what&#8217;s wrong with being dependent on a library that&#8217;s so widely used and saves us so much time? Good question. I see the problem as two fold:

## 1. We Use Many of Its Features Even If It&#8217;s Not the Most Efficient Approach

jQuery provides us with a lot of really cool features, especially when it comes to simplifying how we find and manipulate DOM elements. For example, here&#8217;s how we would usually go about changing the background color of an element:

<pre class="brush: jscript; title: ; notranslate" title="">$('#test').css('background-color', '#000000');
</pre>

Compare this with the vanilla JavaScript approach:

<pre class="brush: jscript; title: ; notranslate" title="">document.getElementById('test').style.backgroundColor = "#000000";
</pre>

It&#8217;s not nearly as compact or flexible. However, if you run a <a href="http://jsperf.com/style-versus-jquery-css/14" target="_blank">speed comparison</a> against the vanilla JavaScript implementation, the vanilla version wins by a longshot.

## 2. It&#8217;s Prevalence Makes it Difficult to Get a Straight Answer on Q&A Sites / Forums

If were to go to a popular Q&A site like <a href="http://www.stackoverflow.com" target="_blank">Stack Overflow</a> and ask a question like _How do I attach an event listener to a DOM element in JavaScript?_, there&#8217;s a pretty good chance that one or more or perhaps all of the answers you&#8217;ll receive will be how to attach an event listener using jQuery. It&#8217;s almost as if jQuery&#8217;s prominence in web development has caused it to become synonymous with the very language it&#8217;s written in.

Now, I&#8217;m not saying that jQuery itself is causing the content of web forums and help sites to become one-sided or go down hill. What I am saying is that the shift towards jQuery-oriented answers from basic JavaScript answers is causing a loss (or at least a muddying) of resources regarding how JavaScript works. It makes it difficult for new developers to get started with the language and for veteran developers to diagnose problems and create new solutions.

## A Challenge: Go Without (For Just a Bit)

In the end, what I&#8217;m suggesting is that you take the time to relearn and rediscover JavaScript without jQuery. Write a dropdown menu, create a form with some validation, bind some events to some elements the old-fashioned way. Take the time to experience some of the pain-points that jQuery helps us navigate around if only so you can understand them better.

## What Do You Think

I&#8217;d love to hear another developer&#8217;s opinion on this. Are we becoming to dependent on jQuery (and other libraries / frameworks)? Leave a comment below.