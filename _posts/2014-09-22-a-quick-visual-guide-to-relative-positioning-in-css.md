---
title: A Quick Visual Guide to Relative Positioning in CSS
date: 2014-09-22T00:00:34+00:00
author: Levi Hackwith
layout: post
excerpt: 'Getting your head around positioning elements in CSS can be very
confusing. When I first started doing front-end web development, I would often
end up spending hours trying to figure out why one element or another was
refusing render where I thought it should. Nine times out of ten, the problem
usually had something to do with the surrounding elements and what the value of
their position attribute happened to be.'
categories:
  - Programming / Web Development
tags:
  - CSS
---

[1]: http://codepen.io/opnsrce/pen/bgHAJ/

Getting your head around positioning elements in CSS can be very confusing.
When I first started doing front-end web development, I would often end up
spending hours trying to figure out why one element or another was refusing
render where I thought it should. Nine times out of ten, the problem usually
had something to do with the surrounding elements and what the value of their
``position`` attribute happened to be.

In order to help new developers understand how relative positioning works in
CSS, I put together a quick [visual demonstration][1].


The box labeled &ldquo;5&rdquo; is absolutely positioned zero pixels from the
right side of its parent container (by default, container 4).

When you click on one of the checkboxes, the corresponding container
divs ``position`` property gets set to ``static`` (the default value). If you
click on the checkbox labeled &ldquo;Disable Level 4&rdquo;, you&rsquo;ll
notice that the &ldquo;5&rdquo; box jumps from the right of box 4 to the right
of box 3. This is because, by setting 4&rsquo;s position to ``static``
instead of ``relative``, you are telling box 5 that 4 is no longer the parent
container. Confused? I was too. When we look at the nested nature of HTML,
we would assume that the &ldquo;parent container&rdquo; of an element is the
nearest element that contains another element. In our case, the parent of 5
would be 4. However, the browser sees things a little different. It defines a
parent element as the nearest element that contains another element _that also
has its ``position`` element set to ``relative``_. By changing the
``position`` attribute of a parent element, you&rsquo;re forcing the browser
to look for the next nearest element with a relative position. Notice how,
if you recheck the checkbox, the 5 box jumps back into place.