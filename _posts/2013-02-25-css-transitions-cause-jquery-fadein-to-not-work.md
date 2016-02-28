---
title: CSS Transitions Cause jQuery FadeIn() to Not Work
date: 2013-02-25T00:00:04+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
dsq_thread_id:
  - 4586110014
categories:
  - Programming / Web Development
tags:
  - CSS
  - JavaScript
  - jQuery
---
While working on a small side project, I discovered an interesting quirk related to jQuery&#8217;s `fadeIn` method: If the element you&#8217;re trying to fade in has it&#8217;s `transition` property set (it doesn&#8217;t matter what vendor prefix you use), the element will just appear without fading in. Here&#8217;s a quick example:

<!--more-->

This is the CSS I&#8217;m using.

<pre class="brush: css; title: ; notranslate" title="">image { /* Fade in page images */
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
    display: block;
    -webkit-transition: all 1s ease-in-out; /* Transition properties (for each vendor) */
    -moz-transition: all 1s ease-in-out;
    -o-transition: all 1s ease-in-out;
    transition: all 1s ease-in-out;
}
image:hover {
    opacity: .5; /* When you mouse over the image, reduce opacity by 50% */
}
</pre>

And here&#8217;s the JavaScript:

<pre class="brush: jscript; title: ; notranslate" title="">$(document).ready(function() {
    var images = $('img');

    images.hide();

    images.each(function(i) {
        $(this).delay(i * 50).fadeIn(500); // Sequentially fade in each image
    });
});
</pre>

When this is run, the images don&#8217;t fade in but are instead made visible in sequential order (no fading effect). After doing some digging, I discovered that if I removed the transition properties from the CSS and instead applied them dynamically _after_ each image is done fading in, everything worked fine (both the fade-in and the opacity reduction on hover).

The CSS

<pre class="brush: css; title: ; notranslate" title="">image { /* I'm trying to fade in a bunch of images (individually) on the page */
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
    display: block;
}
image:hover {
    opacity: .5 /* When you mouse over the image, reduce opacity by 50% */
}
</pre>

The JavaScript

<pre class="brush: jscript; title: ; notranslate" title="">$(document).ready(function() {
    var images = $('img');

    images.hide();

    images.each(function(i) {
        $(this).delay(i * 50).fadeIn(500, function() {
            $(this).css({
                '-webkit-transition': 'all 1s ease-in-out',
                '-moz-transition': 'all 1s ease-in-out',
                '-o-transition': 'all 1s ease-in-out',
                'transition': 'all 1s ease-in-out',
            });
    });
});
</pre>

Unfortunately, I&#8217;m not exactly certain as to _why_ this problem occurs in jQuery. I&#8217;ve stepped through what jQuery is doing during a fade-in and I don&#8217;t see anything that would conflict with what is in the stylesheet. If anyone else has encountered this problem and happens to know more about what&#8217;s going on, please let me know in the comments below.