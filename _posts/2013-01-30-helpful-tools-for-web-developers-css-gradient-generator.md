---
id: 201
title: 'Helpful Tools For Web Developers: CSS Gradient Generator'
date: 2013-01-30T00:00:07+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=201
permalink: /helpful-tools-for-web-developers-css-gradient-generator/
icy_video_embed_code:
  - 
categories:
  - Programming / Web Development
  - Tools
tags:
  - Colorzilla
  - CSS
  - generators
  - gradient
  - isoart
  - Mozilla
---
CSS3 bring a lot of really neat features to the table: animations, the ability to download fonts, among others. One of the features I was most excited about when CSS3 first began to gain browser support was gradients. Now, web developers and designers would no longer have to create 1px wide background images in order to use gradients in their designs. There was one problem, however. The CSS needed to both create the gradient _and_ provide support across all the major browsers was really, really complicated. 

<!--more-->

To generate support for this:

<a href="http://www.levihackwith.com/?attachment_id=203" rel="attachment wp-att-203"><img src="http://www.levihackwith.com/wp-content/uploads/2013/01/gradient_example.png" alt="gradient_example" width="371" height="52" class="aligncenter size-full wp-image-203" srcset="http://www.levihackwith.com/wp-content/uploads/2013/01/gradient_example-300x42.png 300w, http://www.levihackwith.com/wp-content/uploads/2013/01/gradient_example.png 371w" sizes="(max-width: 371px) 100vw, 371px" /></a>

You need all of this:

<pre class="brush: css; title: ; notranslate" title="">background: rgb(30,87,153); /* Old browsers */
/* IE9 SVG, needs conditional override of 'filter' to 'none' */
background: url(data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiA/Pgo8c3ZnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgdmlld0JveD0iMCAwIDEgMSIgcHJlc2VydmVBc3BlY3RSYXRpbz0ibm9uZSI+CiAgPGxpbmVhckdyYWRpZW50IGlkPSJncmFkLXVjZ2ctZ2VuZXJhdGVkIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzFlNTc5OSIgc3RvcC1vcGFjaXR5PSIxIi8+CiAgICA8c3RvcCBvZmZzZXQ9IjUwJSIgc3RvcC1jb2xvcj0iIzI5ODlkOCIgc3RvcC1vcGFjaXR5PSIxIi8+CiAgICA8c3RvcCBvZmZzZXQ9IjUxJSIgc3RvcC1jb2xvcj0iIzIwN2NjYSIgc3RvcC1vcGFjaXR5PSIxIi8+CiAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiM3ZGI5ZTgiIHN0b3Atb3BhY2l0eT0iMSIvPgogIDwvbGluZWFyR3JhZGllbnQ+CiAgPHJlY3QgeD0iMCIgeT0iMCIgd2lkdGg9IjEiIGhlaWdodD0iMSIgZmlsbD0idXJsKCNncmFkLXVjZ2ctZ2VuZXJhdGVkKSIgLz4KPC9zdmc+);
background: -moz-linear-gradient(top,  rgb(30,87,153) 0%, rgb(41,137,216) 50%, rgb(32,124,202) 51%, rgb(125,185,232) 100%); /* FF3.6+ */
background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,rgb(30,87,153)), color-stop(50%,rgb(41,137,216)), color-stop(51%,rgb(32,124,202)), color-stop(100%,rgb(125,185,232))); /* Chrome,Safari4+ */
background: -webkit-linear-gradient(top,  rgb(30,87,153) 0%,rgb(41,137,216) 50%,rgb(32,124,202) 51%,rgb(125,185,232) 100%); /* Chrome10+,Safari5.1+ */
background: -o-linear-gradient(top,  rgb(30,87,153) 0%,rgb(41,137,216) 50%,rgb(32,124,202) 51%,rgb(125,185,232) 100%); /* Opera 11.10+ */
background: -ms-linear-gradient(top,  rgb(30,87,153) 0%,rgb(41,137,216) 50%,rgb(32,124,202) 51%,rgb(125,185,232) 100%); /* IE10+ */
background: linear-gradient(to bottom,  rgb(30,87,153) 0%,rgb(41,137,216) 50%,rgb(32,124,202) 51%,rgb(125,185,232) 100%); /* W3C */
filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#1e5799', endColorstr='#7db9e8',GradientType=0 ); /* IE6-8 */
</pre>

Yeesh! Luckily, the folks over at <a href="http://www.iosart.com/" target="_blank">isoart</a> came up with <a href="http://www.colorzilla.com/gradient-editor/" target="_blank">The Ultimate CSS Gradient Generator</a> to help you quickly generate gradients via an easy to use graphical interface. If you&#8217;ve ever been frustrated with how difficult it is to create CSS gradients, you should check it out.