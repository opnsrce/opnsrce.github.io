---
id: 375
title: Using Handlebars Templates With Backbone and Browserify
date: 2014-12-20T21:33:51+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=375
permalink: /using-handlebars-templates-with-backbone-and-browserify/
icy_video_embed_code:
  - 
dsq_thread_id:
  - 4586109216
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - Backbone.js
  - browserify
  - handlebars
---
While working on a recent [side-project](https://github.com/opnsrce/mycv/), I ran into some trouble implementing Handlebars templates for my use in my backbone views when using Browserify for my dependency management. If you&#8217;ve run into similar issues, here&#8217;s a quick breakdown of what you&#8217;ll need to do to get up and running again:

## 1. Install Hbsfy

In order to precompile the templates for use in your app, you&#8217;ll need to install `hbsfy` and include it in your gulpfile. For the record, I have no idea what the hell that&#8217;s supposed to stand for but I like to imagine it being short for &#8220;Handlebars Sci-Fi&#8221; but spelled in the same way as the terrible TV network. Here&#8217;s a snippet from my gulpfile for you to use as a starting point.

<pre class="brush: jscript; title: ; notranslate" title="">var gulp,
        browserify,
        del,
        gulp,
        hbsfy,
        sass,
        source,
        sourcemaps;

    gulp = require('gulp'); // Include gulp

    // Include our plugins
    browserify      = require('browserify');
    del             = require('del');
    hbsfy           = require("hbsfy"); // &lt;---- THIS RIGHT HERE
    sass            = require('gulp-sass');
    source          = require('vinyl-source-stream');
    sourcemaps      = require('gulp-sourcemaps');
    //---
...
</pre>

## Apply Hbsfy During the Bundle Process

Once you&#8217;ve included Hbsfy, you&#8217;ll need to apply it as a transformation during the `bundle()` process:

<pre class="brush: jscript; title: ; notranslate" title="">...
    gulp.task('compile', function () {
        var options;

        options = {
            debug: true,
            paths: [
                './node_modules',
                './src/app/'
            ]
        };

        hbsfy.configure({
            extensions: ['hbs']
        });

        browserify('./src/main.js', options)
            .transform(hbsfy)
            .bundle()
            .pipe(source('app.min.js'))
            .pipe(gulp.dest('build/public/assets/js'));
    });
...
</pre>

The one thing to note in the above snippet is the call to `hbsfy.configure` where I am simply telling hbsfy (I seriously want to know what that stands for) that my template files will all end in `.hbs`. You can substitute in whatever file format you&#8217;re using for your templates.

## 3. Include the Template in the Same File As Your Backbone View

Once you&#8217;ve got your gruntfile configured properly, you can safely start using Handlebars templates in your Backbone views&#8230;almost. You still need to include them. It&#8217;s rather straightforward:

<pre class="brush: jscript; title: ; notranslate" title="">(function () {
    'use strict';

    var User,
        Users,
        Handlebars,
        template,
        Backbone;

    Backbone = require('backbone');
    User = require('entities/user');
    Users = require('collections/users');
    Handlebars = require('handlebars');
    template = require('./search-full.hbs'); // &lt;!-- RIGHT HERE
...
</pre>

## 4. Override the Render Method of Your View and Call the Template

<pre class="brush: jscript; title: ; notranslate" title="">...
    module.exports = Backbone.View.extend({
        className: '.form',
        el: '#app',
        events: {
            'keypress .search .field': 'submitSearch'
        },
        initialize: function () {
            this.render();
        },
        render: function () { // &lt;!-- OVERRIDDEN
            this.$el.html(template());
            return this;
        },
...
</pre>

For the record, I&#8217;m not sure if this is _the_ way to do this. However, I tried simply setting the value of the `template` property on the view and it didn&#8217;t work. If you know of a better way, feel free to leave a comment.

## Wrapping Up

Well, I hope this eased someone&#8217;s frustrations out there. If it did or if you know of a better approach to this problem, please let me know in the comments below.