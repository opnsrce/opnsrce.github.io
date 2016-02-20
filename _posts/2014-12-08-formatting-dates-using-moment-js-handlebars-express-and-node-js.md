---
id: 362
title: Formatting Dates Using Moment.js, Handlebars, Express, and Node.js
date: 2014-12-08T00:00:26+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=362
permalink: /formatting-dates-using-moment-js-handlebars-express-and-node-js/
categories:
    - Code Snippets
    - Programming / Web Development
tags:
    - express
    - handlebars
    - momentjs
    - node.js
---

[1]: https://www.npmjs.org/package/express3-handlebars
[2]:http://momentjs.com/

For those of you out there that may be struggling with this, here&rsquo;s a
quick breakdown of how to format dates using moment.js, handlebars, express,
and node.js. This post assumes you have the following packages installed in
your express app:

1. Express3 Handlebars ([link][1])
2. Moment.js ([link][2])

Once you&rsquo;ve included these packages in your ``app.js`` file, you&rsquo;ll
need to set up handlebars like so:
<!--more-->

~~~js
...
app = express();
hbsEngine = expressHbs.create({
    extname: 'hbs',
    defaultLayout: 'layout.hbs',
    helpers: {
        formatDate: function (date, format) {
            return moment(date).format(format);
        }
    }
});

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.engine('hbs', hbsEngine.engine);
app.set('view engine', 'hbs');
...
~~~

You can ignore the ``extname`` and ``defaultLayout`` configs incase you want
to use the default values that handlebars sets for you for the extension and
layout file name. The important thing to note is the ``helpers`` object.
Basically, it&rsquo;s the equivalent of the ``registerHelpers`` method in the
JS version of Handlebars. In this example, I&rsquo;m create a ``formatDate``
method that takes in a ``date`` and ``format`` string and returns a formatted
date via moment.js.