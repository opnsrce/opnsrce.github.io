---
title: Why Array.Splice Belongs With Push, Pop, Shift, and Unshift
date: 2013-04-29T00:00:37+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
categories:
  - Programming / Web Development
tags:
  - JavaScript
---
If you take a look at tutorials about JavaScript adding and removing items from an array, you&#8217;ll see four methods mentioned: `Push`, `Pop`, `Shift`, and `Unshift`. If you&#8217;re new to JavaScript or need a refresher, here&#8217;s a quick breakdown of each of those methods.

## `Push`

**Definition:** Mutates an array by appending the given elements and returning the new length of the array. This method changes the length of the array.

<!--more-->

**Syntax:**

<pre class="brush: jscript; title: ; notranslate" title="">array.push(element1, ..., elementN); </pre>

**Example:**

<pre class="brush: jscript; title: ; notranslate" title="">var myArray = [1,2,3,4,5];

console.log('Before: ' + myArray.join(', ')); // OUTPUT: 1, 2, 3, 4, 5
myArray.push(6,7,8,9);
console.log('After: ' + myArray.join(', ')); // OUTPUT: 1,2,3,4,5,6, 7, 8, 9
</pre>

## `Pop`

**Definition:** Removes the last element from an array and returns that element. This method changes the length of the array.

**Syntax:**

<pre class="brush: jscript; title: ; notranslate" title="">array.pop();</pre>

**Example:**

<pre class="brush: jscript; title: ; notranslate" title="">var myArray = [1,2,3,4,5],
    removed;

console.log('Before: ' + myArray.join(', ')); // OUTPUT: 1, 2, 3, 4, 5
removed = myArray.pop();
// OUPUT: I removed 5 and the array is now 1, 2, 3, 4
console.log('After: I removed ' + removed + ' and the array is now ' + myArray.join(', '));
</pre>

## `Shift`

**Definition:** Removes the first element from an array and returns that element. This method changes the length of the array.

**`Syntax:`**

<pre class="brush: jscript; title: ; notranslate" title="">array.shift();</pre>

**Example:**

<pre class="brush: jscript; title: ; notranslate" title="">var myArray = [1,2,3,4,5],
    removed;

console.log('Before: ' + myArray.join(', ')); // OUTPUT: 1, 2, 3, 4, 5
removed = myArray.shift();
// OUPUT: I removed 1 and the array is now 2, 3, 4, 5
console.log('After: I removed ' + removed + ' and the array is now ' + myArray.join(', '));
</pre>

## `Unshift`

**Definition:** Adds one or more elements to the beginning of an array and returns the new length of the array. This method changes the length of the array.

**Syntax:**

<pre class="brush: jscript; title: ; notranslate" title="">arrayName.unshift(element1, ..., elementN) </pre>

**Example:**

<pre class="brush: jscript; title: ; notranslate" title="">var myArray = [1,2,3,4,5];

console.log('Before: ' + myArray.join(', ')); // OUTPUT: 1, 2, 3, 4, 5
myArray.unshift(6,7,8,9);
console.log('After: ' + myArray.join(', ')); // OUTPUT: 6, 7, 8, 9, 1, 2, 3, 4, 5
</pre>

## Introducing `Splice`

While `Push`, `Pop`, `Shift` and `Unshift` are all extremely handy, there&#8217;s another method that goes too often unmentioned when it comes to array methods: Splice. Why is `Splice` left out of most array tutorials? Well, for starters, it&#8217;s definition isn&#8217;t exactly clear:

> Changes the content of an array, adding new elements while removing old elements.

<cite>The Mozilla Developer Network</cite>

Personally, I don&#8217;t find that very enlightening. I think a much better definition might be

> Changes the contents of an array, removing `n` elements starting at the specified index while adding new elements at the specified index.

`Splice` could be also summed up as &#8220;it&#8217;s a lot like `Push`, but it allows you to insert a new element at a specific index instead of just the end of the array&#8221;.

### Examples

To help clarify `Splice`&#8216;s uses, let&#8217;s run through a couple of examples.

#### Insert a New Element at a Specific Point in the Array

<pre class="brush: jscript; title: ; notranslate" title="">var myArray = [1,2,3,5], // Needs a 4
    numElementsToRemove = 0,
    indexToInsertNewElementAt = 3,
    elementToInsert = 4;

console.log('Before: ' + myArray.join(', ')); // 1, 2, 3, 5
myArray.splice(indexToInsertNewElementAt, numElementsToRemove, elementToInsert);
console.log('After: ' + myArray.join(', ')); // 1, 2, 3, 4, 5
</pre>

Here we&#8217;re using `Splice` to add the number 4 at the proper place in the array. Everything here should be pretty straight forward, but let&#8217;s take a closer look at the `numElementsToRemove`. What happens if we increment that number to 1?

#### Insert a New Element at a Specific Point in the Array and Removing an Element

<pre class="brush: jscript; title: ; notranslate" title="">var myArray = [1,2,3,5], // Needs a 4
    numElementsToRemove = 1,
    indexToInsertNewElementAt = 3,
    elementToInsert = 4;

console.log('Before: ' + myArray.join(', ')); // 1, 2, 3, 5
myArray.splice(indexToInsertNewElementAt, numElementsToRemove, elementToInsert);
console.log('After: ' + myArray.join(', ')); // 1, 2, 3, 4
</pre>

Here, `Splice` is adding the 4 at the third index and then removing one element after the third index.

#### Calling `Splice` With a Single Argument

Despite what the documentation says, you _can_ call `Splice` with a single argument. However, <a href="http://stackoverflow.com/questions/5759504/can-array-splice-be-called-with-one-argument" target="_blank">from the sounds of it</a>, you really shouldn&#8217;t.

<pre class="brush: jscript; title: ; notranslate" title="">var myArray = [1,2,3,4,5];

console.log('Before: ' + myArray.join(', ')); // 1, 2, 3, 4, 5
myArray.splice(4);
console.log('After: ' + myArray.join(', ')); // 1, 2, 3, 4
</pre>

Calling `Splice` with a single argument returns all elements up to the index specified (e.g., imputing the number four will return indexes one through three). Again, this behavior isn&#8217;t exactly standard, so I&#8217;d avoid using it just in case it gets depreciated down the road.

## Wrapping Up

Well, I hope you&#8217;ve found this introduction to `Splice` helpful. If you have any questions or notice something I may have misstated, please leave a comment.