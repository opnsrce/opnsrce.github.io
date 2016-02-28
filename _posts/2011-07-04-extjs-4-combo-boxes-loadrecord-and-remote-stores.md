---
title: 'ExtJS 4: Combo Boxes, loadRecord() and Remote Stores'
date: 2011-07-04T00:00:38+00:00
author: Levi Hackwith
layout: post
code: true
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - Bugs
  - combo box
  - ExtJS
  - override
  - stores
---

[1]: https://github.com/opnsrce/Code-Snippets/commit/96847c4b5177fc49bacba6aa1716b88accdb2082#diff-0

A while back I ran into an interesting issue regarding loading records from
the database into a form that contained combo boxes driven by remote stores.
The problem was, when the record got loaded into the form, the stores for the
combo boxes hadn&&rsquo;t loaded, so all the combo boxes said &ldquo;select
one&rdquo;instead of the option that was chosen when the form got submitted.
After doing some digging, I came up with a way around this issue:

<!--more-->

## The Override Code

~~~js
Ext.form.field.ComboBox.override( {
    setValue: function(v) {
        v = (v &amp;&amp; v.toString) ? v.toString() : v;
        if(!this.store.isLoaded &amp;&amp; this.queryMode == 'remote') {
            this.store.addListener('load', function() {
                this.store.isLoaded = true;
                this.setValue(v);
            }, this);
           this.store.load();
        } else {
            this.callOverridden(arguments);
        }
    }
});
~~~

Here, we override the ``setValue()`` method of the ``ComboBox`` component and do
the following:

  1. Make sure the store is not yet loaded (a custom property I added) and
  that it is tied to a remote store.
  2. Add a listener to the &#8216;load&&rsquo; event. When the store is loaded,
  set ``isLoaded`` equal to ``true`` and call ``setValue()`` again.
  3. Load the store
  4. If the store is already loaded or the store is local, call the original
  overridden ``setValue()`` method

Just drop this into whatever JS file you keep your other overrides in and
you&&rsquo;ll be good to go. Happy coding!

__Update:__ The source code for this snippet is available [here][1].