---
id: 283
title: A Helpful Guide to Moving Away From jQuery (Via the Lonely Coder)
date: 2013-05-06T00:00:56+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=283
permalink: /a-helpful-guide-to-moving-away-from-jquery-via-the-lonely-coder/
icy_video_embed_code:
  - 
categories:
  - Programming / Web Development
tags:
  - JavaScript
  - jQuery
---
Recently, I wrote a post about how jQuery&#8217;s prevalence on the web was causing web developers to learn less JavaScript and more jQuery due to how it conceals many of the more complicated inner workings of JavaScript in wrapper methods like `bind` and `ready`. 

Michael Enger over at <a href="http://blog.thelonelycoder.com/" target="_blank">The Lonely Coder</a> seems to agree with me and he put together a <a href="http://blog.thelonelycoder.com/2013/04/30/removing-jquery-from-a-web-app/" target="_blank">really cool guide</a> on how to replace some of the more common jQuery methods with their native JavaScript counterparts. In addition to going over how to replace `ready` and how to do event delegation, he does an excellent job of covering CSS selectors. From the guide:

> One of the greatest benefits of jQuery is to be able to drill down into the DOM by using CSS-style selector strings to specify which element you’re looking for. Something as complicated as “`#app ul .title a:hover > span.left`&#8221; can be used to choose one specific element, or a set of elements that are situated in various places around the document. Unfortunately there isn’t a direct replacement in native JavaScript, but a combination of `getElementById`, `getElementsByTagName` and `getElementsByClassName`, as well as iterating through the results, can be used to select the element(s) you need and not being able to rely on CSS pseudo-classes or some of the more esoteric selectors may result in structuring the HTML in a less convoluted way, avoiding unnecessary strain on the browser who has to deal with all your crazy shenanigans.
> 
> <pre class="brush: jscript; title: ; notranslate" title="">// Get the data-foo attribute of all links inside a .button list
var buttons = document.getElementsByClassName('buttons'),
    foo = '';
for (var i = 0; i &lt; buttons.length; i++) {
    var links = buttons[i].getElementsByTagName('a');
    for (var j = 0; j &lt; links.length; j++) {
        var link = links[j];
        foo += link.attributes['data-foo'];
    }
}
</pre>
> 
> Edit: My good friend Torjus Bjåen made me aware of the `querySelectorAll` function, which provides the same CSS-style selector capabilities that jQuery does, albeit without some of the more “magical” selectors. It works like you’d expect and can be used to easily fetch elements that may be spread about the DOM.
> 
> <pre class="brush: jscript; title: ; notranslate" title="">var links = document.querySelectorAll('.buttons a.special');
for (var i = 0; i &lt; links.length; i++) {
    links[i].style.backgroundColor = '#f09';
}
</pre>

I highly suggest you check out his guide, it&#8217;s an excellent starting place for those looking to move away from jQuery and to a more native approach.