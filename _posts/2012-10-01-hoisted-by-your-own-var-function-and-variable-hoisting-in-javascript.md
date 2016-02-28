---
title: 'Hoisted by your Own Var: Function and Variable Hoisting in JavaScript'
date: 2012-10-01T23:27:20+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - hoisting
  - JavaScript
---
Let&#8217;s take a minute to talk about function / variable hoisting. In JavaScript hoisting means that, regardless of where a function is declared, it is moved or _hoisted_ to the top of whatever scope it&#8217;s been declared in. Okay, that explanation was a little fuzzy so let&#8217;s back it up with a quick example:

<div class="wrap_githubgist" style="width:100%">
  <div style='margin-bottom:1em;padding:0;'>
    <noscript>
      <code>&lt;pre style='overflow:auto;margin:0;padding:0;border:1px solid #DDD;'>Not Found&lt;/pre></code>
    </noscript>
  </div>
</div>

<!--more-->



Alright, here we have a very simple script that first declares a global variable called _myGlobal_ followed by a _hoistMe_ method which contains its own declaration of the _myGlobal_ variable and a series of alert messages. Let&#8217;s run this and see what happens.

[<img class="aligncenter size-full wp-image-154" title="hoist_variable_alert" alt="" src="http://www.levihackwith.com/wp-content/uploads/2012/10/hoist_variable_alert.png" width="534" height="267" srcset="http://www.levihackwith.com/wp-content/uploads/2012/10/hoist_variable_alert-300x150.png 300w, http://www.levihackwith.com/wp-content/uploads/2012/10/hoist_variable_alert.png 534w" sizes="(max-width: 534px) 100vw, 534px" />](http://www.levihackwith.com/wp-content/uploads/2012/10/hoist_variable_alert.png)

In this example, you would expect that the first alert would say &#8216;Global&#8217; instead of &#8216;undefined&#8217;. However, due to hoisting, our _myGlobal variable_ is moved to the top of the scope that it&#8217;s been declared in and the value is overwritten. This means that our JavaScript interpreter actually sees our function like this:



<div class="wrap_githubgist" style="width:100%">
  <div style='margin-bottom:1em;padding:0;'>
    <noscript>
      <code>&lt;pre style='overflow:auto;margin:0;padding:0;border:1px solid #DDD;'>Not Found&lt;/pre></code>
    </noscript>
  </div>
</div>



As you can see, in this example, _myGlobal_ is getting overridden and set to _undefined_ when the function executes. Why would JavaScript decide to behave in this manner, you ask? Well, one of the main advantages of hoisting is that it gives you the flexibility to use a function before actually declaring it. As helpful as that may sound, I find such coding practices sloppy and error-prone.

Let&#8217;s take a look at an example using function statements:



<div class="wrap_githubgist" style="width:100%">
  <div style='margin-bottom:1em;padding:0;'>
    <noscript>
      <code>&lt;pre style='overflow:auto;margin:0;padding:0;border:1px solid #DDD;'>Not Found&lt;/pre></code>
    </noscript>
  </div>
</div>



Now, when you first look at this, you&#8217;d think that your alert would say 5 when in fact you get 15:

[<img class="aligncenter size-full wp-image-155" title="hoist_method_alert" alt="" src="http://www.levihackwith.com/wp-content/uploads/2012/10/hoist_method_alert.png" width="534" height="267" srcset="http://www.levihackwith.com/wp-content/uploads/2012/10/hoist_method_alert-300x150.png 300w, http://www.levihackwith.com/wp-content/uploads/2012/10/hoist_method_alert.png 534w" sizes="(max-width: 534px) 100vw, 534px" />](http://www.levihackwith.com/wp-content/uploads/2012/10/hoist_method_alert.png)

On top of the confusing result, we&#8217;ve always been taught that code written after a _return_ statement can never, ever be run so this code should definitely not be behaving the way it is. Well, remember how we talked about variables getting hoisted to the top of the function declaration? The same occurs for functions. Despite how our code is written, our JavaScript interpreter is actually reading the code like this:



<div class="wrap_githubgist" style="width:100%">
  <div style='margin-bottom:1em;padding:0;'>
    <noscript>
      <code>&lt;pre style='overflow:auto;margin:0;padding:0;border:1px solid #DDD;'>Not Found&lt;/pre></code>
    </noscript>
  </div>
</div>



In the above example, the declaration of _foo_ that returns 15 is overriding the declaration of _foo_ that returns 5.

I hope this helps someone out there. If you have any questions, please leave a comment below.