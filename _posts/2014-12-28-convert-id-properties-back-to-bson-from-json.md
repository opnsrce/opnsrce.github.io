---
id: 380
title: Convert ID Properties Back to BSON from JSON
date: 2014-12-28T22:58:02+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=380
permalink: /convert-id-properties-back-to-bson-from-json/
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - Backbone.js
  - BSON
  - JSON
  - mongoDB
---

[1]: http://www.mongodb.org/
[2]: http://bsonspec.org/

Recently, I started using Backbone with [MongoDB][1] to build an app. As I
started integrating an &ldquo;edit&rdquo; feature I ran into a rather vexing
problem: my `$oid` fields kept getting converted to strings whenever I updated
a document. This caused all manor of havoc with my queries: Data wasn&rsquo;t
getting returned properly, results sets were empty, pages crashed because of
``null`` values, etc. Unfortunately, after doing a bunch of research, the best
advice I found related to modifying `toJSON` and `parse` methods to convert
ID fields back to their original values when posting. This really wasn&rsquo;t
an option for me since I had a number of nested documents in my data
structure that also had ``$oid`` fields that needed to be converted.
<!--more-->
For example:

~~~js
..
"workHistory" : [{
    "description" : "",
    "endDate" : null,
    "name" : "SomeCompany",
    "skills" : [{
        "_id" : ObjectId("549b29c970b452eeb6acecd4"),
        "name" : "CSS",
        "description" : ""
    }]
}]
~~~

I needed a way to check a document for potentional `$oid` fields and convert
them back to their correct [BSON][2] values. Here&rsquo;s what I came up with:

~~~js
var parseIds = function(obj) {
    var objProperties;

    objProperties = Object.keys(obj);
    if (_.isObject(obj) === true) {
        objProperties.map(function(value, index, list) {
            if (value.charAt(0) === "_") {
                obj[value] = mongo.helper.toObjectID(obj[value]);
            } else if (_.isObject(obj[value]) === true) {
                parseIds(obj[value]);
            }
        });
    }

};
~~~

In the ``parseIds`` function, we&rsquo;re looping through all the properties
of the passed in object and looking any property whose name started with an
underscore (this is an arbitrary naming convention for ID fields that I came
up with). If it finds one, it converts the value and updates the object in
place.

Hopefully, someone else finds this useful. If anybody knows of a better way
to handle this, please let me know in the comments.