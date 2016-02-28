---
title: Roll Your Own Dropdown Menu Using Pure CSS
date: 2013-07-01T00:00:03+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
dsq_thread_id:
  - 4586109596
categories:
  - Programming / Web Development
tags:
  - CSS
  - Dropdown
---
There&#8217;s a lot of tutorials out there for creating dropdown menus using Only CSS. However, I haven&#8217;t really found one that breaks down the development process in order to teach it instead of just providing an explanation of code you&#8217;re meant to copy and paste. Here I hope to explain just how CSS dropdown menus work and go over the process I used to develop the one I use on my projects.

<!--more-->

## Start With a Good Foundation: The Markup

The most important step when developing something like this is making sure the markup is clean and semantically correct. If you get this step wrong, you&#8217;re going to have a more difficult time trying to style it properly later. Here&#8217;s the markup I&#8217;ve chosen to use for this project:

<pre class="brush: xml; title: ; notranslate" title="">&lt;ul&gt;
    &lt;li&gt;&lt;a href="#"&gt;Item 1&lt;/a&gt;&lt;/li&gt;
    &lt;li&gt;&lt;a href="#"&gt;Item 2&lt;/a&gt;&lt;/li&gt;
    &lt;li&gt;&lt;a href="#"&gt;Item 3&lt;/a&gt;&lt;/li&gt;
    &lt;li&gt;&lt;a href="#"&gt;Item 4&lt;/a&gt;&lt;/li&gt;
    &lt;li&gt;&lt;a href="#"&gt;Item 5&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
</pre>

Here we&#8217;ve created a very simple unordered list that contains links that refer back to the page itself: pretty standard stuff. What makes this markup so suited for a dropdown menu is the fact that an dropdown menu is technically just a list of items, each one designed to signify a choice or action that user can take.

## Add the Proper Hooks: Classes

Now that we&#8217;ve got our markup figured out, it&#8217;s time to add some CSS styles to it.

<pre class="brush: xml; title: ; notranslate" title="">&lt;ul class="dropdown-menu"&gt;
    &lt;li class="menu-item"&gt;
        &lt;a class="menu-item-link" href="#"&gt;Item 1&lt;/a&gt;
    &lt;/li&gt;
    &lt;li class="menu-item"&gt;
        &lt;a class="menu-item-link" href="#"&gt;Item 2&lt;/a&gt;
    &lt;/li&gt;
    &lt;li class="menu-item"&gt;
        &lt;a class="menu-item-link" href="#"&gt;Item 3&lt;/a&gt;
    &lt;/li&gt;
    &lt;li class="menu-item"&gt;
        &lt;a class="menu-item-link" href="#"&gt;Item 4&lt;/a&gt;
    &lt;/li&gt;
    &lt;li class="menu-item"&gt;
        &lt;a class="menu-item-link" href="#"&gt;Item 5&lt;/a&gt;
    &lt;/li&gt;
&lt;/ul&gt;
</pre>

Most of the classes here are pretty self explanatory: their names reflect the function of the elements they&#8217;re meant to style.

With the addition of the class names to the elements, we can now start applying styles to the menu.

## Style the Menu

Let&#8217;s apply the following styles to the dropdown menu:

<pre class="brush: css; title: ; notranslate" title="">.dropdown-menu {
    padding: 0;
    margin: 0;
    width: 130px;
    font-family: Arial;
    display: block;
    border: solid 1px #CCCCCC;
    border-bottom-style: none;
    background-color: #F4F4F4;
}
.dropdown-menu .menu-item-link {
    display: block;
    border-bottom: solid 1px #CCCCCC;
    text-decoration: none;
    line-height: 30px; /* Vertically center the text */
    color: rgba(89,87,87,0.9);
    height: 30px;
    padding: 5px;
    cursor: pointer;
}
</pre>

If you&#8217;re familiar with CSS, most of the code here is pretty self explanatory. Once you&#8217;ve applied the styles, you should get something that looks like this:

[<img src="http://www.levihackwith.com/wp-content/uploads/2013/06/dropdown-menu-step-1.png" alt="dropdown-menu-step-1" width="169" height="260" class="aligncenter size-full wp-image-308" />](http://www.levihackwith.com/wp-content/uploads/2013/06/dropdown-menu-step-1.png)

## Hide and Hover: Making the Menu Drop Down

With the markup and basic styles now in place, we now have our selves a very nice static menu. However, the goal of the project is to create a _drop down_ menu which means we&#8217;re going to need a way to show and hide the list items not at the top of the list.

To start off, we&#8217;re going to need to modify our markup and add an &#8220;`active`&#8221; class to the first element in the list so we know which list item we want to keep visible. Go ahead and update markup to look like the following:

<pre class="brush: xml; title: ; notranslate" title="">&lt;ul class="dropdown-menu"&gt;
    &lt;li class="menu-item active"&gt; &lt;!-- Add active class --&gt;
        &lt;a class="menu-item-link" href="#"&gt;Item 1&lt;/a&gt;
    &lt;/li&gt;
    &lt;li class="menu-item"&gt;
        &lt;a class="menu-item-link" href="#"&gt;Item 2&lt;/a&gt;
    &lt;/li&gt;
    &lt;li class="menu-item"&gt;
        &lt;a class="menu-item-link" href="#"&gt;Item 3&lt;/a&gt;
    &lt;/li&gt;
    &lt;li class="menu-item"&gt;
        &lt;a class="menu-item-link" href="#"&gt;Item 4&lt;/a&gt;
    &lt;/li&gt;
    &lt;li class="menu-item"&gt;
        &lt;a class="menu-item-link" href="#"&gt;Item 5&lt;/a&gt;
    &lt;/li&gt;
&lt;/ul&gt;
</pre>

Now we need to update our CSS to both hide the &#8220;inactive&#8221; list items (those without the `active` class) and make sure we keep the active list item visible. Go ahead and add the following rules to your CSS:

<pre class="brush: css; title: ; notranslate" title="">.dropdown-menu .menu-item {
    display: none;
}

.dropdown-menu .menu-item.active {
    display: block;
}

.dropdown-menu:hover .menu-item {
    display: block;
}

</pre>

Now, the above css might be a bit confusing (especially with the use of the `:hover` pseudo-selectors), so I&#8217;ll treat each one as part of a series and go through them step-by-step:

  1. Hide every menu item that is part of the `dropdown-menu` list.
  2. For every menu item with a class of `active`, override the display rule from step one and show them as a block-level element.
  3. Whenever the `dropdown-menu` is moused over, find every element with a class of `list-item` and display it as a block-level element.

## Finishing Touches: Hover Effects and an Arrow &#8220;Icon&#8221;

Okay, so we&#8217;ve now got our dropdown menu showing and hiding the on mouse over. Before we call this thing finished, let&#8217;s go ahead and add some finishing touches to make the final product a bit more polished.

First, let&#8217;s add a hover effect to each of the dropdown elements. This is not only a nice design touch, it also helps indicate which item the user is currently hovered over. In order to do this, we simply need to add another `:hover` selector rule to our CSS:

<pre class="brush: css; title: ; notranslate" title="">.dropdown-menu .menu-item-link:hover {
    background-color: #DDDDDD;
}
</pre>

Once you add that to the code, you&#8217;ll notice that the background color of each menu item you mouse over darkens.

Now, we&#8217;re going to add a cool little down arrow to the right of the active menu item. Traditionally, we&#8217;d use some kind of <span> tag with its `background-image` property set to the location of an arrow icon we created. With this tutorial being about using _only_ CSS to create our dropdown menu, we&#8217;re going to instead use the `:after` selector and the `:content` property to create our &#8220;icon&#8221; on the fly using code I learned from Chris Coyier over at <a href="http://css-tricks.com/snippets/css/css-triangle/" target="_blank">CSS tricks</a>. Add the following rule to your stylesheet:

<pre class="brush: css; title: ; notranslate" title="">.dropdown-menu .menu-item.active .menu-item-link:after {
    width: 0;
    height: 0;
    content: "";
    position: absolute;
    top: 18px;
    right: 8px;
    border-top: 4px solid rgba(0, 0, 0, 1);
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
}
</pre>

Now before you starting mumbling _WTF_ at your screen, let me explain what&#8217;s going on here.

The first thing I want to cover is the `:after selector`. If you&#8217;ve never encountered this one before, the best definition I&#8217;ve found is from the [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/CSS/::after):

> The CSS :after pseudo-element matches a virtual last child of the selected element. Typically used to add cosmetic content to an element, by using the content CSS property. This element is inline by default.

By using the `:after` selector along with the `:content` property, we can dynamically inject content designed to appear _after_ our menu item link. In the code above, we&#8217;re injecting an empty string, positioning it in the middle of the list item, and then styling it to look like a triangle using the `border` properties. The finished result will look something like this:

[<img src="http://www.levihackwith.com/wp-content/uploads/2013/06/dropdown-menu-final.png" alt="dropdown-menu-final" width="173" height="63" class="aligncenter size-full wp-image-310" />](http://www.levihackwith.com/wp-content/uploads/2013/06/dropdown-menu-final.png)

## Wrapping Up

Well, I hope you guys found this CSS menu tutorial a little more helpful than some of the other ones out there. If you don&#8217;t understand something or feel I could have explained something better, please let me know. Also feel free to let me know if you like this tutorial and would like to see more stuff like this.