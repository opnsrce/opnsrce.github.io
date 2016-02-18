---
id: 38
title: 'Add Event Listeners to &#8216;Play&#8217; and Other Media Events Using Sencha Touch'
date: 2011-02-26T18:31:12+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=38
permalink: /add-event-listeners-to-play-and-other-media-events-using-sencha-touch/
icy_video_embed_code:
  - 
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - Audio
  - HTML5
  - JavaScript
  - Sencha Touch
---
Recently, I was working on a side-project that involved allowing the user to press play and listen to a sample track from a list of tracks on their iPhone. While this functionality works great when the user is on WiFi, the delay between pressing &#8216;Play&#8217; and hearing the song on a 3G connection makes the application feel sluggish and non-responsive. My first idea was to add an event listener to the &#8216;play&#8217; event (or something similar) and show / hide some sort of loading message when the user selects &#8216;play&#8217;. Unfortunately, the Sencha Touch API doesn&#8217;t support any such event. However, there is a way around this.

<!--more-->

If you dig within the <a href="http://dev.sencha.com/deploy/touch/docs/source/Audio.html#cls-Ext.Audio" target="_blank">source code</a>, you&#8217;ll notice that, whenever you declare and render a new Audio object, an <audio> tag is applied to the current HTML page. Native HTML objects like <audio> <a href="https://developer.mozilla.org/en/Using_audio_and_video_in_Firefox#Media_events" target="_blank">have their own set of events</a> that can be &#8220;listened&#8221; to by the browser and therefore the Sencha Touch Library. Here&#8217;s how:

<pre class="brush: jscript; title: ; notranslate" title="">// This would be inside of an 'itemtap' event listener method
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
...</pre>

What we&#8217;re doing here is pretty straight-forward. The part to pay attention to is line 10, the &#8220;element&#8221; property. Much like the how the &#8220;scope&#8221; property of other config objects lets us change the &#8220;this&#8221; or &#8220;self&#8221; reference of a method call, the &#8220;element&#8221; property lets us change what element the event listener is paying attention to. In this case &#8216;media&#8217; lets us access the native HTML5 <audio> tag, and listen for the &#8216;canplay&#8217; event. Once the event fires, the LoadMask is hidden.

Hopefully, this helps you out as much as it did me. Feel free to post a comment with any questions you might have.