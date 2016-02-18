---
id: 236
title: Row (Zebra) Striping With Mustache.js Using Counters
date: 2013-02-20T00:00:54+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=236
permalink: /row-zebra-striping-with-mustache-js-using-counters/
icy_video_embed_code:
  - 
dsq_thread_id:
  - 4586111284
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - JavaScript
  - Mustache
  - templating
---
When I started working with Mustache templates, one of the features I felt was lacking was the ability to track what item was currently being processed by the template. Sure, you can always reference the current item via `{{.}}` but there&#8217;s no way to see how many items have been processed; there&#8217;s no counter. This makes it difficult to do things like alternate row colors on a table (a.k.a row or &#8220;zebra&#8221; striping). 

Well, I set about figuring out a way to get around this limitation and here&#8217;s what I came up with. Basically, we&#8217;re setting up a function called `getClass` and storing it as a property of the JSON data we&#8217;re getting back from the server. Each time the function gets called we check the value of `callCounter` which is a property of the `getClass` function (remember, functions are object and can therefore have properties). Each time the function is called, we increment the value of `callCounter`. If the value is odd we return the string &#8216;odd&#8217;; if it is even we return the string &#8216;even&#8217;.

<pre class="brush: jscript; title: ; notranslate" title="">$(document).on('ready', function() {
    $.getJSON('assets/data/channels.json', {}, function(channelData, textStatus, jqXHr) {
        channelData.getClass = function() {
            channelData.getClass.callCounter = channelData.getClass.callCounter || 0;
            channelData.getClass.callCounter++;
            return channelData.getClass.callCounter % 2 == 0 ? 'even' : 'odd';

        }
        $.get('assets/templates/channelList.mustache.html', function(template, textStatus, jqXhr) {
            var channelList = $('#channels tbody');

            channelList.append(Mustache.render($(template).filter('#channelTpl').html(), channelData))
        });
    });
});

</pre>

Your template might end up looking something like this:

<pre class="brush: xml; title: ; notranslate" title="">&lt;script id="channelTpl" type="text/html"&gt;
{{#channels}}
&lt;tr class ="{{getClass}}"&gt;
    &lt;td&gt;{{Name}}&lt;/td&gt;
    &lt;td&gt;&lt;a href ="{{playlist}}"&gt;{{playlist}}&lt;/a&gt;&lt;/td&gt;
&lt;/tr&gt;
{{/channels}}
&lt;/script&gt;
</pre>

Hopefully this helps someone out. If you know of a better way to accomplish this, please let me know in the comments below.