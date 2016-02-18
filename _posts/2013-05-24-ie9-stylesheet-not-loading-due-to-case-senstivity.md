---
id: 293
title: IE9 Stylesheet Not Loading Due to Case Sensitivity
date: 2013-05-24T00:00:18+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=293
permalink: /ie9-stylesheet-not-loading-due-to-case-senstivity/
icy_video_embed_code:
  - 
categories:
  - Programming / Web Development
tags:
  - CSS
  - Internet Explorer
---
I recently discovered something very dastardly about IE9 (and possibly other versions &#8211; I haven&#8217;t tested them all): class names are case sensitive in IE9. In other words, if your HTML looks something like this:

<pre class="brush: xml; title: ; notranslate" title="">...
&lt;div class = "MyDiv"&gt;&lt;/div&gt;
...
</pre>

And your CSS looks something like this:

<pre class="brush: css; title: ; notranslate" title="">.myDiv {
/* Styles Here */
}
</pre>

<!--more-->

Internet Explorer will not apply the styles to the div because `MyDiv` is not the same as `myDiv`. However, if you were to run this HTML through another browser, the page will render as expected.

Oh, and why the weird post title? Well, it appears that <a href="http://blogs.msdn.com/b/ieinternals/archive/2011/03/27/http-406-not-acceptable-php-ie9-standards-mode-accepts-only-text_2f00_css-for-stylesheets.aspx" target="_blank">IE9 not properly loading stylesheets is a common problem</a>. However, it usually has to do with the mime type of the CSS file and less to do with the problem discussed here. I wanted to draw attention to the main symptom so that someone else who got as frustrated as I did might find the answer sooner.