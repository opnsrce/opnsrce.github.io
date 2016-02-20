---
id: 363
title: How to Parse Responses From the StackExchange API Using Node.js
date: 2014-12-08T18:13:01+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=363
permalink: /how-to-parse-responses-from-the-stackexchange-api-using-node-js/
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - API
  - node.js
  - stackexchange
---

[1]: http://www.stackoverflow.com
[2]: http://stackexchange.com/
[3]: https://api.stackexchange.com/docs/compression

Currently, I&rsquo;m working on a small side project that involves parsing the wiki entries for given tags on [StackOverflow][1]. Without going into a ton of boring detail, the task I was trying to complete can be broken down thusly:

  1. Make a request for the wiki entries of one or more tags from the SE API.
  2. Show that data in a Handlebars template
  3. Profit

When I first started tackling this problem, I assumed you consume the API just
like any other: using AJAX or the ``request`` node package. However, when I
started making requests of the API, I kept getting back binary data instead of
the JSON I was expecting. After reviewing the API&rsquo;s documentation, I
learned that [StackExchange][2] sends back data [compressed][3] via either gzip
or deflate (depending on the headers sent with the request).

What these means is that you&rsquo;ll need to decompress the response before
you&rsquo;ll be able to parse it as JSON and use it in your template. I had to
do a bunch of digging to figure out the most effective way to do this and
here&rsquo;s what I came up with:

~~~js
...
var requestOptions;
var req;

requestOptions = {
  url: 'http://api.stackexchange.com/2.2/tags/javascript/wikis?' +
    'site=stackoverflow'
};

req = request(requestOptions);

req.on('response', function (wikiRequest) {
  var wiki;
  var a;
  var i;
  var buffer;
  var gunzip;

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
~~~

In order to use this example, you&rsquo;ll need to make sure you&rsquo;ve
included the ``request`` and ``zlib`` modules (zlib is already installed with
node and request can be installed via ``npm install request``).

Hopefully, this saves somebody some time and frustration out there. If it does
or if you know of a better approach, feel free to let me know.