---
title: How to Include HTML Entities in CSS Content Property
date: 2013-02-06T00:00:40+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
categories:
  - Code Snippets
  - Programming / Web Development
  - Tools
tags:
  - CSS
  - Entity Conversion Calculator
  - special characters
---
Recently, I ran into a situation where I was asked to modify a couple of pagination buttons so that the left and right arrows were replaced with the &laquo; and &raquo; symbols. Now, I won&#8217;t go into a ton of background details, but let&#8217;s just say that modifying the source code of the page wasn&#8217;t the best approach in terms of maintainability. Instead I decided to use the `content` property in CSS to add the symbols on the fly.

If you&#8217;re not familiar with the `content` property, it allows you to insert content either before or after an element:

<pre class="brush: css; title: ; notranslate" title="">img:before {
    content: 'This will be before the image ';
}

img:after {
    'This will be after the image';
}
</pre>

If you drop that into a webpage, it will put the phrase &#8220;This will before the image&#8221; and &#8220;This will be after the image&#8221; before and after every image, respectively. Now, this is all pretty straight forward stuff if you want to put simple text before or after an element, but what about special characters? Well, you&#8217;d think you&#8217;d be able to do something like this:

<pre class="brush: css; title: ; notranslate" title="">img:before {
    content: '&laquo;'
}

img:after {
    '&raquo';
}
</pre>

Unfortunately, instead of displaying the appropriate symbols on the page, the string literals of &#8220;&laquo;&#8221; and &#8220;&raquo;&#8221; get displayed. To get around this, you need to use the hex values of the html entities. How do you get the hex values of the entity you&#8217;re trying to include? Well, you could always <a href="http://stackoverflow.com/a/5786516/122164" target="_blank">roll your own</a> entity conversion script or you could just paste the character into the <a href="http://www.evotech.net/articles/testjsentities.html" target="_blank">Entity Conversion Calculator</a>. Once you figure out the appropriate hex values, all you have to do is plugin them into your CSS:

<pre class="brush: css; title: ; notranslate" title="">img:before {
    content: '&#92;&#48;0AB'
}

img:after {
    '&#92;&#48;0BB';
}
</pre>