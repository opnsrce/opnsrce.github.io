---
id: 146
title: How to Remove / Update Tooltips In Twitter Bootstrap
date: 2012-08-09T00:00:53+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=146
permalink: /how-to-remove-update-tooltips-in-twitter-bootstrap/
categories:
  - Code Snippets
  - Programming / Web Development
---
Recently, I ran into an issue with Twitter Bootstrap where I needed to update and show a tooltip based on certain conditions. Unfortunately, there&#8217;s no built-in way to change an existing tooltip once it&#8217;s been applied to an element. After doing some digging, I discovered that the tooltip&#8217;s data is stored with the elements `data` element in the `toggle` property. By setting this property to `false`, you&#8217;ll be able to update an existing tooltip.

<div class="wrap_githubgist" style="width:100%">
  <div style='margin-bottom:1em;padding:0;'>
    <noscript>
      <code>&lt;pre style='overflow:auto;margin:0;padding:0;border:1px solid #DDD;'>Not Found&lt;/pre></code>
    </noscript>
  </div>
</div>