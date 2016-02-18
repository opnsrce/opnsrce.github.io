---
id: 322
title: Helpful Chrome Flags For Web Developers
date: 2013-11-11T00:00:17+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=322
permalink: /helpful-chrome-flags-for-web-developers/
icy_video_embed_code:
  - 
categories:
  - Programming / Web Development
  - Tools
tags:
  - chrome
  - flags
---
Most of the time, I develop locally when writing code: I don&#8217;t like taking the time to upload files to a server for testing. Unfortunately, this can make testing things like AJAX calls and references to local files difficult due to security settings that come default with Chrome (my preferred browser). Recently, I discovered some really handy flags that you can append to Chrome when launching from the command line. 

<!--more-->

## &#8211;disable-web-security

This flag is great for when you want to be able to send AJAX requests to a domain different from the page your testing and don&#8217;t want to run into the same-origin policy that blocks such requests by default. I like to use this flag when I&#8217;m developing against a third party API or my development environment&#8217;s configuration doesn&#8217;t (or can&#8217;t) match what&#8217;s in production.

## &#8211;allow-file-access-from-files

This flag lets files loaded in the browser (that is being served locally via `file://` instead of a web server) access other local files. I find this comes in handy when I want to work with a copy of a website without spinning up a web server to view the files. 

## What Flags Have You Found Helpful?

If there&#8217;s other flags that you&#8217;ve found helpful in your development workflow, please leave a comment below so I can add it to the list!