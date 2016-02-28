---
title: 'Book Recommendation: High Performance JavaScript'
date: 2013-01-16T00:00:15+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
categories:
  - Books
  - Programming / Web Development
tags:
  - JavaScript
  - Nicholas C Zakas
  - performance
---
If you&#8217;ve often found yourself struggling to figure out the best way to write JavaScript in order to speed up your web applications, you&#8217;re not alone. As I&#8217;ve gotten to work on more complex and larger web applications, I&#8217;ve started to notice how difficult it is to keep the application working at a speed that doesn&#8217;t harm the user experience. More often then not, this has as much to do with poorly written code as it does with code that just doesn&#8217;t quite scale well. That list scrolled so gracefully with 30 items in it, but begins to choke and lock up the browser when fed 300.

<!--more-->



Luckily, Nicholas C Zakas is here to help. In his book <cite>High Performance JavaScript (Build Faster Web Application Interfaces)</cite>, he goes over some of the more common performance pitfalls when it comes to writing efficient JavaScript that scales well. Here&#8217;s one my favorite tidbits regarding identifier resolution:

> Identifier resolution isn’t free, as in fact no computer operation really is without some sort of performance overhead. The deeper into the execution context’s scope chain an identifier exists, the slower it is to access for both reads and writes. Consequently, local variables are always the fastest to access inside of a function, whereas global variables will generally be the slowest (optimizing JavaScript engines are capable of tuning this in certain situations). Keep in mind that global variables always exist in the last variable object of the execution context’s scope chain, so they are always the furthest away to resolve. Figures 2-4 and 2-5 show the speed of identifier resolution based on their depth in the scope chain. A depth of 1 indicates a local variable.
>
> ..A good rule of thumb is to always store out-of-scope values in local variables if they are used more than once within a function..

<a href="http://www.levihackwith.com/?attachment_id=184" rel="attachment wp-att-184"><img src="http://www.levihackwith.com/wp-content/uploads/2013/01/figure-2-4.png" alt="figure 2-4" width="678" height="620" class="aligncenter size-full wp-image-184" srcset="http://www.levihackwith.com/wp-content/uploads/2013/01/figure-2-4-300x274.png 300w, http://www.levihackwith.com/wp-content/uploads/2013/01/figure-2-4.png 678w" sizes="(max-width: 678px) 100vw, 678px" /></a>

<cite>Zakas, Nicholas C. (2010-03-11). High Performance JavaScript (p. 19). OReilly Media &#8211; A. Kindle Edition.</cite>

I want to take a moment and point out some of the browsers in that chart. As you can see, they are pretty old compared to where we are today. A few of the problems that Zakas talks about aren&#8217;t problems in most of the modern browsers we use today. That being said, most of the solutions in this book still apply and I still highly recommend this book to anyone who&#8217;s really looking to get into the nuts and bolts of how their JavaScript application behaves and make it run faster. It&#8217;s available in both paperback and Kindle formats on <a href="http://www.amazon.com/Performance-JavaScript-Faster-Application-Interfaces/dp/059680279X" target="_blank">Amazon</a>.