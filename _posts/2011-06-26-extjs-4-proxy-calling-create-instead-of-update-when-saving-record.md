---
id: 70
title: 'ExtJS 4: Proxy Calling &#8216;Create&#8217; Instead of &#8216;Update&#8217; When Saving Record'
date: 2011-06-26T00:00:41+00:00
author: Levi Hackwith
layout: post
guid: http://levihackwith.com/?p=70
permalink: /extjs-4-proxy-calling-create-instead-of-update-when-saving-record/
categories:
  - Programming / Web Development
tags:
  - ExtJS
  - Lessons Learned
---
Recently, while working with a model and proxy in ExtJS 4, I ran into the issue where the model&#8217;s proxy would call the &#8216;create&#8217; action instead of &#8216;update&#8217; when saving changes to an existing record. <!--more--> Here&#8217;s the sample model and store we&#8217;ll be using to duplicate the problem:

<pre class="brush: jscript; title: ; notranslate" title="">Ext.Loader.setConfig({ // Set up auto-loading
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
            create: 'myBackend.php?action=create', // Called when saving new records
            read: 'data/users.json', // Called when reading existing records
            update: 'myBackend.php?action=update', // Called when updating existing records
            destroy: 'myBackend.php?action=destroy' // Called when deleting existing records
        },
        reader: {
            type: 'json', // We expect the server to give us a JSON string as a response
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
});&lt;/pre&gt;
This is a pretty straightforward example. We have a 'User' model with the following fields: id, name and dob (date of birth) and a store that is tied to that model. Let's load up one of those user objects from the database and try to change the title:
&lt;pre escaped="true" lang="javascript" line="1"&gt;Ext.onReady(function() {
    Ext.widget('userModel').self.load(1, {
        success: function(record, operation) {
            record.data.name = 'Joe Smith';
        }
    })
})
</pre>

Now let&#8217;s try saving our changes and take a peek at the AJAX request sent to the server (via Chrome&#8217;s JavaScript tools console):

**Console Output:**

<pre class="brush: jscript; title: ; notranslate" title="">record.save();
url: http://www.dev.levihackwith.com/dnd_dev/myBackend.php?action=create&amp;_dc=1309112727215
Query String Parameters:
action:create
...
1
As you can a see, our proxy attempted to create the record via the model proxy's 'create' api command instead of update it using the 'update' command. Why is this? Well, let's take a closer look at the record that was returned to us when we called the model's load method:

&lt;a href="http://www.levihackwith.com/wp-content/uploads/2011/06/ScreenClip.png"&gt;&lt;img class="size-full wp-image-72" title="Loaded User Model" src="http://www.levihackwith.com/wp-content/uploads/2011/06/ScreenClip.png" alt="User model returned when save() was called" width="513" height="204" /&gt;&lt;/a&gt;

See the model's "phantom" property? That's been set to true. Let's learn a little more about this property via the API documentation (emphasis mine):
&lt;blockquote&gt;Phantom: Boolean
True when the record does not yet exist in the server-side database (see setDirty). &lt;strong&gt;Any record which has a real database pk [primary key] set as its id property is NOT a phantom&lt;/strong&gt; -- it's real.&lt;/blockquote&gt;
Now, what does that mean, exactly? Well, when you are setting up a model, one of the properties you can set is the idProperty property. This specifies which field in the model serves as the unique identifier for that record when it's sent and received from the server. Now let's take another look at the response from the server:

1
{
    'success': true,
    'users':[{
        'id': '',
        'name': 'John Smith',
        'dob': '1980-06-12'
    }]
}</pre>

<!-- Server response code here -->

See how the ID field is blank? Because it&#8217;s blank, Ext assumes that it&#8217;s not been saved to the database yet and sets the Phantom property to true. Once we adjust our backend code to set the value of the field that acts as the idProperty (in this case, &#8220;id&#8221;), Ext recognizes the record as coming from the server and sets Phantom to false:

So, next time your proxy starts misbehaving, double check your server responses and model configuration and make sure you&#8217;re returning a fully-populated object. Happy coding!