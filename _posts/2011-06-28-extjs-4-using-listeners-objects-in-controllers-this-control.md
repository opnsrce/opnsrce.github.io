---
title: 'ExtJS 4: Using Listeners objects in Controllers (this.control)'
date: 2011-06-28T21:46:24+00:00
author: Levi Hackwith
layout: post
code: true
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - Controller
  - ExtJS
  - Listener
  - MVC
---

[1]: http://docs.sencha.com/ext-js/4-0/#/api/Ext.form.Panel-method-addListener

When setting up a controller in ExtJS 4, you might do something like this:

~~~js
Ext.define('app.controller.myController', {
    init: function() {
        this.control({
            'form &gt; textfield': {
                change: this.textFieldChange
            }
        })
    },
    textFieldChange: function(textField, newValue, oldValue, options) {
      alert('The text box went from' + oldValue + ' to ' + newValue);
    }
});
~~~

What this code is saying is &ldquo;Find every textfield inside of the form in
the current view (usually the viewport) and, whenever the value changes, fire
the ``textFieldChange()`` method.&rdquo; Now, this is fine and all, but what
if your ``textFieldChange()`` method sent a request to the server? That would
mean that, for every character you typed, a new request would be created and
sent to the server causing a lot of unnecessary overhead.

The best solution would be to use the ``buffer`` property of the event
[listener object][1] to delay the request until we&rsquo;re finished typing.
Here&rsquo;s how you go about declaring additional properties of an event
listener from inside the controller:

~~~js
Ext.define('app.controller.myController', {
    init: function() {
        this.control({
            'form &gt; textfield': {
                change: {
                    fn: this.textFieldChange,
                    buffer: 500 // Delay the request by half a second
                 }
            }
        })
    },
    textFieldChange: function(textField, newValue, oldValue, options) {
      alert('The text box went from' + oldValue + ' to ' + newValue);
    }
});
~~~

Hope somebody out there finds this as helpful as I did. Happy coding!