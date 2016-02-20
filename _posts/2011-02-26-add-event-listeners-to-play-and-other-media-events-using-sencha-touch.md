---
title: Add Event Listeners to "Play" and Other Media Events Using Sencha Touch
date: 2011-02-26T18:31:12+00:00
author: Levi Hackwith
layout: post
permalink: /add-event-listeners-to-play-and-other-media-events-using-sencha-touch/
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - Audio
  - HTML5
  - JavaScript
  - Sencha Touch
---

[1]: http://dev.sencha.com/deploy/touch/docs/source/Audio.html#cls-Ext.Audio
[2]: https://developer.mozilla.org/en/Using_audio_and_video_in_Firefox#Media_events

Recently, I was working on a side-project that involved allowing the user to
press play and listen to a sample track from a list of tracks on their iPhone.
'While this functionality works great when the user is on WiFi, the delay
between pressing &ldquo;Play&rdquo; and hearing the song on a 3G connection
makes the application feel sluggish and non-responsive. My first idea was to
add an event listener to the ``play`` event (or something similar)
and show / hide some sort of loading message when the user selects
&ldquo;play&rdquo;. Unfortunately, the Sencha Touch API doesn&rsquo;t
support any such event. However, there is a way around this.

<!--more-->

If you dig within the [source code][1], you&rsquo;ll notice that, whenever you
declare and render a new Audio object, an ``<audio>`` tag is applied to the
current HTML page. Native HTML objects like <audio>
[have their own set of events][2]that can be listened to by the browser and
therefore the Sencha Touch Library. Here&rsquo;s how:

~~~js
// This would be inside of an 'itemtap' event listener method
...
myAudio = new Ext.Audio({
    id: 'audioPreview',
    hidden: true,
    url: audioURL,
    renderTo: Ext.getBody(),
    listeners: {
        canplay: {
            element: 'media',
            fn: function() {
                audioLoadMask.hide();
            }
        }
    }
});
Envato.AudioJungle.Previewer.audioPreview.play()
audioLoadMask.show();
...
~~~

What we&rsquo;re doing here is pretty straight-forward. The part to pay
attention to is line 10, the ``element`` property. Much like the how the
``scope`` property of other config objects lets us change the ``this`` or
``self`` reference of a method call, the ``element`` property lets us change
what element the event listener is paying attention to. In this case,
``media`` lets us access the native HTML5 ``<audio>`` tag, and listen for the
``canplay`` event. Once the event fires, the ``LoadMask`` is hidden.

Hopefully, this helps you out as much as it did me. Feel free to post a
comment with any questions you might have.