---
id: 378
title: 'Autocomplete Awesomeness: Why You Should Prefix Your Media Query Variables'
date: 2014-12-24T00:00:53+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=378
permalink: /autocomplete-awesomeness-why-you-should-prefix-your-media-query-variables/
icy_video_embed_code:
  - 
dsq_thread_id:
  - 4586109166
categories:
  - Code Snippets
  - Programming / Web Development
  - Tools
tags:
  - IDE
  - Media Queries
  - Responsive Design
  - SASS
---
I&#8217;ve read multiple blog posts about what to [name](http://css-tricks.com/naming-media-queries/) [your](https://gist.github.com/ethanmuller/7006656) [media queries](http://blog.grayghostvisuals.com/sass/naming-sass-media-queries/) and I doubt there will ever be a consensus on which way is best. That being said, I would like to offer some advice when it comes to naming your media query _variables_: Give every media query a common prefix (e.g., `$mq-` or `$bp-`). That way, when you use your autocomplete / intellisense in your IDE, you see this:

[<img src="http://www.levihackwith.com/wp-content/uploads/2014/12/Screen-Shot-2014-12-22-at-6.48.01-PM.png" alt="Screen Shot 2014-12-22 at 6.48.01 PM" width="610" height="291" class="aligncenter size-full wp-image-379" srcset="http://www.levihackwith.com/wp-content/uploads/2014/12/Screen-Shot-2014-12-22-at-6.48.01-PM-300x143.png 300w, http://www.levihackwith.com/wp-content/uploads/2014/12/Screen-Shot-2014-12-22-at-6.48.01-PM.png 610w" sizes="(max-width: 610px) 100vw, 610px" />](http://www.levihackwith.com/wp-content/uploads/2014/12/Screen-Shot-2014-12-22-at-6.48.01-PM.png)

Every single breakpoint, accessible and ready to use.