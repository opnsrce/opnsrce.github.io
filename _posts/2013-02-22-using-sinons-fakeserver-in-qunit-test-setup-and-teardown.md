---
title: 'Using Sinon&#8217;s FakeServer in QUnit test Setup and Teardown'
date: 2013-02-22T00:00:40+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
dsq_thread_id:
  - 4586110066
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - Christian Johansen
  - QUnit
  - sinon.js
  - unit testing
---
I&#8217;ve recently begun switching from Buster.js to QUnit for my [GitJs](https://github.com/opnsrce/gitjs) project and I discovered a roadblock when it came to using Sinon&#8217;s `FakeServer` in QUnit&#8217;s `setup` and `teardown` methods in a module. According to a <a href="http://cjohansen.no/en/javascript/using_sinon_js_with_qunit" target="_blank">blog post on Christian Johansen&#8217;s website</a>, to use the `fakeServer` object you do something like this:

<!--more-->

<pre class="brush: jscript; title: ; notranslate" title="">test("should make request", function () {
    var server = this.sandbox.useFakeServer();
    var dataSource = new XHRDataSource();
    dataSource.get();

    equal(1, server.requests.length);
});
</pre>

You instantiate the `fakeServer` object using `this.sandbox.useFakeServer`. This totally works for an individual test. But what if you wanted to use the same `fakeServer` instance across all your tests in a module? Well, you&#8217;d think you&#8217;d just do this:

<pre class="brush: jscript; title: ; notranslate" title="">module('My Test Module', {
    setup: function() {
        this.server = this.sandbox.useFakeServer();
    },
    teardown: function() {
        this.server.restore();

        delete this.server;
    }
});

test("should make request", function () {
    var dataSource = new XHRDataSource();
    dataSource.get();

    equal(1, this.server.requests.length);
});
</pre>

But when you run this you&#8217;ll get an error message about not being able to call `useFakeServer` because `sandbox` is undefined. After doing a little digging, I figured out that you actually need to reference the `sinon` object directly in order to use `fakeServer` in `setup` and `teardown`:

<pre class="brush: jscript; title: ; notranslate" title="">module('My Test Module', {
    setup: function() {
        this.server = sinon.fakeServer.create();
    },
    teardown: function() {
        this.server.restore();

        delete this.server;
    }
});

test("should make request", function () {
    var dataSource = new XHRDataSource();
    dataSource.get();

    equal(1, this.server.requests.length);
});
</pre>

By calling `sinon.fakeServer.create()` and storing the instance as a property of `this`, you&#8217;ll be able to reference it in every test in a module without having to redeclare it.