---
title: Creating New Conditionals in Handlebars
date: 2014-04-07T00:00:46+00:00
author: Levi Hackwith
layout: post
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - handlebars
  - JavaScript
---

[1]: http://stackoverflow.com/a/16315366

If you work with Handlebars long enough, you&rsquo;ll start to notice a very
annoying gap in its capabilities: conditionals. Now, Handlebars does come
with a conditionals helper that simply tests whether or not the passed in
value is truthy or not and acts accordingly. While this is fine for a good
portion of scenarios, I guarantee there will come a time where you need a
more robust solution. Today, we&rsquo;re going to go over three conditional
helpers that handlebars is lacking and how to make them yourself.
<!--more-->

# EqualTo

~~~js
Handlebars.registerHelper('ifequal', function(value1, value2, options) {
    if(value1 === value2) {
        return options.fn(this);
    }
    return options.inverse(this);
});
~~~

# LessThan and LessThanOrEqual

~~~js
Handlebars.registerHelper('iflessthan', function(value1, value2, options) {
    if(value1 < value2) {
        return options.fn(this);
    }
    return options.inverse(this);
});
~~~

~~~js
Handlebars.registerHelper('iflessthanorequal',
    function(value1, value2, options) {
        if(value1 <= value2) {
            return options.fn(this);
        }
        return options.inverse(this);
    }
);
~~~

If you need additional functionality (e.g., greater-than-or-eaual-to or
not-equal-to), you can easily figure out what needs to be done given the
examples provided. If you don&rsquo;t feel like creating individual helpers
for each kind of conditional, I found [this][1] really cool snippet on
StackOverflow that may come in handy:

~~~js
Handlebars.registerHelper('ifCond', function (v1, operator, v2, options) {
    switch (operator) {
        case '==':
            return (v1 == v2) ? options.fn(this) : options.inverse(this);
        case '===':
            return (v1 === v2) ? options.fn(this) : options.inverse(this);
        case '<':
            return (v1 < v2) ? options.fn(this) : options.inverse(this);
        case '<=':
            return (v1 <= v2) ? options.fn(this) : options.inverse(this);
        case '>':
            return (v1 > v2) ? options.fn(this) : options.inverse(this);
        case '>=':
            return (v1 >= v2) ? options.fn(this) : options.inverse(this);
        case '&&':
            return (v1 && v2) ? options.fn(this) : options.inverse(this);
        case '||':
            return (v1 || v2) ? options.fn(this) : options.inverse(this);
        default:
            return options.inverse(this);
    }
});
~~~

You use it like this:

~~~js
{#ifCond var1 '==' var2}}
~~~