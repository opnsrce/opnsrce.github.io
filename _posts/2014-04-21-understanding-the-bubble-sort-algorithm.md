---
id: 342
title: Understanding the Bubble Sort Algorithm
date: 2014-04-21T00:00:06+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=342
permalink: /understanding-the-bubble-sort-algorithm/
icy_video_embed_code:
  - 
dsq_thread_id:
  - 4586109371
categories:
  - Programming / Web Development
---
A while back, we talked about algorithms <a title="A Clear Explanation of A Binary Search" href="http://www.levihackwith.com/a-clear-explanation-of-a-binary-search/" target="_blank">like binary search</a> and explained how it works. Today, we&#8217;re going to do the same thing with a sorting algorithm called bubble sort. While it&#8217;s by far not the most efficient algorithm to use when sorting a list of items, it&#8217;s the simplest one to implement and is a great starting point for those interested in learning more about sorting algorithms in general.

<!--more-->

First: what is the bubble sort algorithm? Wikipedia defines it as:

> &#8230;[A] simple sorting algorithm that works by repeatedly stepping through the list to be sorted, comparing each pair of adjacent items and swapping them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. The algorithm gets its name from the way smaller elements &#8220;bubble&#8221; to the top of the list&#8230;

Basically, bubble sort works by comparing two adjacent values in a list and, if the value on the left is greater than the value on the right (e.g., 2 comes before 1), it swaps the position of those two values. From there it then checks the next two values (swapping values as needed) until it reaches the last value it sorted (to start, this value is set to the index of the last value in the list).

Once the end of the list has been reached, the index of the last value sorted is decreased by one and the sorting process starts again.

Here&#8217;s a visual of how this might look:

![](http://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)

The bolded numbers at the end represent the last value that&#8217;s been sorted. Once the index of the last value sorted equals 1, the algorithm has finished sorting the array.

&nbsp;

## Write a Bubble Sort Function

The next thing we&#8217;ll cover is how you might go about writing a function that uses the bubble sort algorithm to sort an array. Here&#8217;s an example of such a function:

<pre class="brush: jscript; title: ; notranslate" title="">function swap(dataArray, index1, index2) {
    var tmp = dataArray[index1];
    
    dataArray[index1] = dataArray[index2];
    dataArray[index2] = tmp;
    
    return dataArray;
}

function bubbleSort(data) {
    var pointer = 0,
        maxIndexToCheck = data.length - 1;
        
    for(; maxIndexToCheck &gt;= 1; maxIndexToCheck--) {
        for(pointer = 0; (pointer + 1) &lt;= maxIndexToCheck; pointer++) {   
            if(data[pointer] &gt; data[pointer + 1]) {
                data = swap(data, pointer, (pointer + 1));
            }         
        }
    }
    
    return data;
}
</pre>

The `swap` method is just there to swap value arrays, so let&#8217;s take a close look at the `bubbleSort` function. In this function, we first create an outer loop that keeps track of the index of the last value that&#8217;s been sorted. By default, this value is equal to the largest index in the array:

<pre class="brush: jscript; title: ; notranslate" title="">...
    var pointer = 0,
        maxIndexToCheck = data.length - 1;
        
    for(; maxIndexToCheck &gt;= 1; maxIndexToCheck--) {
...
</pre>

Next, we create a loop that will move through pairs of values in the array comparing the left most value to the value next to it. If the value on the left is greater than the value on the right, we swap those two values&#8217; locations in the array:

<pre class="brush: jscript; title: ; notranslate" title="">...
        for(pointer = 0; (pointer + 1) &lt;= maxIndexToCheck; pointer++) {   
            if(data[pointer] &gt; data[pointer + 1]) {
                data = swap(data, pointer, (pointer + 1));
            }         
        }
...
</pre>

Notice how this loop only increments the pointer up to the index of the last value we&#8217;ve sorted. As the value of `maxIndexToCheck` decrements, the number of array values getting checked and swapped drops as well.

Finally, once both loops are complete we return the newly-sorted array.

## A Word of Warning

Despite it&#8217;s ease of use and implementation, the bubble sort algorithm is hardly the best approach to sorting a large amount of data. The worse-case scenario for this algorithm is `O(n<sup>2</sup>)` which means that the most iterations needed to sort the algorithm equals the number of items being sorted squared. We&#8217;ll get into algorithm speed in a later post, but for now just know that there are better algorithms to use besides this one. 

Photo Credit: [Evan Leeson](https://www.flickr.com/photos/ecstaticist/3067907278/in/photolist-5F6PX5-5zMnad-5zx43t-5vAas4-5hkay3-5gq8WN-4GGyfS-4muZzK-4iRtBa-3baHjy-2XCNR3-2wCvrp-2nH7T1-2hwwC5-2gkSwy-2ektuu-R9ziU-Jkf4T-BjtkP-B7566-ABdSL-sFrSx-iWUJ7-cMUCz-6tCSB-5nqAj-3Tk26-eevyN5-cxTCa5-c42Ehh-9a52Ay-7Zbcq9-6r9mfH-6jhVFz-5NNVLa-dXziJS-d4QcPo-8HyYww-5rPf1i-55YATm-4DxQbz-4z4DGj-Fwhun-z2Bfj-mRKNQ-9jdFQ-2WCJ3Y-5usJQy-4JmHhG-NEozn)