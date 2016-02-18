---
id: 187
title: 'Helpful Tools for Web Developers: Sprite Cow'
date: 2013-01-18T00:00:31+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=187
permalink: /helpful-tools-for-web-developers-sprite-cow/
icy_video_embed_code:
  - 
categories:
  - Programming / Web Development
  - Tools
tags:
  - CSS
  - sprite
  - Sprite Cow
---
If you&#8217;ve been doing web development for as long as I have, you&#8217;ve no doubt had to deal with CSS sprites. For those of you who may not know, a CSS sprite is simply one big image with a bunch of little images inside of it. By combining multiple images together into a single image, say of a web application&#8217;s icon set, you end up reducing the amount of HTTP requests sent to the server and decreasing page load times. While all of this is great stuff, there is one difficulty when it comes to working with sprites that I don&#8217;t feel gets enough attention: splitting them back out into individual images.

<!--more-->

You see, to display an individual image on a sprite sheet, you need to use the `background-position` in CSS:

<pre class="brush: css; title: ; notranslate" title="">.sprite {
    background: url('imgs/example.png') no-repeat 34px 28px;
    width: 33px;
    height: 33px;
}
</pre>

The `34px 28px` in the above code centers the background image `34px` from the left of the `example.png` image and `28px` from the top and restricts the image to a `33px` by `33px` square. As you can see, calculating the position of an individual icon is not the easiest thing in the world. Most of the time, it boils down to a lot of math and trial-and-error. Luckily, tools like <a href="http://www.spritecow.com/" target="_blank">Sprite Cow</a> make this job a whole lot easier. With Sprite Cow, all you have to do is upload the sprite you want to use, specify the background color of the sprite you uploaded (this makes it easier for Sprite cow to identify individual icons), and then select the icon you want to show. Sprite cow automatically calculates the width, height, and background position needed to show _only_ that icon and outputs the CSS you should use.

I absolutely love Sprite Cow and I use it constantly; it&#8217;s saved me _hours_ of development time. I highly recommend it to anyone who&#8217;s fed up with constantly tweaking their CSS in order to get their CSS sprites working right. You can check it out <a href="http://www.spritecow.com" target="_blank">here</a> or <a href="http://twitter.com/SpriteCow" target="_blank">follow them on Twitter</a>.