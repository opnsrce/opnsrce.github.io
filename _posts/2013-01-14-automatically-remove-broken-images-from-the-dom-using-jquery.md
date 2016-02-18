---
id: 175
title: Automatically Remove Broken Images from the DOM using jQuery
date: 2013-01-14T00:00:43+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=175
permalink: /automatically-remove-broken-images-from-the-dom-using-jquery/
icy_video_embed_code:
  - 
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - Automation
  - error handling
  - gallery
  - images
  - JavaScript
---
A while back I was tasked with finding a way to automatically remove broken images from a gallery of images. The problem was that, in this system, users were able to bulk-upload image descriptions via CSV and then upload the images later on. If the image gallery went live before all the images were uploaded, the result was a gallery full of broken images that really made the user experience suck (see below for an example demo of the problem).

<!--more-->

<p style="text-align: center">
  <a href="http://www.levihackwith.com/automatically-remove-broken-images-from-the-dom-using-jquery/broken-images/" rel="attachment wp-att-176"><img class="aligncenter  wp-image-176" alt="broken images" src="http://www.levihackwith.com/wp-content/uploads/2013/01/broken-images.png" width="334" height="332" srcset="http://www.levihackwith.com/wp-content/uploads/2013/01/broken-images-300x298.png 300w, http://www.levihackwith.com/wp-content/uploads/2013/01/broken-images.png 556w" sizes="(max-width: 334px) 100vw, 334px" /></a>
</p>

At the time, the only way to fix this issue was time-consuming and overly complicated:

  1. User notices that their gallery contains broken images and notifies the developers.
  2. the developers either a) go hunting around for the broken images and upload them or b) run SQL commands to remove the invalid image references from the database.

As you can see, there&#8217;s a lot of time and manual labor that goes into fixing this kind of problem. However, there is a way to get around this.

## Introducing (and Handling) The Error Event

Images have an `error` event that fires whenever the image fails to load. With this in mind, you can add an event handler to that event that removes the image if it fails to load. Here&#8217;s how to do it using jQuery:

<pre class="brush: jscript; title: ; notranslate" title="">img.error(function() {
    $(this).remove();
});
</pre>

All this is doing is removing the image from the DOM whenever the image&#8217;s `error` event fires.

## Dealing With Multiple Containers

As an additional example, let&#8217;s say your image gallery had a link and a div wrapped around it:

<pre class="brush: xml; title: ; notranslate" title="">&lt;div&gt;
    &lt;a href="http://www.google.com"&gt;
        &lt;img alt="" src="myBrokeImage.jpg" /&gt;
    &lt;/a&gt;
&lt;/div&gt;
</pre>

In that case, you would alter the event handler like so:

<pre class="brush: jscript; title: ; notranslate" title="">img.error(function() {
    $(this).parent().parent().remove();
});
</pre>

This would remove the entire `<div>` and not just the image.

## Other Cool Things You Could Do With This

There&#8217;s some pretty cool things you can do with this event handler beyond just removing the image from the page. You could also:

1. Send an AJAX request that triggers an email to someone if an image fails to load multiple times.
  
2. Retrieve an alternate image or custom placeholder image.

If you need to grab the source of the image that failed, you can simply call 

<pre class="brush: jscript; title: ; notranslate" title="">$(this).attr('src')
</pre>

before you remove the image from the DOM and it will return the path of the image that tried to load.

## Things to Keep in Mind

When working with an image&#8217;s `error` event, there are a few things you&#8217;ll want to keep in mind:

First, the `error` event fires after the `src` attribute of the image has been set. You&#8217;ll want to make sure you bind your event handler before this happens by placing the event binding inside of the callback for jQuery&#8217;s `.ready()` method.

Second, if you have a jQuery plugin that expects the images to be present before it is instantiated, make sure you move the instantiation logic into a method that will fire after _all_ elements of the page are done loading such as a handler for the window&#8217;s `load` event.