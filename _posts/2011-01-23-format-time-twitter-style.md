---
title: 'Format Time Twitter-Style'
date: 2011-01-23T22:28:21+00:00
author: Levi Hackwith
layout: post
permalink: /format-time-twitter-style/
categories:
  - Code Snippets
tags:
  - PHP
---
When you post a Tweet, it get&rsquo;s timestamped with something like
&quot;posted 20 minutes ago&quot;. If you&rsquo;d like to replicate this 
behavior in PHP, here&rsquo;s a function you can use:

<!--more-->

~~~php
function calc_time_diff($timestamp, $unit = NULL, $show_unit = TRUE) {
    // How many seconds have elapsed
    $seconds = round((time() - $timestamp));
    // How many minutes have elapsed
    $minutes = round((time() - $timestamp) / 60);
    // How many hours have elapsed
    $hours = round((time() - $timestamp) / 60 / 60);
    // How many hours have elapsed
    $days = round((time() - $timestamp) / 60 / 60 / 24);
    $seconds_string = $seconds;
    $minutes_string = $minutes;
    $hours_string = $hours;
    $days_string = $days;
    switch($unit) {
        case "seconds": return $seconds;
            break;
        case "minutes": return $minutes;
            break;
        case "hours": return $hours;
            break;
        case "days": return $days;
            break;
        default: // No time unit specified, return the most relevant
            if($seconds &lt; 60) { // Less than a minute has passed
                if($seconds != 1) {
                    $seconds_string .= " seconds ago";
                }
                else {
                    $seconds_string .= " second ago";
                }
                return ($show_unit) ? $seconds_string : $seconds;
            }
            elseif($minutes &lt; 60) { // Less than an hour has passed
                if($minutes != 1) {
                    $minutes_string .= " minutes ago";
                }
                else {
                    $minutes_string .= " minute ago";
                }
                return ($show_unit) ? $minutes_string : $minutes;
                ;
            }
            elseif($hours &lt; 24) { // Less than a day has passed
                if($hours != 1) {
                    $hours_string .= " hours ago";
                }
                else {
                    $hours_string .= " hour ago";
                }
                return ($show_unit) ? $hours_string : $hours;
            }
            else { // More than a day has passed
                if($days != 1) {
                    $days_string .= " days ago";
                }
                else {
                    $days_string .= " day ago";
                }
                return ($show_unit) ? $days_string : $days;
            }
            break;
    }
}
~~~