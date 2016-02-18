---
id: 107
title: 'ExtJS 4: Passing Filters Between a Grid and a Chart Store'
date: 2011-10-02T16:16:42+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=107
permalink: /extjs-4-passing-filters-between-a-grid-and-a-chart-store/
icy_video_embed_code:
  - 
categories:
  - Programming / Web Development
tags:
  - Charting
  - ExtJS
  - filtering
  - stores
---
In preparation for another round of Envato screencasts, I&#8217;ve been messing around with the new Charting API that comes with ExtJS 4. For this project, I wanted to show how you can filter a grid full of data and have it change the data in the pie chart. Unfortunately, I soon discovered that pie charts (or rather, charts in general) and data grids take two different types of data. 

<!--more-->

For example: here&#8217;s the JSON response for the store that runs my pie chart:

<pre class="brush: jscript; title: ; notranslate" title="">[
    {
        "favorite_color": "blue",
        "total": "48",
        "percentage": "12"
    },
    {
        "favorite_color": "green",
        "total": "53",
        "percentage": "13"
    },
    {
        "favorite_color": "orange",
        "total": "56",
        "percentage": "14"
    },
    {
        "favorite_color": "pink",
        "total": "59",
        "percentage": "15"
    },
    {
        "favorite_color": "red",
        "total": "38",
        "percentage": "10"
    },
    {
        "favorite_color": "violet",
        "total": "45",
        "percentage": "11"
    },
    {
        "favorite_color": "yellow",
        "total": "101",
        "percentage": "25"
    }
]
</pre>

For a pie chart, your store needs to have two main things: a field that the pie chart&#8217;s labeling system will use (e.g., &#8216;favorite_color&#8217;) and a field that the pie chart&#8217;s series will use (e.g., &#8216;total&#8217;). As you can see from the feature image, the pie chart uses the `favorite_color` and `total` fields to display the data in the correct proportions. Now let&#8217;s look at a single record from the JSON response for the data grid: 

<pre class="brush: jscript; title: ; notranslate" title="">{
        "id": "50",
        "first_name": "Wynne",
        "last_name": "Aguilar",
        "age": "94",
        "gender": "2",
        "hair_color": "Other",
        "eye_color": "Hazel",
        "state": "ND",
        "favorite_color": "yellow",
        "car_model": "Toyota",
        "housing_type": "Mobile Home",
        "marriage_status": "Single",
        "has_pets": "1",
        "num_children": "10"
    }
</pre>

As you can see from the drastic difference between the two data stores, if we tried to power the grid and the pie chart from the same store, neither would render correctly; the pie chart wouldn&#8217;t have a field to calculate it&#8217;s segment sizes with and the grid wouldn&#8217;t have any of the fields it&#8217;s expecting through the column model. Long story short, there&#8217;s no way to tie the grid&#8217;s data to the pie chart (or vice versa) without causing serious issues. 

To get around this limitation, we need to simultaneously filter both stores at the same time. Here&#8217;s the controller for both the grid and the pie chart: 

<pre class="brush: jscript; title: ; notranslate" title="">Ext.define('App.controller.People', {
    extend: 'Ext.app.Controller',
    models: [
        'Person',
    ],
    stores: [
        'people.People',
        'people.FavoriteColorCounts'
    ],
    views:[
        'person.Grid',
        'chart.FavoriteColorPieChart'
    ],
    refs: [{
        ref: 'favoriteColorPieChart', 
        selector: 'favoritecolorpiechart'
    }, {
        ref: 'personGrid',
        selector: 'persongrid'
    }],        
    init: function() {
        this.getPeoplePeopleStore().on(
            'load',
            function(store, records, successful, operation, options) {
                var filters;
                var gridFilterFeature = this.getPersonGrid().filters;
                    filters = gridFilterFeature.buildQuery(gridFilterFeature.getFilterData());
                this.getPeopleFavoriteColorCountsStore().load({
                   params: {
                       filter: filters
                   }
                });
            },
            this
        )
        this.callParent(arguments)
    }
});
</pre>

There&#8217;s a lot going on there, but we really need to only focus on the `init` method: 

<pre class="brush: jscript; title: ; notranslate" title="">...
    init: function() {
        this.getPeoplePeopleStore().on(
            'load',
            function(store, records, successful, operation, options) {
                var filters;
                var gridFilterFeature = this.getPersonGrid().filters;
                    filters = gridFilterFeature.buildQuery(gridFilterFeature.getFilterData());
                this.getPeopleFavoriteColorCountsStore().load({
                   params: {
                       filter: filters
                   }
                });
            },
            this
        )
        this.callParent(arguments)
    }
</pre>

Let&#8217;s break it down: 

<pre class="brush: jscript; title: ; notranslate" title="">...
        this.getPeoplePeopleStore().on(
            'load',
            function(store, records, successful, operation, options) {
...
</pre>

Here, we&#8217;re adding a listener to the `load` event of the `people.People` store.

<pre class="brush: jscript; title: ; notranslate" title="">...
          var filters;
          var gridFilterFeature = this.getPersonGrid().filters;
          filters = gridFilterFeature.buildQuery(gridFilterFeature.getFilterData());
          this.getPeopleFavoriteColorCountsStore().load({
              params: {
                  filter: filters
              }
...
</pre>

Here, we&#8217;re grabbing the filters from the grid we want to use on the pie chart&#8217;s store, rebuilding them into a JSON string using `buildQuery` and then reloading the pie chart&#8217;s store while passing in the filters. 

Well, I hope that helps someone out because God knows I wasted fours of my life figuring it out.