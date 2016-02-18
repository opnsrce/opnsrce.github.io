---
id: 289
title: 'Code Snippet: Prevent Flickering When Enforcing Maxlength on Textareas'
date: 2013-05-20T00:00:36+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=289
permalink: /code-snippet-prevent-flickering-when-enforcing-maxlength-on-textareas/
icy_video_embed_code:
  - 
dsq_thread_id:
  - 4586109830
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - JavaScript
---
I was doing some research today regarding how to limit the number of characters on the page while removing the annoying flickering effect that often occurs with JavaScript-based solutions to the problem. Here&#8217;s what I came up with:
  
<!--more-->

<pre class="brush: jscript; title: ; notranslate" title="">document.addEventListener('DOMContentLoaded', function() {
        var textArea = document.getElementById('textarea'), // Just a random &lt;textarea&gt; on the page
            i,
            limitTextLength,
            charRemainingLabel = document.getElementById('charsRemaining'); // span on the page to show chars left
            
        limitTextLength = function(e) {
            var maxLength = 200,
                key,
                charsRemaining = 200,
                me = this;
                
            e = e || window.event;
            key = e.which;
            charsRemaining = Math.max(0, (maxLength - me.value.length));
            
            charRemainingLabel.textContent = charsRemaining + " characters remaining";
            if( (key &gt; 31 || key === 13) && e.type === 'keypress') {
                if(charsRemaining &lt;= 0) { // cancel normal typing
                    e.preventDefault();
                }
            } else { // Allows for backspace and copy-and-paste
                me.value = me.value.substr(0, 200); 
            }
        }
        
        textArea.addEventListener('keypress', limitTextLength, false);
        textArea.addEventListener('keyup', limitTextLength, false);
    }, false);    
</pre>

The most important part is the distinction between `keypress` and `keyup`. The `keypress` event can be canceled properly because it occurs whenever a regular key is pressed (letters, numbers, etc.,). However, if you want the event to fire when keys like `backspace` are hit, you need to add the same handler to the `keyup` event.