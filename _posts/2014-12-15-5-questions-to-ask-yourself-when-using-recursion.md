---
id: 369
title: 5 Questions to Ask Yourself When Using Recursion
date: 2014-12-15T22:06:13+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=369
permalink: /5-questions-to-ask-yourself-when-using-recursion/
icy_video_embed_code:
  - 
categories:
  - Programming / Web Development
  - Uncategorized
tags:
  - concepts
  - recursion
---
Recursion can be a tough concept to grasp regardless of the language you decided to program in. In order to help developers who find themselves struggling with the concept (myself included), I&#8217;ve broken down the concept into five simple questions you&#8217;ll need to answer in order to write solid recursive functions (inspired by the folks over at [CodeCademy](http://codecademy.com)).
  
<!--more-->

Each of these questions breaks down a simple JavaScript function designed to find the factoral of a given number:

<pre class="brush: jscript; title: ; notranslate" title="">function factoral(n) {
    if(n === 0) {
        return 1;
    }
    if(n &lt; 0) {
        throw "You cannot get the factoral of a negative number";
    }
    return n * factoral(n-1);
}
</pre>

## What is/are the base case(s)?

In recursion, a base case can be best defined as scenarios where the function returns a value without recursing. In the factoral function example, the base case would be when `n` equals `1`.

## What is/are the recursive case(s)?

A recursive case is a scenario in which the function calls itself (recurses). In the example function, this occurs whenever `n` is greater than `1`.

## Have I included any other necessary termination condition(s)?

This question is meant to be a sanity check for the developer. Basically, we want to check and see if there are any other conditions that may cause the function to terminate or fail that we haven&#8217;t yet accounted for. In the factoral example, this extra condition would be the check against a negative number that throws an exception.

## Do the statements in the function lead to the base case?

When writing a recursive function, you want to make sure that every recursive call brings you closer and closer to the base case and, therefore, the function returning a single value. In this example, we&#8217;re subtracting `1` from `n` every time we call factoral which leads us closer and closer to our base case of ``.

## Does the recursion build on the base case until the desired result is returned by the function?

This question can be a little tricky to answer depending on the complexity of the function you&#8217;re writing. Basically, we want to make sure that each call of the function adds to the result of the previous call. In the factoral example, we&#8217;re multiplying `n` By the value of its last iteration through the function.

## Apply the Questions

Now it&#8217;s your turn to give it a try. I want you to create a [gist](https://gist.github.com/) and breakdown a recursive function using the five questions listed above and post a link to it in the comments. Here&#8217;s some suggestions for function ideas:

  1. Recursively print a nested list of items
  2. Find all permutations of a given string
  3. Reverse a string

I look forward to seeing your examples!

Photo Credit: [Jordan Smith](https://www.flickr.com/photos/jordanrandallsmith/8282731636/in/photolist-dBVaxS-3iTXv9-5e3LXD-7BrLZS-6hKmk-aoiYsk-57pvzs-5X5Mao-ariTEb-pFR3J-4zXfNb-5kj7it-Vqhx7-5Fq1ca-57EMe-6Q6XD-75uv2e-8KWr1F-dji1xb-G1JHJ-56zMVR-cZH4-2p6isf-9uUyBX-8E4yaz-adWjLG-n18U7-4bXwFB-4AP5vd-5DhnHH-5hJcXt-3e7L-3vpr5-97Kq7c-eoEZW-4iwW7-5VMpMv-zZ6u1-asoecs-4T2Av-6ncKFV-64JP-8t4iis-4PCYJJ-3nyGS2-6Urgtr-98g64G-5FuiA7-4odKBh-9a8ovq)