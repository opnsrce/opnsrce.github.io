---
id: 207
title: 'JavaScript Performance Tip: Precompile Your Regular Expressions'
date: 2013-02-04T00:00:32+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=207
permalink: /javascript-performance-tip-precompile-your-regular-expressions/
icy_video_embed_code:
  - 
categories:
  - Programming / Web Development
tags:
  - JavaScript
  - jsperf
  - performance
  - regex
---
When it comes to speeding up your web applications, the little things can make quite a difference. One of the ways you can improve the performance of your application is by &#8220;precompiling&#8221; any regular expressions you use. But wait, JavaScript is an interpreted language. How can a regular expression be precompiled? Well, take a look at the following code:

<!--more-->

<pre class="brush: jscript; title: ; notranslate" title="">var preCompiledReplaceRegex = /test/g; 
    myHtml = "&lt;span&gt;This is a test&lt;/span&gt;&lt;div&gt;Of a regex&lt;/div&gt;&lt;p&gt;test&lt;/p&gt;&lt;em&gt;test&lt;/em&gt;";

   myHtml.replace(preCompiledReplaceRegex, 'kittens'); // Compiled Regex
</pre>

By storing the regex in a variable before using it to replace the word &#8220;test&#8221; with the word &#8220;kittens&#8221;, we increase the performance of the code. When a regex is used and _not_ stored in a variable, it gets reevaluated every time the `replace` method is called. By storing it in a variable before use, we guarantee that the expression only gets evaluated once. Let&#8217;s rewrite the above example, but use the regex directly in the call to the `replace` method:

<pre class="brush: jscript; title: ; notranslate" title="">var myHtml = "&lt;span&gt;This is a test&lt;/span&gt;&lt;div&gt;Of a regex&lt;/div&gt;&lt;p&gt;test&lt;/p&gt;&lt;em&gt;test&lt;/em&gt;";

myHtml.replace(/test/g, "kittens");
</pre>

When we run these snippets through [JsPerf](http://jsperf.com/regex-performance-testing/2 "jsPerf") we get the following (in Chrome):

[<img src="http://www.levihackwith.com/wp-content/uploads/2013/01/jsPerf-regex.png" alt="jsPerf regex" width="961" height="200" class="aligncenter size-full wp-image-211" srcset="http://www.levihackwith.com/wp-content/uploads/2013/01/jsPerf-regex-300x62.png 300w, http://www.levihackwith.com/wp-content/uploads/2013/01/jsPerf-regex.png 961w" sizes="(max-width: 961px) 100vw, 961px" />](http://www.levihackwith.com/wp-content/uploads/2013/01/jsPerf-regex.png)

Here&#8217;s a breakdown of the performance across multiple browsers:

[<img src="http://www.levihackwith.com/wp-content/uploads/2013/01/jfperf-regex-chart.png" alt="jfperf regex chart" width="960" height="731" class="aligncenter size-full wp-image-209" srcset="http://www.levihackwith.com/wp-content/uploads/2013/01/jfperf-regex-chart-300x228.png 300w, http://www.levihackwith.com/wp-content/uploads/2013/01/jfperf-regex-chart.png 960w" sizes="(max-width: 960px) 100vw, 960px" />](http://www.levihackwith.com/wp-content/uploads/2013/01/jfperf-regex-chart.png)

When I ran this test in IE9, JsPerf calculated a 9% speed difference between the precompiled regex vs the non-precompiled one; that&#8217;s nothing to sneeze at.