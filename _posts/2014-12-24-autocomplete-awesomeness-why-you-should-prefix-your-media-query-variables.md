---
title: 'Autocomplete Awesomeness: Why You Should Prefix Your Media Query
       Variables'
date: 2014-12-24T00:00:53+00:00
author: Levi Hackwith
layout: post
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

[1]: /wp-content/uploads/2014/12/Screen-Shot-2014-12-22-at-6.48.01-PM.png
[2]: http://css-tricks.com/naming-media-queries/
[3]: https://gist.github.com/ethanmuller/7006656
[4]: http://blog.grayghostvisuals.com/sass/naming-sass-media-queries/

I&rsquo;ve read multiple blog posts about what to [name][2] [your][2]
[media queries][4] and I doubt there will ever be a consensus on which way is
best. That being said, I would like to offer some advice when it comes to
naming your media query _variables_: Give every media query a common
prefix (e.g., ``$mq-`` or ``$bp-``). That way, when you use your autocomplete /
intellisense in your IDE, you see this:
<!--more-->
![IDE ScreenShot][1]

Every single breakpoint, accessible and ready to use.