---
id: 366
title: How to Make Gulp Copy a Directory AND Its Contents
date: 2014-12-12T22:43:06+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=366
permalink: /how-to-make-gulp-copy-a-directory-and-its-contents/
icy_video_embed_code:
  - 
dsq_thread_id:
  - 4586109293
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - Gulp.js
---
I just got done switching one of my [side-projects](http://digitalresume.herokuapp.com/users/54530e03c575dc86d61d22f8) over to [Gulp](http://gulpjs.com/) for the build process and I kept struggling with how to copy multiple folders from the `src` directory to the `build` directory in such a way that the directory&#8217;s contents _and_ its original folder structure are preserved. Basically, I was trying to achieve this:
  
<!--more-->

`</p>
<pre>
src // Copy everything under src
  ->public
    ->pubFile1
    ->pubFile2
  ->vendor
    ->vendorFile1
    ->vendorFile2

build // Destination folder (correct structure)
  ->public
    ->pubFile1
    ->pubFile2
  ->vendor
    ->vendorFile1
    ->vendorFile2  
</pre>
<p>`

But instead I kept getting this:

`</p>
<pre>
build // Destination folder (correct structure)
  ->pubFile1
  ->pubFile2
  ->vendorFile1
  ->vendorFile2  
</pre>
<p>`

Here&#8217;s what I had for my `copy` task in Gulp:

<pre class="brush: jscript; title: ; notranslate" title="">...
    gulp.task('copy', ['clean'], function () {
        return gulp.src(['src/public/**/*', 'src/vendor/**/*'])
          .pipe(gulp.dest('build'));
    });
</pre>

What I needed to set it to was this:

<pre class="brush: jscript; title: ; notranslate" title="">...
    gulp.task('copy', ['clean'], function () {
        return gulp.src(['src/public/**/*', 'src/vendor/**/*'], {
            base: 'src'
        }).pipe(gulp.dest('build'));
    });
</pre>

The `base` config option tells gulp where to start copying _from_. It wouldn&#8217;t matter how many other folders we had put in the path before `src`, gulp would still duplicate all directories that are listed after `src` in the path. If we wanted to copy more directories, we&#8217;d just specify a different base:

<pre class="brush: jscript; title: ; notranslate" title="">...
    gulp.task('copy', ['clean'], function () {
        return gulp.src(['some/other/folders/src/public/**/*', 'some/other/folders/src/vendor/**/*'], {
            base: 'other'
        }).pipe(gulp.dest('build'));
    });
</pre>

The output structure would look something like this:
  
`</p>
<pre>
build
  ->folders
    ->public
      ->pubFile1
      ->pubFile2
    ->vendor
      ->vendorFile1
      ->vendorFile2  
</pre>
<p>`

Hopefully this clears things up!