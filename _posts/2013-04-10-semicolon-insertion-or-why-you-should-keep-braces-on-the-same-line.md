---
title: 'Semicolon Insertion: Or Why You Should Keep Braces on the Same Line'
date: 2013-04-10T00:00:32+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
categories:
  - Programming / Web Development
tags:
  - JavaScript
---
When it comes to code formatting, developers can be pretty opinionated. Some believe in tabs while others like to use spaces. Some people believe the `else` statement should go on the same line as the closing brace of the `if` and some people think the `else` should go on the same line.

<!--more-->

Of the many things that developers can disagree on when it comes to code formatting, I think one of the most debated has to be brace position. Basically, it boils down to two camps: those that believe the brace belongs on the same line:

<pre class="brush: jscript; title: ; notranslate" title="">return {
    someProperty: "someValue"
};
</pre>

And those that believe the brace belongs on the next line:

<pre class="brush: jscript; title: ; notranslate" title="">return
{
    someProperty: "someValue"
};
</pre>

For the most part, brace placement is simply a matter of preference. However, there are times when where you place your braces can have unintended consequences. When the second code block is executed as part of a function, the value returned is &#8220;undefined&#8221; instead of &#8220;object&#8221;. This is because JavaScript is automatically inserting what it thinks is a missing semicolon which turns the code block into this:

<pre class="brush: jscript; title: ; notranslate" title="">return;
{
    someProperty: "someValue"
}
</pre>

Basically, the interpreter expects that, when the `return` statement returns a value, the value it&#8217;s returning is on the same line as the `return` statement.