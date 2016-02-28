---
title: 5 Questions to Ask Yourself When Using Recursion
date: 2014-12-15T22:06:13+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
categories:
  - Programming / Web Development
  - Uncategorized
tags:
  - concepts
  - recursion
---

[1]: http://codecademy.com
[2]: https://gist.github.com/

Recursion can be a tough concept to grasp regardless of the language you
decided to program in. In order to help developers who find themselves
struggling with the concept (myself included), I&rsquo;ve broken down the
concept into five simple questions you&rsquo;ll need to answer in order to
write solid recursive functions (inspired by the folks over at [CodeCademy][1]).
<!--more-->

Each of these questions breaks down a simple JavaScript function designed to
find the factoral of a given number:

~~~js
function factoral(n) {
    if(n === 0) {
        return 1;
    }
    if(n < 0) {
        throw "You cannot get the factoral of a negative number";
    }
    return n * factoral(n-1);
}
~~~

# What is/are the base case(s)?

In recursion, a base case can be best defined as scenarios where the function
returns a value without recursing. In the factoral function example, the
base case would be when ``n`` equals ``1``.

# What is/are the recursive case(s)?

A recursive case is a scenario in which the function calls itself (recurses).
In the example function, this occurs whenever ``n`` is greater than ``1``.

# Have I included any other necessary termination condition(s)?

This question is meant to be a sanity check for the developer. Basically, we
want to check and see if there are any other conditions that may cause the
function to terminate or fail that we haven&rsquo;t yet accounted for. In the
factoral example, this extra condition would be the check against a negative
number that throws an exception.

# Do the statements in the function lead to the base case?

When writing a recursive function, you want to make sure that every recursive
call brings you closer and closer to the base case and, therefore, the function
returning a single value. In this example, we&rsquo;re subtracting ``1``
from ``n`` every time we call factoral which leads us closer and closer to our
base case of ``0``.

# Does the recursion build on the base case until the desired result is
returned by the function?

This question can be a little tricky to answer depending on the complexity of
the function you&rsquo;re writing. Basically, we want to make sure that each
call of the function adds to the result of the previous call. In the factoral
example, we&rsquo;re multiplying `n` By the value of its last iteration through
the function.

# Apply the Questions

Now it&rsquo;s your turn to give it a try. I want you to create a [gist][2]
and breakdown a recursive function using the five questions listed above and
post a link to it in the comments. Here&rsquo;s some suggestions for function
ideas:

  1. Recursively print a nested list of items
  2. Find all permutations of a given string
  3. Reverse a string

I look forward to seeing your examples!