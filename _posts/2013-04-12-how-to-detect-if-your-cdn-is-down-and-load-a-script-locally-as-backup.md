---
id: 274
title: 'How to &#8220;Detect&#8221; If Your CDN is Down And Load a Script Locally As Backup'
date: 2013-04-12T00:00:33+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=274
permalink: /how-to-detect-if-your-cdn-is-down-and-load-a-script-locally-as-backup/
icy_video_embed_code:
  - 
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - JavaScript
  - jQuery
---
I&#8217;m sure this has been around for a while now, but I just stumbled upon it and found it interesting:

<pre class="brush: jscript; title: ; notranslate" title="">...
&lt;script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"&gt;&lt;/script&gt;
&lt;script&gt;
window.jQuery || document.write('&lt;script src="js/vendor/jquery-1.9.1.min.js"&gt;&lt;\/script&gt;')&lt;/script&gt;
...
</pre>

Basically, this does a check to see if jQuery has loaded properly from the CDN and, if it hasn&#8217;t, it tries to load it locally.