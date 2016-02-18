---
id: 304
title: 'Element.dataset not supported in IE: Here&#8217;s a Workaround'
date: 2013-07-05T00:00:54+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=304
permalink: /element-dataset-not-supported-in-ie-heres-a-workaround/
icy_video_embed_code:
  - 
dsq_thread_id:
  - 4586109684
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - Internet Explorer
  - JavaScript
  - workaround
---
Recently, I was working on a project that used the <a href="https://developer.mozilla.org/en-US/docs/Web/API/element.dataset" target="_blank"><code>dataset</code> property</a> to store some additional info about element and I discovered that none of my code worked in IE. After doing some research, I found out that `dataset` property is not supported by IE (at least not until version 11 comes out). If you&#8217;ve ever run into this issue, here&#8217;s a quick workaround:

<pre class="brush: jscript; title: ; notranslate" title="">var myElement = document.getElementById('myElement'), // contains attribute data-my-custom-value
    myCustomValue;

if(myElement.dataset !== undefined) { // standard approach
    myCustomValue = myElement.dataset.myCustomValue;
} else {
    myCustomValue = myElement.getAttribute('data-my-custom-value'); // IE approach
}
</pre>

In the above example, if the `dataset` property is undefined, we use the `getAttribute` method to grab it instead. The one thing to note here is that when you use `dataset` property to retrieve the value of the `my-custom-value` attribute, the name of the attribute gets converted to camel-case and the &#8220;data&#8221; portion of the name is dropped; when you use `getAttribute` the value is retrieved using the original hyphened value.