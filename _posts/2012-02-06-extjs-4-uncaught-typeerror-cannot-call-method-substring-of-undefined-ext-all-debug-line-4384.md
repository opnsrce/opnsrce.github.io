---
title: 'ExtJS 4: Uncaught TypeError: Cannot call method &#8216;substring&#8217; of undefined ext-all-debug line 4384'
date: 2012-02-06T00:00:13+00:00
author: Levi Hackwith
layout: post
categories:
  - Programming / Web Development
tags:
  - Bugs
  - ExtJS
  - JavaScript
  - Lessons Learned
---
When working with ExtJS 4, you&#8217;ll often run into ambiguous error message like this one:

> Uncaught TypeError: Cannot call method &#8216;substring&#8217; of undefined

 <cite>ext-all-debug.js line 4384</cite>

I recently ran into this while coding up an Ext application for another blog post, and I thought I&#8217;d share with you its root cause and solution.

<!--more-->

If you head straight to the line number in question, you&#8217;ll find yourself somewhere in the middle of the `parseNamespace` method of Ext&#8217;s ClassManager object and you&#8217;ll notice that the parameter that the method expects (`namespace`) is undefined, causing the method to throw an error. However if you look a little deeper in the callstack, you&#8217;ll notice that the `instantiateByAlias` method was called just before `parseNamespace`:.

<pre class="brush: jscript; title: ; notranslate" title="">instantiateByAlias: function() {
    var alias = arguments[0],
        args = arraySlice.call(arguments),
        className = this.getNameByAlias(alias);

    if (!className) {
        className = this.maps.aliasToName[alias];

        Ext.syncRequire(className);
    }

    args[0] = className;

    return this.instantiate.apply(this, args);
}
</pre>

If you place a breakpoint in this method and run the application again, you&#8217;ll be able to watch it load each Ext class (as well as your application&#8217;s custom components) by its xtype alias. Eventually, it attempt to load one of your application&#8217;s classes and then crash.

The reason for this crash is because you&#8217;ve most likely misspelled the alias of that component while referencing it in another component. Take a look at my grid code:

<pre class="brush: jscript; title: ; notranslate" title="">Ext.define('App.view.person.Grid', {
    extend: 'Ext.grid.Panel',
    alias: 'widget.persongrid',
    title: 'People',
    columns: [{
        header: 'ID',
        dataIndex: 'id'
    }, {
        header: 'First Name',
        dataIndex: 'first_name'
    }, {
        header: 'Last Name',
        dataIndex: 'last_name'
    }, {
        header: 'Address',
        dataIndex: 'address'
    }, {
        header: 'City',
        dataIndex: 'city'
    }, {
        header: 'State',
        dataIndex: 'state'
    }, {
        header: 'Zip Code',
        dataIndex: 'zip_code'
    }]
});
</pre>

Now take a look at my viewport code:

<pre class="brush: jscript; title: ; notranslate" title="">Ext.define('App.view.Viewport', {
    extend: 'Ext.container.Viewport',
    config: {
        items: [{
            xtype: 'peoplegrid',
            store: 'People'
        }]
    }
});
</pre>

See how I referenced my Person grid view by the alias `peoplegrid` in the viewport file but I declared the alias to be `persongrid` in the grid file? That&#8217;s what&#8217;s causing the JavaScript error. So, the moral of the story is: If you get obscure errors about strings being undefined in ExtJS 4, _always_ check deeper in the callstack (not just the line-number in question) and _always_ double-check your xtype aliases across your application.

Hope this helps.