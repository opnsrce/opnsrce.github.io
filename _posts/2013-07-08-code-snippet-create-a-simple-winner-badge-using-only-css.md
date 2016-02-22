---
id: 312
title: 'Code Snippet: Create a Simple &#8220;Winner&#8221; Badge Using only CSS'
date: 2013-07-08T00:00:07+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=312
permalink: /code-snippet-create-a-simple-winner-badge-using-only-css/
icy_video_embed_code:
  -
dsq_thread_id:
  - 4586109542
categories:
  - Uncategorized
---
Today I&#8217;m just going to share with you something I made over the weekend: a really simple &#8220;winner&#8221; badge using only CSS3.

First, the Markup:

<pre class="brush: xml; title: ; notranslate" title="">...
&lt;div class = "badge"&gt;
    &lt;div id = "content"&gt;Winner&lt;/div&gt;
&lt;/div&gt;
...
</pre>
<!--more-->

And the CSS:

<pre class="brush: css; title: ; notranslate" title="">@font-face {
    font-family: 'AirstreamRegular';
    src: url('../fonts/Airstream/airstream.eot');
    src: url('../fonts/Airstream/airstream.eot') format('embedded-opentype'),
         url('../fonts/Airstream/airstream.woff') format('woff'),
         url('../fonts/Airstream/airstream.ttf') format('truetype'),
         url('../fonts/Airstream/airstream.svg#AirstreamRegular') format('svg');
}

.badge {
    background: rgb(35%, 22%, 12%);
    width: 180px;
    height: 180px;
    left: 150px;
    top: 75px;
    position: relative;
    text-align: center;
    border-radius: 30px;
}
.badge:before, .badge:after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    background: inherit;
    border-radius: inherit;
}
.badge:before {
    -webkit-transform: rotate(30deg);
       -moz-transform: rotate(30deg);
        -ms-transform: rotate(30deg);
         -o-transform: rotate(30deg);
}
.badge:after {
    -webkit-transform: rotate(60deg);
       -moz-transform: rotate(60deg);
        -ms-transform: rotate(60deg);
         -o-transform: rotate(60deg);
}
#content {
    position: relative;
    z-index: 1;
    text-align: center;
    line-height: 180px;
    font-family: 'AirstreamRegular';
    border-radius: 360px;
    background-color: white;
    box-sizing: border-box;
    width: 180px;
    height: 180px;
    font-size: 3.5em;
    color: rgb(35%, 22%, 12%);
    top: 0;
    left: 0;
    background: rgba(224, 214, 187, 1);
}
</pre>

The end result is what you saw at the beginning of the post.

A special thanks to [Alan Johnson](http://commondream.net/post/8848553728/pure-css-badges) for coming up with the original 12-point burst CSS I modified to make this happen.