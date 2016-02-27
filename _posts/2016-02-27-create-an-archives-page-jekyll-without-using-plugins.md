---
title: 'Create an Archives Page in Jekyll Without Using Plugins'
date: 2016-02-18T00:00:34+00:00
author: Levi Hackwith
layout: post
permalink: /create-an-archives-page-jekyll-without-using-plugins/
categories:
  - Programming / Web Development
tags:
  - SASS
  - CSS
  - Mixin
---

[1]: https://github.com/github/pages-gem/pull/106

Recently, I wanted to add an &ldquo;Archives&rdquo; to my site. While this
can be easily done via a number of Jekyll plugins, Github pages (my
site&rsquo;s host) doesn't allow custom plugins on their platform and won't be
adding an archives feature [anytime soon][1]. However, I did some experimenting
and came up with a way to create a simple Archives page without using plugins.

<!--more-->

# Step 1: Limit Posts on the Main Page

The first thing your going to want to do is limit the number of posts that get
displayed on your site's landing page:

~~~hbs
{% raw %}
  <ul class="post-list">
    {% for post in site.posts limit:site.pagination %}
    <li>
      <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}
        {{post.excerpt.length}}
      </span>

      <h2>
        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">
          {{ post.title }}
        </a>
      </h2>
      <p class="post-excerpt">
        {{ post.excerpt }}
      </p>
        <a
          class = "post-read-more-link"
          href="{{ post.url | prepend: site.baseurl }}">
          Read More
        </a>
    </li>
    {% endfor %}
  </ul>
  {% endraw %}
~~~

Here we've limited the number of posts being displayed to the value of the
``pagination`` property in our ``_config.yml`` file. You don't have to use this
variable if you don't want to. I just chose it because it made the most sense.

## Step 2: Create Archives.html

Now that we've limited what we show on the homepage, we can go ahead and create
the archives page to display our remaining posts:

~~~hbs
{% raw %}
---
title: Archives
layout: default
---

<div class="home-page">
    <h1 class="home-page__title">{{ page.title }}</h1>
    <ol class="home-page__post-list">
        {% for post in site.posts offset: site.pagination + 1 %}
        <li class="post">
            <span class="date">{{ post.date | date: "%b %-d, %Y" }}</span>
            <h2 class="title">
                <a class="link" href="{{ post.url }}">{{ post.title }}</a>
            </h2>
        </li>
        {% endfor %}
    </ol>
</div>
{% endraw}
~~~

The only new thing to point out is the use of the ``offset`` parameter in our
``for`` loop. This tells the loop what index to start at when looping through
the site's posts.