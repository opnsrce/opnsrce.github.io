---
title: How to Make Gulp Copy a Directory AND Its Contents
date: 2014-12-12T22:43:06+00:00
author: Levi Hackwith
layout: post
excerpt: 'I just got done switching one of my side-projects over to Gulp for
the build process and I kept struggling with how to copy multiple folders from
the src directory to the build directory in such a way that the
directory&rsquo;s contents and its original folder structure are preserved.'
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - Gulp.js
---

[1]: http://digitalresume.herokuapp.com/users/54530e03c575dc86d61d22f8
[2]: http://gulpjs.com/

I just got done switching one of my [side-projects][1] over to [Gulp][2] for
the build process and I kept struggling with how to copy multiple folders from
the ``src`` directory to the ``build`` directory in such a way that the
directory&rsquo;s contents _and_ its original folder structure are preserved.
Basically, I was trying to achieve this:

~~~
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
~~~

But instead I kept getting this:

~~~
build // Destination folder (correct structure)
  ->pubFile1
  ->pubFile2
  ->vendorFile1
  ->vendorFile2
~~~

Here&rsquo;s what I had for my `copy` task in Gulp:

~~~js
gulp.task('copy', ['clean'], function () {
  return gulp.src(['src/public/**/*', 'src/vendor/**/*'])
    .pipe(gulp.dest('build'));
});
~~~

What I needed to set it to was this:

~~~js
...
gulp.task('copy', ['clean'], function () {
    return gulp.src(['src/public/**/*', 'src/vendor/**/*'], {
        base: 'src'
    }).pipe(gulp.dest('build'));
});
~~~

The ``base`` config option tells gulp where to start copying _from_. It
wouldn&rsquo;t matter how many other folders we had put in the path before
``src``, gulp would still duplicate all directories that are listed after
``src`` in the path. If we wanted to copy more directories, we&rsquo;d just
specify a different base:

~~~js
...
gulp.task('copy', ['clean'], function () {
    return gulp.src([
      'some/other/folders/src/public/**/*',
      'some/other/folders/src/vendor/**/*'
    ], {
        base: 'other'
    }).pipe(gulp.dest('build'));
});
~~~

The output structure would look something like this:

~~~
build
  ->folders
    ->public
      ->pubFile1
      ->pubFile2
    ->vendor
      ->vendorFile1
      ->vendorFile2
~~~

Hopefully this clears things up!