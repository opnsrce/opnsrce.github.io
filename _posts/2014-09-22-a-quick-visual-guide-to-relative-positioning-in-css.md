---
title: A Quick Visual Guide to Relative Positioning in CSS
date: 2014-09-22T00:00:34+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
categories:
  - Programming / Web Development
tags:
  - CSS
---
Getting your head around positioning elements in CSS can be very confusing. When I first started doing front-end web development, I would often end up spending hours trying to figure out why one element or another was refusing render where I thought it should. Nine times out of ten, the problem usually had something to do with the surrounding elements and what the value of their `position` attribute happened to be.

In order to help new developers understand how relative positioning works in CSS, I put together a quick visual demonstration:

<p data-height="580" data-theme-id="0" data-slug-hash="bgHAJ" data-default-tab="result" data-user="opnsrce" class='codepen'>
  See the Pen <a href='http://codepen.io/opnsrce/pen/bgHAJ/'>bgHAJ</a> by Levi Hackwith (<a href='http://codepen.io/opnsrce'>@opnsrce</a>) on <a href='http://codepen.io'>CodePen</a>.
</p>



The box labeled &#8220;5&#8221; is absolutely positioned zero pixels from the right side of its parent container (by default, container 4).

When you click on one of the checkboxes, the corresponding container div&#8217;s `position` property gets set to `static` (the default value). If you click on the checkbox labeled &#8220;Disable Level 4&#8221;, you&#8217;ll notice that the &#8220;5&#8221; box jumps from the right of box 4 to the right of box 3. This is because, by setting 4&#8217;s position to `static` instead of relative, you are telling box 5 that 4 is no longer the parent container. Confused? I was too. When we look at the nested nature of HTML, we would assume that the &#8220;parent container&#8221; of an element is the nearest element that contains another element. In our case, the parent of 5 would be 4. However, the browser sees things a little different. It defines a parent element as the nearest element that contains another element _that also has its `position` element set to `relative`_. By changing the `position` attribute of a parent element, you&#8217;re forcing the browser to look for the next nearest element with a relative position. Notice how, if you recheck the checkbox, the 5 box jumps back into place.

Hopefully the clarifies things regarding relative positioning in CSS. If you have any questions or feedback, please leave a comment.

photo credit: [atzu](https://www.flickr.com/photos/atzu/4365152223/) via [photopin](http://photopin.com) [cc](http://creativecommons.org/licenses/by-nc-sa/2.0/)