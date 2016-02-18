---
id: 365
title: How to Exclude Layout Files When Rendering Templates With Node.js and Express
date: 2014-12-11T21:42:57+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=365
permalink: /how-to-exclude-layout-files-when-rendering-templates-with-node-js-and-express/
icy_video_embed_code:
  - 
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - express
  - handlebars
  - node.js
---
I struggled with this for a good half-hour and I figured I&#8217;d share in case anyone else ran into this issue. Long story short, I needed to return an HTML fragment for a particular ajax request from the app (in this case, search results) but the response always included the layout file I configured for the app:

<pre class="brush: jscript; title: ; notranslate" title="">hbsEngine = expressHbs.create({
        extname: 'hbs',
        defaultLayout: 'layout.hbs',
        helpers: {
            formatDate: function (date, format) {
                return moment(date).format(format);
            }
        }
    });
</pre>

<!--more-->

I&#8217;d found various blog posts mentioning something about setting `layout` to false when rendering the template, but they were never really clear about how to disable the layout _and_ pass data to the template. 

Here&#8217;s how you do just that:

<pre class="brush: jscript; title: ; notranslate" title="">db.collection('users').find({
        firstName: req.query.searchTerm
    }).toArray(function (err, items) {;
        res.render('components/searchResults.hbs', {layout: false, items: items});
    });
</pre>

In the above example, `items` is the property that our template will loop through (via an `{{#each}}{{/each}}`).

Hope this clarifies things!