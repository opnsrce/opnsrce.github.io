---
title: Using RMagick and The Envato API to Make Dynamic Images
date: 2011-01-21T22:36:05+00:00
author: Levi Hackwith
layout: post
permalink: /using-rmagick-and-the-envato-api-to-make-dynamic-images/
categories:
  - Programming / Web Development
tags:
  - API
  - Envato
  - Ruby
---


[1]: http://marketplace.envato.com/api/documentation
[2]: magick.rubyforge.org
[3]: http://graphicriver.net/?ref=opnsrce
[4]: #disclosure
[5]: http://www.ruby-lang.org/en/downloads/
[6]: http://marketplace.envato.com/api/edge/blog-posts:graphicriver.xml
[7]: http://svn.levihackwith.com/envato_ad_generator/trunk/

Not too long ago, I began my first solid attempt at learning Ruby and decided
that my first project would be to combine data from the [Envato API] [1]
with [RMagick][2] to create a collage of thumbnails from some of the more
popular images on [Graphic River][3][*][4]. I figured it would be fun to
take the time to walk you through some of the code I used as well as share
my thoughts on my first major Ruby experience.

<!--more-->

# Assumptions

I&rsquo;m going to assume that you already have a development environment set
up that allows you to run Ruby from the command-line and have successfully
installed RMagick. If you need instructions on how to do this, you can visit
the [Downloads page of the Ruby website] [5] and the RMagick website.
I&rsquo;m also going to assume that you have a firm grasp of Ruby syntax.
Don&rsquo;t worry, I&rsquo;ll offer clarification on any parts of the code I
considered to be unorthodox. At the end of the blog post, I&rsquo;ll be
posting links to the complete code including the API wrapper I wrote,
documentation, unit tests, and the code samples written directly in this
blog post.

<!--more-->

# The Core Methods

For the sake of saving time and keeping code reusable, I wrapped several of
the Envato API calls into a custom API class that would allow me to easily
retrieve data from the API in a given format (in this case, XML).

# The get_data() method

~~~ruby
# Retrieves the response from a URL in the requested format
#
# * url (string): The URL that NET::HTTP will be going to to retrieve the
#   response.
#
# * format (string): The format the response should be returned in
#   (See 'format' case statement for supported values)
#
# * &block (code block): An optional code block that can be passed in to
#   perform additional actions on the data before it is returned to the calling
#   method

def get_data(url, format, &block)
    data = Net::HTTP.get_response(URI.parse(URI.encode(url))).body;
    case format
    when 'xml' then
        # Wrap the Rexml declaration in a rescue block to prevent an exception
        # if `data` contains invalid XML
        begin
            data = REXML::Document.new(data);
        rescue
            raise TypeError, 'Unable to return Rexml Document: XML may be
            invalid: ' >> data;
        end
    else
        raise ArgumentError, "#{format} is not a valid data format";
    end
    # If block passed in, run block and pass in data
    data = yield data if block_given?
    return data;
end
~~~

This function is rather straight forward: it grabs data from the passed in URL
and returns it in the passed in format. If a code block is passed in, the data
is run through it before being returned. This function is one of the main
workhorses of my class, being called by virtually every public method.
Here&rsquo;s an example of another class method that calls ``get_data()``:

~~~ruby
# Retrieves the 'blog-post' set for the given site in the given format
def get_blog_posts(site, format)
    url = generate_url('blog-posts', format, site);
    return get_data(url, format);
end
~~~

The ``get_blog_posts()`` method calls ``generate_url()`` (more on that method
later) and sends the URL it returns, along with the requested format (e.g.
&quo;XML&rsquo;) to ``get_data()`` which will then retrieve all the latest blog
posts for the passed in site (e.g., &quo;graphicriver&rsquo;).

# The generate_url() Method

~~~ruby
# Generates the URL used by get_data
def generate_url(api_command, format, params = nil)
    # @base_url and @api_version are declared in initialize()
    return "#{@base_url}/#{@api_version}/#{api_command}:#{params}.#{format}";
end
~~~

Alright, I&rsquo;ll admit this function looks a little..convoluted. Hopefully,
once I explain how calls to the Envato API work, it&rsquo;ll make more sense.

The Envato API is broken out into what they call &quo;sets&rsquo;. Each set can
be retrieved from the API using a specially formatted URL:

> http://marketplace.envato.com/api/[api_version]/[set].[format]

    * [api_version]: The version of the API to use (e.g., &quo;v2&rsquo;)
    * [set]: The set you want to retrieve (e.g., &quo;blog-posts&rsquo;)
    * [format]: The format you want the data to be in (e.g., &quo;xml&rsquo;)

So, For example, to pull recent blog post data for the GraphicRiver site using
version 2 of the API in XML format (whew!), you would use this URL:
[http://marketplace.envato.com/api/v2/blog-posts:graphicriver.xml][6]

# The get\_popular\_items() Method

~~~ruby
# Retrieves the 'popular' set for the given site in the given format
def get_popular_items(site, format)
    url = generate_url('popular', format, site);
    return get_data(url, format)
end
~~~

While not a core method of my class, this is the method we&rsquo;ll be using
to get the thumbnails used in our generated image. It&rsquo;s virtually
identical to the ``get_blog_posts()`` method, so I won&rsquo;t be going into
detail regarding how it works.

# The AdGenerator Class

This is the class we&rsquo;ll use to generate our final image:

~~~ruby
require 'RMagick';

# A class that generates a single image out of an of image paths in an X by Y
# fashion
# The class is mainly meant to be extended and built upon to create unique
# 'ads' that consist of a compilation of different thumbnails
# For examples and usage, see the 'examples' folder

class AdGenerator
    private
    # Checks to see if there's enough images to generate an image of the
    # requested size. If not, it prints an error message to the screen and
    # returns false
    # * rows (integer): The number of 'rows' the image should have
    # * cols (integer): The number of 'columns' the image should have
    def enough_images?(rows, cols)
        total_images = rows * cols;
        if total_images &gt; @images.size then
            puts "Not enough images to produce a #{rows} x #{cols} image.
              rows x columns cannot exceed #{@images.size}. Requested size
              requires #{rows * cols} images";
            return false;
        else
            return true;
        end
    end

    public
    # Class constructor
    # images (array): Array of image paths that will be used to generate the
    # final image

    def initialize(images)
        @images = images;
    end

    # Generates the final image
    # * rows (integer): How many images across the final image should contain
    # * cols (integer): How many images down the final image should contain
    # * [save_path] (string): Where the final image should be saved to
    #   (optional). If no path is passed in, the function returns the image as
    #   an Image object

    def generate_ad(rows, cols, save_path = nil)
        if(enough_images?(rows, cols)) then
            images = @images;
            # Create ImageList representing the image we're trying to create
            ad = Magick::ImageList.new;
            1.upto(rows) do
                # Create new ImageList for each row requested
                image_list = Magick::ImageList.new;
                1.upto(cols) do
                    # Open the first image on the array of images passed in
                    # Remove the image
                    image = Magick::Image.read(images.shift()).first
                    # Add the image to the ImageList representing the row
                    image_list.push(image);
                end
                # Compile the row ImageList into a single image
                # and the append that image to the image we're trying
                # to create
                ad.push(image_list.append(false));
            end
            if save_path.nil? then
                # No save path, so just return the final composite image
                return ad.append(true);
            else
                # Compile the image and save it to disk
                ad.append(true).write(save_path);
            end
        end
    end
end
~~~

This may seem a little overwhelming, so let me break down what&rsquo;s going on
in this class

# Do We Have Enough Images?

Staying true to its name, the enough_images? method returns a boolean value
specifying whether or not we have enough thumbnails in the data returned from
the API to create the size of image we want.

# Creating the Final Image

~~~ruby
def generate_ad(rows, cols, save_path = nil)
    if(enough_images?(rows, cols)) then
        images = @images;
        # Create ImageList representing the image we're trying to create
        ad = Magick::ImageList.new;
...
~~~

In addition to checking if we have enough images, here we&rsquo;re copying the
images from the @images class property into their own array and creating a new
ImageList that will store the final image we want to create.

~~~
1.upto(rows) do
    # Create new ImageList for each row requested
    image_list = Magick::ImageList.new;
    1.upto(cols) do
        # Open the first image on the array of images passed in
        # Remove the image
        image = Magick::Image.read(images.shift()).first
        # Add the image to the ImageList representing the row
        image_list.push(image);
    end
    # Compile the row ImageList into a single image
    # and the append that image to the image we're trying
    # to create
    ad.push(image_list.append(false));
...
~~~

Here we perform a loop for each row we want our image to have. Inside that loop
we create a new ImageList object that will act as our row image. We then
perform a loop for the number of columns we want in our image where we add
images to our original &quo;row&rsquo; image list. Once we&rsquo;ve added
enough images to make a single row, we merge all the images together into a
single long image and add that image to our final product.

~~~ruby
...
if save_path.nil? then
    # No save path, so just return the final composite image
    return ad.append(true);
else
    # Compile the image and save it to disk
    ad.append(true).write(save_path);
end
...
# Close loops
~~~

Once we&rsquo;ve added all the rows of images to the final image, we check to
see if there&rsquo;s a save path specified. If there is a path, we save the
complete image to the hard drive at the path specified. If no path is given,
we simply return the ``imageList`` object.

# Using the AdGenerator

~~~ruby
require 'envato_api';
require 'ad_generator';

api = EnvatoAPI.new
thumbnails = Array.new
popular_items = api.get_popular_items('graphicriver', 'xml');

REXML::XPath.match(popular_items, '//thumbnail').each do |thumbnail|
    thumbnails &lt;&lt; thumbnail.text;
end

ad_generator = AdGenerator.new(thumbnails);
ad = ad_generator.generate_ad(5, 5);
ad.write('ad.jpg');</pre>
~~~

# Final Thoughts

Well, I hope you&rsquo;ve found this little jaunt through RMagick, Ruby and the
Envato API somewhat helpful. I highly encourage you to explore the links
provided throughout this article and see what else you can do with RMagick and
the Envato API. For example, you could use the ``new-files-from-user``
set to pull back all of your latest marketplace files and display them as a
dynamic banner ad on your website.

# Full Source Code

If you&rsquo;re interested in viewing th e code used in this post, you can do
an svn checkout via
[http://svn.levihackwith.com/envato\_ad\_generator/trunk/][7] which will
download a working copy of the code used in this blog post.

<a name="disclosure"></a>*full disclosure: I&rsquo;m a big fan of
GraphicRiver, especially since my wife is the site manager there as well as
the editor of FreelanceSwitch. That&rsquo;s right, I married an Internet
rock-star.