---
id: 242
title: A Clear Explanation of A Binary Search
date: 2013-02-27T00:00:26+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=242
permalink: /a-clear-explanation-of-a-binary-search/
icy_video_embed_code:
  - 
categories:
  - Programming / Web Development
tags:
  - Algorithms
  - Binary Search
  - Computer Science
---
I&#8217;ll be the first to admit that there are many aspects of computer science that confuse me. One of the things that I was never quite able to grasp (until now) was exactly what a binary search is and how it works. According to <a href="http://en.wikipedia.org/wiki/Binary_search_algorithm" target="_blank">wikipedia</a>, a binary search is an algorithm that:

<!--more-->

> &#8230;finds the position of a specified value (the input &#8220;key&#8221;) within a sorted array.\[1\]\[2\] In each step, the algorithm compares the input key value with the key value of the middle element of the array. If the keys match, then a matching element has been found so its index, or position, is returned. Otherwise, if the sought key is less than the middle element&#8217;s key, then the algorithm repeats its action on the sub-array to the left of the middle element or, if the input key is greater, on the sub-array to the right. If the remaining array to be searched is reduced to zero, then the key cannot be found in the array and a special &#8220;Not found&#8221; indication is returned. 

Makes perfect sense, doesn&#8217;t it? Yeah, I didn&#8217;t get it either. Luckily, that rather complicated definition can be broken down into [3] steps that you can repeat until you find the value you&#8217;re looking for. For this example, we&#8217;re going to use an array of numbers from 1 to 500 and we&#8217;re going to be searching for the number 432.

## 1. Calculate the High and Low Range and Divide In Half

The first piece of data you&#8217;re going to need is the high and low end of your search &#8220;range&#8221;. Given our array of 1 to 500, the high range is 499 (array.length &#8211; 1) and the low range is 1. Next, we&#8217;re going to add the high range and the low range together and divide by 2. This number indicates the first point of the array we&#8217;re going to search from &#8211; half way between the high and low range. In this example, it&#8217;s 500 / 2 or 250.

## 2. Determine if You&#8217;re &#8220;Hot&#8221; or &#8220;Cold&#8221;

Now that we have our first search index figured out (250), we need to determine if we&#8217;re &#8220;hot&#8221; or &#8220;cold&#8221;. That is, if our search index is too high (hot) or too low (cold). In this example, we&#8217;re at 250 and we&#8217;re searching for 432 so our search is currently cold. With all this in mind, we can come to the following conclusions:

  * The key we are searching for cannot exist below 251 (our lowest known search point + 1).
  * The key we are searching for could exist at as high as 500.

If our search was hot instead of cold our conclusions would be:

  * The key we are searching for cannot exist above 249 (our highest known search point &#8211; 1).
  * The key we are searching for could exist at as low as 1.

With this in mind, it&#8217;s time to move on to step 3.

## 3. Recalculate the High and Low Range

We know now that the position we&#8217;re searching for can&#8217;t be below 251 so we can safely assume that our new low is 251 and that our high is still 500. With this new information, we proceed back to Step 1 and cycle through each of the steps again until the search range is reduced to one number: the index of the value we are searching for.

## A complete example

Now that we&#8217;ve covered the necessary steps, let&#8217;s step through a complete example.

<pre class="brush: plain; title: ; notranslate" title="">Target: 432
Range: 1 to 499

----------------------------------------
Iteration 1:
    1. Calculate search index:
         - Search index: (1 + 499) / 2 = 250
    2. Determine "Hot" or "Cold":
         - 250 &lt; 432 = "Cold"
    3. Recalculate High and Low Range
         - Low: 251 (Search Index + 1)
         - High 500
----------------------------------------

----------------------------------------
Iteration 2:
    1. Calculate search index:
         - Search index: (251 + 500) / 2 = 376
    2. Determine "Hot" or "Cold":
         - 376 &lt; 432 = "Cold"
    3. Recalculate High and Low Range
         - Low: 377 (Search Index + 1)
         - High 500
----------------------------------------

----------------------------------------
Iteration 3:
    1. Calculate search index:
         - Search index: (377 + 500) / 2 = 439 (Rounded Up)
    2. Determine "Hot" or "Cold":
         - 439 &gt; 432 = "Hot"
    3. Recalculate High and Low Range
         - Low: 377
         - High 438 (Search Index - 1)
----------------------------------------

----------------------------------------
Iteration 4:
    1. Calculate search index:
         - Search index: (377 + 438) / 2 = 408 (Rounded Up)
    2. Determine "Hot" or "Cold":
         - 408 &lt; 432 = "Cold"
    3. Recalculate High and Low Range
         - Low: 409 (Search Index + 1)
         - High 438
----------------------------------------

----------------------------------------
Iteration 5:
    1. Calculate search index:
         - Search index: (409 + 438) / 2 = 424 (Rounded Up)
    2. Determine "Hot" or "Cold":
         - 424 &lt; 432 = "Cold"
    3. Recalculate High and Low Range
         - Low: 425 (Search Index + 1)
         - High 438
----------------------------------------

----------------------------------------
Iteration 6:
    1. Calculate search index:
         - Search index: (425 + 438) / 2 = 432 (Rounded Up)
    2. Determine "Hot" or "Cold":
         - 432 = 432 = "Match"
    3. Since there's a match, return 432 (the search index where we found the matching value)
----------------------------------------
</pre>

## Things to Keep In Mind

There are three things that, if you forget to do them, can screw up your binary search:

  1. You forget to subtract one from the length of the array when establishing your initial high range
  2. You forget to add 1 to your low range if you are &#8220;cold&#8221; or you forget to subtract one from your high range if you are &#8220;hot&#8221;.
  3. You forget to round up when calculating your search index ( (high + low) / 2).

## Scrutiny Requested

This is really my first foray into the world of algorithms. I don&#8217;t claim to be an expert or even competent in the material I&#8217;ve covered here. That being said, if I&#8217;m wrong or I&#8217;ve stated something unclearly or incorrectly, please let me know in the comments. I really want to get better at this stuff.