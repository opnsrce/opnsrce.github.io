---
title: 'ExtJS 4: Proxy Calling Create Instead of Update When Saving Record'
date: 2011-06-26T00:00:41+00:00
author: Levi Hackwith
layout: post
code: true
permalink: /extjs-4-proxy-calling-create-instead-of-update-when-saving-record/
categories:
  - Programming / Web Development
tags:
  - ExtJS
  - Lessons Learned
---

[1]: /images/posts/{{ page.permalink }}/console.png

Recently, while working with a model and proxy in ExtJS 4, I ran into the
issue where the model&rsquo;s proxy would call the ``create`` action instead
of ``update`` when saving changes to an existing record. Here&rsquo;s
the sample model and store we&rsquo;ll be using to duplicate the problem:
<!--more-->

~~~js
Ext.Loader.setConfig({ // Set up auto-loading
    enabled: true,
    paths: {
        Ext: 'extjs/src'
    }
});
Ext.define('User', { // The store
    alias: 'widget.userModel',
    extend: 'Ext.data.Model',
    idProperty: 'id',
    fields: [{
        name: 'id',
        type: 'int'
    }, {
        name: 'name',
        type: 'string'
    }, {
        name: 'dob',
        type: 'date',
        dateFormat: 'Y-m-d'
    }],
    proxy: {
        type: 'ajax',
        api: {
            // Called when saving new records
            create: 'myBackend.php?action=create',
            // Called when reading existing records
            read: 'data/users.json',
            // Called when updating existing records
            update: 'myBackend.php?action=update',
            // Called when deleting existing records
            destroy: 'myBackend.php?action=destroy'
        },
        reader: {
            // We expect the server to give us a JSON string as a response
            type: 'json',
            root: 'users'
        }
    }
})

Ext.define('Users', {
    extend: 'Ext.data.Store',
    alias: 'widget.userStore',
    model: 'User',
    autoLoad: false,
    autoSync: true
});
~~~

This is a pretty straightforward example. We have a ``User`` model with the
an ``id``, ``name``, and ``dob`` (date of birth) and a store that is tied to
that model. Let's load up one of those user objects from the database and try
to change the title:

~~~js
Ext.onReady(function() {
    Ext.widget('userModel').self.load(1, {
        success: function(record, operation) {
            record.data.name = 'Joe Smith';
        }
    })
})
~~~

Now let&rsquo;s try saving our changes and take a peek at the AJAX request
sent to the server (via Chrome&rsquo;s JavaScript tools console):

~~~
**Console Output:**

record.save();
url: http://www.dev.levihackwith.com/dnd_dev/myBackend.php? \
    action=create&_dc=1309112727215
Query String Parameters:
action:create
...
~~~
As you can a see, our proxy attempted to create the record via the model
proxy's ```create`` api command instead of update it using the 'update'
command. Why is this? Well, let's take a closer look at the record that was
returned to us when we called the model's load method:

![][1]

See the model's "phantom" property? That's been set to true. Let's learn a
little more about this property via the API documentation (emphasis mine):

> Phantom: Boolean
>
> True when the record does not yet exist in the server-side database
> (see setDirty). __Any record which has a real database pk [primary key] set as
> its id property is NOT a phantom__ -- it's real.

Now, what does that mean, exactly? Well, when you are setting up a model,
one of the properties you can set is the idProperty property. This specifies
which field in the model serves as the unique identifier for that record when
it's sent and received from the server. Now let's take another look at the
response from the server:

~~~js
{
    'success': true,
    'users':[{
        'id': '',
        'name': 'John Smith',
        'dob': '1980-06-12'
    }]
}
~~~

See how the ID field is blank? Because it&rsquo;s blank, Ext assumes that
it&rsquo;s not been saved to the database yet and sets the Phantom property to
``true``. Once we adjust our backend code to set the value of the field that
acts as the idProperty (in this case, ``id``), Ext recognizes the record as
coming from the server and sets Phantom to ``false``

So, next time your proxy starts misbehaving, double check your server
responses and model configuration and make sure you&rsquo;re returning a
fully-populated object. Happy coding!