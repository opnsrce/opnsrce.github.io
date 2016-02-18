---
id: 363
title: How to Parse Responses From the StackExchange API Using Node.js
date: 2014-12-08T18:13:01+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=363
permalink: /how-to-parse-responses-from-the-stackexchange-api-using-node-js/
icy_video_embed_code:
  - 
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - API
  - node.js
  - stackexchange
---
Currently, I&#8217;m working on a small side project that involves parsing the wiki entries for given tags on <a class="zem_slink" href="http://www.stackoverflow.com" title="Stack Overflow" rel="homepage" target="_blank">StackOverflow</a>. Without going into a ton of boring detail, the task I was trying to complete can be broken down thusly:

  1. Make a request for the wiki entries of one or more tags from the SE API.
  2. Show that data in a Handlebars template
  3. Profit

<!--more-->

When I first started tackling this problem, I assumed you consume the API just like any other: using AJAX or the `request` node package. However, when I started making requests of the API, I kept getting back binary data instead of the JSON I was expecting. After reviewing the API&#8217;s documentation, I learned that <a class="zem_slink" href="http://stackexchange.com/" title="Stack Exchange Network" rel="homepage" target="_blank">StackExchange</a> sends back data [compressed](https://api.stackexchange.com/docs/compression) via either gzip or deflate (depending on the headers sent with the request). 

What these means is that you&#8217;ll need to decompress the response before you&#8217;ll be able to parse it as JSON and use it in your template. I had to do a bunch of digging to figure out the most effective way to do this and here&#8217;s what I came up with:

<pre class="brush: jscript; title: ; notranslate" title="">...
        var requestOptions,
            req;

        requestOptions = {
            url: 'http://api.stackexchange.com/2.2/tags/javascript/wikis?site=stackoverflow'
        };

        req = request(requestOptions);
        req.on('response', function (wikiRequest) {
            var wiki,
                a,
                i,
                buffer,
                gunzip;

            if (wikiRequest.statusCode === 200) {
                buffer = [];
                gunzip = zlib.createGunzip();

                wikiRequest.pipe(gunzip);

                gunzip.on('data', function (data) {
                    // decompression chunk ready, add it to the buffer
                    buffer.push(data.toString());

                }).on("end", function () {
                    // response and decompression complete, join the buffer and return
                    wiki = JSON.parse(buffer.join(''));
                    // wiki now contains JSON data of API response
...
</pre>

In order to use this example, you&#8217;ll need to make sure you&#8217;ve included the `request` and `zlib` modules (zlib is already installed with node and request can be installed via `npm install request`).

Hopefully, this saves somebody some time and frustration out there. If it does or if you know of a better approach, feel free to let me know.