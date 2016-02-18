---
id: 251
title: 'Code Snippet: CSS Wildcard Selectors'
date: 2013-03-08T00:00:24+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=251
permalink: /code-snippet-css-wildcard-selectors/
icy_video_embed_code:
  - 
dsq_thread_id:
  - 4586109947
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - Attribute
  - CSS
  - wildcard
---
Just a quick CSS code snippet I found helpful the other day. CSS wildCard selectors

## Attribute &#8220;Contains&#8221; Selector

<pre class="brush: css; title: ; notranslate" title="">a[id*=-myElement] {
    color: red;
}
</pre>

The above CSS will find any anchor tag whose `id` attribute contains the text &#8220;-myElement&#8221;. 

## Attribute &#8220;Ends With&#8221; Selector

<pre class="brush: css; title: ; notranslate" title="">a[id$=-myElement] {
    color: red;
}
</pre>

The above CSS will find any anchor tag whose `id` attribute ends with the text &#8220;-myElement&#8221;.

## Attribute &#8220;Begins With&#8221; Selector

<pre class="brush: css; title: ; notranslate" title="">a[id^=-myElement] {
    color: red;
}
</pre>

The above CSS will find any anchor tag whose `id` attribute ends with the text &#8220;-myElement&#8221;.

This is by no means a complete list of attribute selectors. For a full reference, check out [this reference](https://developer.mozilla.org/en-US/docs/CSS/Attribute_selectors) on the Mozilla Developer Network