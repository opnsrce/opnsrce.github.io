---
id: 296
title: 'Code Snippet: How to Sort An Array of JSON Objects By Property'
date: 2013-05-27T00:00:14+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=296
permalink: /code-snippet-how-to-sort-an-array-of-json-objects-by-property/
icy_video_embed_code:
  - 
dsq_thread_id:
  - 4586109770
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - JavaScript
  - JSON
  - sort
---
While working on another project, I ran into a situation where I needed to sort an array of JSON objects. Now, for those of you who may be new to JavaScript, the `array.sort` method allows you to pass in a custom sort function that is meant to look something like this:

<!--more-->

<pre class="brush: jscript; title: ; notranslate" title="">array.sort(function (a, b) {
    var sortStatus = 0;

    if (a &lt; b) {
        sortStatus = -1;
    } else if (a &gt; b) {
            sortStatus = 1;
    }

    return sortStatus;
});
</pre>

Basically, the function takes in two values (`a` and `b`), compares them, and then returns the appropriate numeric code. Given the nature of JSON objects, this basic approach won&#8217;t work. We could, however, create a function for each property we want to sort by. For example, let&#8217;s say we wanted to sort by the `firstName` property:

<pre class="brush: jscript; title: ; notranslate" title="">function sortByFirstName(a, b) {
    var sortStatus = 0;

    if (a.firstName &lt; b.firstName) {
        sortStatus = -1;
    } else if (a.firstName &gt; b.firstName) {
            sortStatus = 1;
    }
    return sortStatus;
}

array.sort(sortByFirstName);
</pre>

Now, while this approach works just fine, it doesn&#8217;t really scale. If each of the JSON objects being sorted has dozens of properties, you would need to create dozens of methods. However, there is a better approach:

<pre class="brush: jscript; title: ; notranslate" title="">function sortByProperty(property) {
    'use strict';
    return function (a, b) {
        var sortStatus = 0;
        if (a[property] &lt; b[property]) {
            sortStatus = -1;
        } else if (a[property] &gt; b[property]) {
            sortStatus = 1;
        }

        return sortStatus;
    };
}

array.sort(sortByProperty('firstName'));
</pre>

Here we&#8217;re using the `sortByProperty` method to dynamically generate the sorting method we saw earlier. This way, you can use a single method to sort any the array against any property you want.