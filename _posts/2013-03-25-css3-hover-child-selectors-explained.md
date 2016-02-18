---
id: 253
title: 'CSS3 :Hover > Child Selectors Explained'
date: 2013-03-25T00:00:37+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=253
permalink: /css3-hover-child-selectors-explained/
icy_video_embed_code:
  - 
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - CSS
---
Recently, I spent some time reading over pure CSS implementations of a dropdown menu and I was having a hard time grasping the implementation (sad, I know). The HTML made sense (it&#8217;s usually a series of nested lists), but the CSS was never very well explained. The confusing part usually looked something like this:

<pre class="brush: css; title: ; notranslate" title="">ol &gt; li:hover &gt; ol {
    position: absolute;
    /* Other styles here */
}
</pre>

What this translate to is _When I hover over a list item that is part of an ordered list, find an ordered list that is a direct child of that list item and apply the following styles to it._ I know for a lot of you the CSS above is pretty straight forward. For me, it took a while for the concept to click. Maybe this post will help it click for someone else.