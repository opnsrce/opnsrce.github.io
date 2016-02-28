---
title: Chrome Not Autoplaying Video Stream in Canvas
date: 2013-05-29T00:00:34+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
categories:
  - Programming / Web Development
tags:
  - API
  - HTML5
  - JavaScript
---
I was recently tinkering with some <a href="http://davidwalsh.name/demo/camera.php" target="_blank">demo code</a> that <a href="http://davidwalsh.name/browser-camera" target="_blank">David Walsh</a> put together and, after setting up my own demo using the code mentioned in the post, I noticed some odd behavior in Chrome. Whenever you loaded the page and gave Chrome permission to access your webcam, the camera stream would not show up until you triggered a repaint on the page (e.g., resizing the developer toolbar or clicking the &#8220;snap picture&#8221; button). While I don&#8217;t really understand why this is the case, I did figure out a way to fix it:

<!--more-->

<pre class="brush: jscript; title: ; notranslate" title="">video.addEventListener('canplay', function(e) {
    video.style.display = video.style.display;
});
</pre>

Here I&#8217;ve attached an event listener to the `canplay` event of the video element. When the event fires, it sets the value of the display property to whatever it happens to be currently. While this code doesn&#8217;t exactly _do_ anything in and of itself, it _does_ force a `recalculate style` event to fire. This is turn makes the video stream visible.

## Feedback Requested

I&#8217;m sorry I don&#8217;t have any information as to the exactly cause of this issue. If David Walsh or anyone else out there wants to shed some light on the issue, please leave a comment below.