---
title: Reordering List Items using Only CSS
date: 2013-07-03T00:00:27+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
categories:
  - Programming / Web Development
tags:
  - CSS
---
Recently, I&#8217;ve been doing a lot of research into CSS-only dropdown menus; I&#8217;ve found them to be pretty straight-forward (for the most part). One topic I have not been able to find much coverage on is how to rearrange items within the dropdown to give the illusion that the user has selected an item. Where you might use this is in a dropdown menu where the user is able to pick an option that changes how the data is sorted by on the page. Let&#8217;s go ahead and set up an example:

<!--more-->

<pre class="brush: xml; title: ; notranslate" title="">...
    &lt;ul class = "dropdown-menu"&gt;
        &lt;li class = "menu-item"&gt;
            &lt;a href = "#" class = "menu-item-link"&gt;First Name&lt;/a&gt;
        &lt;/li&gt;
        &lt;li class = "menu-item"&gt;
            &lt;a href = "#" class = "menu-item-link"&gt;Last Name&lt;/a&gt;
        &lt;/li&gt;
        &lt;li class = "menu-item active"&gt;
            &lt;a href = "#" class = "menu-item-link"&gt;Age&lt;/a&gt;
        &lt;/li&gt;
        &lt;li class = "menu-item"&gt;
            &lt;a href = "#" class = "menu-item-link"&gt;City&lt;/a&gt;
        &lt;/li&gt;
    &lt;/ul&gt;
    ...
</pre>

And here&#8217;s the CSS to style the menu and set up the dropdown behavior:

<pre class="brush: css; title: ; notranslate" title="">.dropdown-menu {
    padding: 0;
    margin: 0;
    width: 130px;
    font-family: Arial;
    display: table;
    position: relative;
    border: solid 1px #CCCCCC;
    border-bottom-style: none;
    background-color: #F4F4F4;
}

/* Hide all menu items by default */
.dropdown-menu .menu-item {
    display: none;
}

.dropdown-menu .menu-item-link {
    display: table-cell;
    border-bottom: solid 1px #CCCCCC;
    text-decoration: none;
    color: rgba(89,87,87,0.9);
    height: 30px;
    padding: 5px;
    vertical-align: middle;
    cursor: pointer;
}

/* Prevents double borders */
.dropdown-menu:hover .menu-item {
    border-bottom-style: solid;
}

/* The hover effect on each item */
.dropdown-menu .menu-item-link:hover {
    background-color: #DDDDDD;
}

/* On mouseover, show all the menu items */
.dropdown-menu:hover .menu-item {
    display: table-row;
}

/* Force the active menu item to the top */
.dropdown-menu .menu-item.active {
    display: table-header-group;
}

/* Add the triangle to the dropdown menu */
.dropdown-menu .menu-item.active .menu-item-link:after {
	width: 0;
	height: 0;
	content: "";
	position: absolute;
	top: 12px;
	right: 8px;
	border-top: 4px solid rgba(0, 0, 0, 1);
	border-left: 4px solid transparent;
	border-right: 4px solid transparent;

}
</pre>

Now, a good majority of this stuff is simply for styling the table but I do want to point out a few things. For starters, you&#8217;ll notice that I&#8217;ve set the display of the `<ul>` to `table` and all the `<li>` tags are table-rows. This not only helps with vertically centering the text in each menu item, but it also allows me to set the active menu item to display as a table header. If you remember, HTML headers (`<thead>`) always show up at the top of the table regardless of where they are in the HTML. By setting the active `<li>` to display like a table header, we guarantee that it will always remain at the top of the list visually regardless of where it is declared in the HTML.

<pre class="brush: css; title: ; notranslate" title="">...
/* Force the active menu item to the top */
.dropdown-menu .menu-item.active {
    display: table-header-group;
}
...
</pre>

## Demo

If you&#8217;d like to see the menu in action, you can checkout this [JsFiddle](http://jsfiddle.net/OpnSrce/k882f/) I put together.