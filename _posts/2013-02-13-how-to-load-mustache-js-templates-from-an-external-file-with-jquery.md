---
title: How to Load Mustache.js Templates From an External File with jQuery
date: 2013-02-13T00:00:45+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
dsq_thread_id:
  - 4586112447
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - JavaScript
  - jQuery
  - Mustache
---
Recently, I&#8217;ve been hearing a lot about all the different JavaScript templating libraries out there. Well, I decided to sit down with with Mustache.js and tinker around with it. One of the first stumbling blocks I ran into was figuring out how to load a template that&#8217;s stored in an external file. After doing some digging into a bunch of different blog posts online, I&#8217;ve figured out that it boils down to just a couple of basic steps:

<!--more-->

  1. Dump the template code into an HTML file
  2. Load the template file into your code using jQuery&#8217;s `$.get` method, grab the desired HTML, and render it

## 1. Dump the code into an HTML file

When you declare a mustache template directly into your code, it&#8217;s usually just a simple JavaScript string stored in a variable:

<pre class="brush: jscript; title: ; notranslate" title="">$(document).on('pageinit', function() {
    $.getJSON('assets/data/channels.json', {}, function(channelData, textStatus, jqXHr) {
        var channelList = $('#channels'),
            template;
        // The template var is just a string
        template = '{{#channels}}&lt;li&gt;&lt;img src = "http://placehold.it/80x80"&gt;&lt;span&gt;{{name}}&lt;/span&gt;&lt;/li&gt;{{/channels}}';
        channelList.append(Mustache.to_html(template, channelData))
        channelList.listview("refresh");
    });
});
</pre>

Here we&#8217;re just rending a bunch of music channels into a jQuery mobile list view. And all of this works fine, but the template is not very easy to maintain. Now we&#8217;ll move in into an external HTML file:

<pre class="brush: xml; title: ; notranslate" title="">&lt;!--
[channelList.mustache.html]
This is the template for items in the channel list for when the app first loads
--&gt;
&lt;script id="channelTpl" type="text/html"&gt;
{{#channels}}
&lt;li&gt;
    &lt;img src = "http://placehold.it/80x80"&gt;
    &lt;span&gt;{{name}}&lt;/span&gt;
&lt;/li&gt;
{{/channels}}
&lt;/script&gt;
</pre>

Side Note: The .mustache in the file name doesn&#8217;t do anything. I just put it there in case I wanted to use the same code with a different templating engine.

You&#8217;ll notice that everything is pretty much the same from our first example except that we&#8217;ve wrapped our code in `` tags and given that tag an ID of `channelTpl`. This will come in handy later when we load in the template via the `$.get` method.

## 2. Load the template file into your code using jQuery&#8217;s `$.get` method, grab the desired HTML, and render it

Okay, now that we&#8217;ve got our external file set up, we need to modify our code to pull in the file:

<pre class="brush: jscript; title: ; notranslate" title="">$(document).on('pageinit', function() {
    $.getJSON('assets/data/channels.json', {}, function(channelData, textStatus, jqXHr) {
        var channelList = $('#channels');

        $.get('assets/templates/channelList.mustache.html', function(template, textStatus, jqXhr) {
            channelList.append(Mustache.render($(template).filter('#channelTpl').html(), channelData))
            channelList.listview("refresh");
        });
    });
});
</pre>

As you can see, we&#8217;re pulling in the template file in using $.get. The callback for that method receives a variable called `template` which contains all the code stored in the file. However, Mustache doesn&#8217;t like stuff like `` tags in its templates so we use jQuery to filter down through the template to where we can return just the HTML we want to render. Here, we&#8217;re asking for everything _inside_ the script tags. Also notice how in the previous example we called `Mustache.to_html` where this time we&#8217;re calling `Mustache.render`. This is because we are no longer passing in a raw JavaScript string value so we don&#8217;t need to convert it to HTML before rendering it.

## Final Thoughts

Well, I hope this helps someone out. Please keep in mind that this is my first attempt at really doing _anything_ with Mustache.js and JavaScript templates in general. If I&#8217;ve done something wrong or you know of a better way to accomplish what we&#8217;ve talked about here, please let me know in the comments below.