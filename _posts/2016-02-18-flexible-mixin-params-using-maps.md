---
title: 'Flexible Mixin Params Using Maps'
date: 2016-02-18T00:00:34+00:00
author: Levi Hackwith
layout: post
permalink: /flexible-mixin-params-using-maps/
categories:
  - Programming / Web Development
tags:
  - SASS
  - CSS
  - Mixin
---

[1]: http://sass-lang.com/guide

[Mixins][1] in Sass are great for dynamically generating CSS properties based on
passed in variables. For example, assuming you're working with a twelve column
grid layout, your mixin for generating a column might look something like this:

<!--more-->

~~~sass
@mixin column($num-columns) {
  width: $num-columns / 12;
  padding: 12px; // Add a 12px gutter to the column
}
~~~

This is helpful and all, but what if you wanted to add the ability to not add
a gutter to a specific side of the column? You might do something like this:

~~~sass
@mixin column($num-columns, $top-gutter: true, right-gutter-true, ...) {
  width: $num-columns / 12;
  if($top-gutter == true) {
    padding-top: 12px;
  }
  ...
  // do this conditional for each side
}
~~~

As you can see, the parameter list gets little unweildy and hard to maintain. If
you need to add additional, required parameters to the mixin, you end up having
to pass the default value of ``true`` for _each_ gutter variable. To get around
this, we can use a map.

# Maps to the rescue

Originally introduced in SASS 3.3, maps act similar to objects in other
languages like JavaScript:

~~~sass
@mixin column($num-columns, $gutters:()) {
  width: $num-columns / 12;
  @each $gutter, $bool in $gutters {
    @if($bool == true) {
      padding-#{$gutter}: 12px;
    }
  }
}
~~~

Another way you can use maps in SASS is as a kind of config object:

~~~sass
@mixin column($width, $options:()) {
  ////////////////////////////////////////////////////////////////////////////
  $default-options: (
    // What sides to remove padding from: e.g., collapse: top left
    collapse: none,
    // How many columns-widths from the left a column should start
    push: 0,
    // How many column-widths from the right a column should start
    pull: 0,
    //
    // What direction to force a column to be in. Possible value are: right,
    // center
    //
    force: none
  );

  $options: map-merge($default-options, $options);

  $collapse: map-get($options, 'collapse');
  $collapsible-sides: top bottom left;
  $force: map-get($options, 'force');
  $gutter-width: map-get($grid-config, 'gutter-width');
  $num-columns: map-get($grid-config, 'num-columns');
  $pull: map-get($options, 'pull');
  $push: map-get($options, 'push');
  $push: map-get($options, 'push');
////////////////////////////////////////////////////////////////////////////
~~~

Here, we use the ``map-merge`` method to merge the passed in ``options`` param
with the ``$default-options`` map. This way, we can guarantee the values of
any options not passed in by the user. To retrieve options from the config,
simply call ``map-get``.

## Why Use This Approach Over Optional Params

The main reason you should use maps instead of optional params for you mixins
has more to do with code flexibility and maintainability than anything. You can
easily add new functionality to a mixin without breaking existing consumers of
your code.