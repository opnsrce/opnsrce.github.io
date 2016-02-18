---
id: 190
title: 'Helpful Tools For Web Developers: Duri.me &#8211; Base64 Encode Your Images'
date: 2013-01-23T00:00:27+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=190
permalink: /helpful-tools-for-web-developers-duri-me-base64-encode-your-images/
icy_video_embed_code:
  - 
categories:
  - Programming / Web Development
  - Tools
tags:
  - Base64 Encoding
  - CSS
  - Duri.me
  - images
  - Patrik Larsson
  - Tiago Duarte
---
One of the more recent CSS techniques I&#8217;ve learned is how to base64 encode images and fonts _directly_ into a CSS file. Why would you do something like that? Here&#8217;s a couple of the main benefits of CSS encoding:

<!--more-->

  1. Fewer HTTP Requests: Only the CSS file needs to be requested so there&#8217;s fewer HTTP requests to the server.
  2. If your design includes custom fonts, you can embed the required font files directly in the CSS. This helps guarantee your design will be viewed as intended.

## How to Go About Encoding Images

There&#8217;s two main approaches you can take when it comes to base64 encoding your images: Writing a small script using a backend language like PHP or using a preexisting tool. If you&#8217;re not the programming type, I recommend <a href="http://www.duri.me" target="_blank">Duri.me</a>. It&#8217;s a really simple drag-and-drop tool that not only generates the base64 string, but also gives you the CSS you&#8217;ll need to use on your website (I&#8217;ve truncated the encoded image text for brevity):

<pre class="brush: css; title: ; notranslate" title="">{
    width: 500px;
    height: 628px;
    background-repeat: no-repeat;
    background-image: url(data:image/jpg;base64,/9j/4AAQSkZJRgABAQEASABIAAD//gAuSGF...)
}
</pre>

## Things to Keep in Mind

Per the <a href="http://duri.me/faq.php" target="_blank">FAQ</a>, there are some disadvantages to using Base64 encoded images in your CSS:

  * The size of the embedded code is 1/3 larger than the binary equivalent, however this can be reduced to 2-3% using gzip compression.
  * Internet Explorer 7 is not supported.
  * Internet Explorer 8 limits data URIs to a maximum lenght of 32KB.
  * Data URIs don&#8217;t carry a filename like a normal file,
  * Data URIs need to be re-enconded and re-embedded every time a change is made to the image.

Regardless of whether or not Base64 encoding is the right way to go for your site, I still think that Duri.me is a great tool that is elegantly designed and dead-simple to use. If you want to learn more about its creators, check out <a href="https://twitter.com/LarssonPatrik" target="_blank">Patrik Larson on Twitter</a> as well as <a href="http://tiagoduarte.com/" target="_blank">Tiago Duarte</a>.