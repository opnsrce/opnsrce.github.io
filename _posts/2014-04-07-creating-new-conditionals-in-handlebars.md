---
id: 334
title: Creating New Conditionals in Handlebars
date: 2014-04-07T00:00:46+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=334
permalink: /creating-new-conditionals-in-handlebars/
icy_video_embed_code:
  - 
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - handlebars
  - JavaScript
---
If you work with Handlebars long enough, you&#8217;ll start to notice a very annoying gap in its capabilities: conditionals. Now, Handlebars does come with a conditionals helper that simply tests whether or not the passed in value is truthy or not and acts accordingly. While this is fine for a good portion of scenarios, I guarantee there will come a time where you need a more robust solution. Today, we&#8217;re going to go over three conditional helpers that handlebars is lacking and how to make them yourself.

## EqualTo

<pre class="brush: jscript; title: ; notranslate" title="">Handlebars.registerHelper('ifequal', function(value1, value2, options) {
  if(value1 === value2) {
    return options.fn(this);
  }
  return options.inverse(this);
});
</pre>

## LessThan and LessThanOrEqual

<pre class="brush: jscript; title: ; notranslate" title="">Handlebars.registerHelper('iflessthan', function(value1, value2, options) {
  if(value1 &lt; value2) {
    return options.fn(this);
  }
  return options.inverse(this);
});
</pre>

<pre class="brush: jscript; title: ; notranslate" title="">Handlebars.registerHelper('iflessthanorequal', function(value1, value2, options) {
  if(value1 &lt;= value2) {
    return options.fn(this);
  }
  return options.inverse(this);
});
</pre>

If you need additional functionality (e.g., greater-than-or-eaual-to or not-equal-to), you can easily figure out what needs to be done given the examples provided. If you don&#8217;t feel like creating individual helpers for each kind of conditional, I found <a href = "http://stackoverflow.com/a/16315366" target = "_blank">this</a> really cool snippet on StackOverflow that may come in handy:

<pre class="brush: jscript; title: ; notranslate" title="">Handlebars.registerHelper('ifCond', function (v1, operator, v2, options) {

    switch (operator) {
        case '==':
            return (v1 == v2) ? options.fn(this) : options.inverse(this);
        case '===':
            return (v1 === v2) ? options.fn(this) : options.inverse(this);
        case '&lt;':
            return (v1 &lt; v2) ? options.fn(this) : options.inverse(this);
        case '&lt;=':
            return (v1 &lt;= v2) ? options.fn(this) : options.inverse(this);
        case '&gt;':
            return (v1 &gt; v2) ? options.fn(this) : options.inverse(this);
        case '&gt;=':
            return (v1 &gt;= v2) ? options.fn(this) : options.inverse(this);
        case '&&':
            return (v1 && v2) ? options.fn(this) : options.inverse(this);
        case '||':
            return (v1 || v2) ? options.fn(this) : options.inverse(this);
        default:
            return options.inverse(this);
    }
});
</pre>

You use it like this:

<pre class="brush: jscript; title: ; notranslate" title="">{{#ifCond var1 '==' var2}}
</pre>