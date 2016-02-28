---
title: 'Using Handlebars &#8220;Each&#8221; Blocks with Backbone Collections / Templates'
date: 2013-07-22T07:56:20+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
dsq_thread_id:
  - 4586109494
categories:
  - Programming / Web Development
tags:
  - Backbone.js
  - JavaScript
  - templates
---
A while back I took Code School&#8217;s amazing <a href="http://www.codeschool.com/courses/anatomy-of-backbonejs" target="_blank">course on Backbone.js</a>. In one of the slides, I found this block of code:

<pre class="brush: jscript; title: ; notranslate" title="">var TodoListView = Backbone.View.extend({
  initialize: function(){
    this.collection.on('add', this.addOne, this);
    this.collection.on('reset', this.addAll, this);
  },
  addOne: function(todoItem){
    var todoView = new TodoView({model: todoItem});
    this.$el.append(todoView.render().el);
  },
  addAll: function(){
    this.collection.forEach(this.addOne, this);
￼  },
  render: function(){
    this.addAll();
  }
});
</pre>

For the most part, it&#8217;s pretty straight forward. Basically, they are calling the `addOne` method and passing in the model they want to add to the list view. In the context of the lesson, they were trying to show how you might go about looping through a collection of items and adding them to a list while avoiding issues related to scope.

<!--more-->

While I found the entire lesson to be extremely helpful, I found this bit of code to be rather, well, odd. I began to ask myself &#8220;Why don&#8217;t they just use an `{{each}}` block and loop through the todo list collection that way?&#8221;

## Collection Expectations VS Handlebars Expectations

Initially, I thought you could simple load the handlebars template and the collection with the same JSON data. Something like this:

<pre class="brush: jscript; title: ; notranslate" title="">// The data
var studentFixtures = {
    students: [{
        "id": 1,
        "firstName": "Santiago",
        "lastName": "Hart",
        "picture": "",
        "age": 19,
        "grade": 9
    }, {
        "id": 2,
        "firstName": "Reynolds",
        "lastName": "Caldwell",
        "picture": "",
        "age": 14,
        "grade": 9
    }, {
        "id": 3,
        "firstName": "Lloyd",
        "lastName": "Mcdonald",
        "picture": "",
        "age": 18,
        "grade": 11
    }, {
        "id": 4,
        "firstName": "Arlene",
        "lastName": "Carney",
        "picture": "",
        "age": 14,
        "grade": 11
    }, {
        "id": 5,
        "firstName": "Mae",
        "lastName": "Hensley",
        "picture": "",
        "age": 16,
        "grade": 12
    }, {
        "id": 6,
        "firstName": "Haynes",
        "lastName": "Delacruz",
        "picture": "",
        "age": 20,
        "grade": 10
    }]
};
</pre>

<pre class="brush: jscript; title: ; notranslate" title="">...
// The Collection
this.studentCollection = new Students();
this.studentCollection.reset(studentFixtures.students); // Load the collection with data
this.studentListView = new StudentListView({
    collection: this.studentCollection
});
...
</pre>

And then do something similar for the template / view:

<pre class="brush: jscript; title: ; notranslate" title="">var StudentListView = Backbone.View.extend({
    template: Handlebars.compile($('#student-list-template').html()),
    render: function() {
        this.$el.html(this.template(this.collection.toJSON()));
        $('#main-container').append(this.$el);
    }
});
</pre>

The trouble with this approach is the fact that Handlebars and Backbone collections expect their data in two different formats: Handlebars expects an object with a property whose value is an array of objects, and the collection just wants an array of objects.

To remedy this, we need to wrap the array of data sent to the Handlebars template in an object that has the property the template is expecting:

<pre class="brush: jscript; title: ; notranslate" title="">var StudentListView = Backbone.View.extend({
    template: Handlebars.compile($('#student-list-template').html()),
    events: {
        "click a": function(e) {
            e.preventDefault();
            alert('clicked');
        }
    },
    render: function() {
        console.log(this.template({students:this.collection.toJSON()}));
        this.$el.html(this.template({students:this.collection.toJSON()}));
        $('#main-container').append(this.$el);
    }
});
</pre>

Hopefully this helps someone else out. If you have any questions, please leave a comment below.