---
id: 228
title: If-Else Logic in Mustache.js (Sort Of)
date: 2013-02-15T00:00:00+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=228
permalink: /if-else-logic-in-mustache-js-sort-of/
icy_video_embed_code:
  - 
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - JavaScript
  - Mustache
  - templating
---
For those of you who may not be familiar with it, [Mustache.js](http://mustache.github.com/) is a logic-less templating engine for JavaScript. What do I mean by &#8220;logic-less&#8221;. Well, simply put, it means that Mustache.js lacks structures common to many programming languages; there&#8217;s no way to do things like for-loops or function calls (as we may be familiar with them) from within a template. The goal behind this lack of structure is to force you to keep your display logic and your view (templates) completely separate. 

<!--more-->

Luckily, if you code your templates properly you can emulate if-else like behavior in your templates using inverted-sections. According to the Mustache documentation, an inverted-section is a section that:

> [M]ay render text once based on the inverse value of the key. That is, they will be rendered if the key doesn&#8217;t exist, is false, or is an empty list. 

What this means is that we can use sections to print a value _if_ it&#8217;s filled in, _else_ we use an inverted-section to print a value if that value is not filled in:

<pre class="brush: jscript; title: ; notranslate" title="">&lt;script id="channelTpl" type="text/html"&gt;
{{#channels}}
&lt;li&gt;
    &lt;img src = "http://placehold.it/80x80"&gt;
    {{#name}} {{! This is our IF }}
    &lt;span&gt;{{name}}&lt;/span&gt;
    {{/name}}
    
    {{^name}} {{! This is our ELSE }}
    &lt;span&gt;[No Name Provided]&lt;/span&gt;
    {{/name}}
&lt;/li&gt;
{{/channels}}
&lt;/script&gt;
</pre>

Here we&#8217;re saying that if the `{{name}}` of our channel is empty, you&#8217;ll see &#8220;[No Name Provided]&#8221; in the rendered template.