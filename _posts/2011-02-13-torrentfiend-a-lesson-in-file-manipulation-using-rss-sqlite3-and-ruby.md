---
id: 33
title: 'TorrentFiend: A Lesson in File Manipulation Using RSS, SQLite3 and Ruby'
date: 2011-02-13T10:01:45+00:00
author: Levi Hackwith
layout: post
code: true
permalink: /torrentfiend-a-lesson-in-file-manipulation-using-rss-sqlite3-and-ruby/
categories:
  - Programming / Web Development
tags:
  - Ruby
  - SQLite3
---

[1]: http://en.wikipedia.org/wiki/BitTorrent_tracker#Private_trackers
[2]: https://github.com/opnsrce/TorrentFiend

Back when I was in college, I didn&rsquo;t have cable or even a TV. In order
to stay entertained, I relied heavily on bittorrent to keep up with my
favorite free and totally legal to download shows like, *_ahem_* _Found_ and
_How I Lost Your Father_. Unfortunately, with my busy work/class schedule
I didn&rsquo;t have time to surf my favorite torrent site and download the
latest episodes of all the shows I watched each week. To combat this problem,
I wrote a small perl script that ran during the week, checking an RSS feed for
new episodes of each show. Now, as part of my goal to learn Ruby, I&rsquo;v
converted the script into Ruby and have decided to release the code publicly
for those who would like a better understanding of how Ruby reads and
manipulates RSS data.

<!--more-->

Let&rsquo;s take a look at the code, shall we?

The first thing we need to do is include some libraries that will add-in the
functionality we need to send http requests, manipulate URLs and XML
documents, and write data to a SQLite3 database (you may need to install
additional gems in order to get these all working properly):

~~~ruby
require 'net/http';
require 'open-uri';
require 'rexml/document';
require 'sqlite3';
require 'net/http';
require 'uri';
require 'rexml/document';
require 'sqlite3';
...
~~~

Now that we&rsquo;ve got our includes all set up, let&rsquo;s dive into
torrentFiend&rsquo;s download_torrent method:

~~~ruby
def download_torrent(episode_id, torrent_url, limit = 10)
    # Check to make sure we haven't been trapped in an infinite loop
    if limit == 0 then
        puts "Too much redirection, skipping #{episode_id}";
        return true;
    else
        # Convert the URL of the torrent into a URI usable by Net:HTTP
        torrent_uri = URI.parse(torrent_url);
        # Open a connection to the torrent URL
        Net::HTTP.get_response(torrent_uri) { |http|
            # Check to see if we were able to connect to the torrent URL
            case http
            # We connected just fine
            when Net::HTTPSuccess, Net::HTTPFound then
                # Create a torrent file to store the data in
                File.open("#{episode_id}.torrent", 'wb') { |torrent_file|
                # Write the torrent data to the torrent file
                torrent_file.write(http.body);
                # Close the torrent file
                torrent_file.close

                # Check to see if we've download a 'locked' torrent file
                # (html) instead of a regular torrent (.torrent)
                if(File.exists?('download.torrent.html'))
                    # Delete the html file
                    File.delete('download_torrent.html');
                    return false;
                else
                    return true;
                end
            }
            when Net::HTTPRedirection then
                download_torrent(episode_id, http['location'], limit - 1);
            end
        }
    end
end
~~~

The first thing you&rsquo;ll notice in this method is a check of the value of
the limit variable:

~~~ruby
...
    # Check to make sure we haven't been trapped in an infinite loop
    if limit == 0 then
        puts "Too much redirection, skipping #{episode_id}";
        return true;
...
~~~

The idea here is pretty straight forward: in the event that we get redirected
when trying to download a torrent from the passed in URL, this function will
be called again with the new destination passed in for the URL and the limit
variable decremented by 1. This is to prevent our program from getting stuck
in a series of infinite redirects. For the purposes of this program,
we&rsquo;ve limited the number of possible redirects to ten. Now that
we&rsquo;ve done our safety check against redirects, let&rsquo;s try and
resolve the URL that got passed in:

~~~ruby
...
    # Convert the URL of the torrent into a URI usable by Net:HTTP
    torrent_uri = URI.parse(torrent_url);
    # Open a connection to the torrent URL
    Net::HTTP.get_response(torrent_uri) { |http|
        # Check to see if we were able to connect to the torrent URL
        case http
            # We connected just fine
        when Net::HTTPSuccess, Net::HTTPFound then
            # Create a torrent file to store the data in
            File.open("#{episode_id}.torrent", 'wb') { |torrent_file|
                # Write the torrent data to the torrent file
                torrent_file.write(http.body);
                # Close the torrent file
                torrent_file.close
                # Check to see if we've download a 'locked' torrent file
                # (html) instead of a regular torrent (.torrent)
                if(File.exists?('download.torrent.html'))
                    # Delete the html file
                    File.delete('download_torrent.html');
                    return false;
                else
                    return true;
                end
            }
        when Net::HTTPRedirection then
            download_torrent(episode_id, http['location'], limit - 1);
        end
...
~~~

After we parse the URL into a format Net::HTTP can use, we attempt to connect
to the URL and check to see what kind of response we received. If we received
a normal response (``success`` or ``found``), we create a new torrent file
based off of the episode_id passed in and write the data we received from the
URL to it. Let&rsquo;s take a closer look at a few lines of logic within that
check:

~~~ruby
...
    # Write the torrent data to the torrent file
    torrent_file.write(http.body);
    # Close the torrent file
    torrent_file.close
    # Check to see if we've download a 'locked' torrent file (html) instead of
    # a regular torrent (.torrent)
    if(File.exists?('download.torrent.html'))
        # Delete the html file
        File.delete('download_torrent.html');
        return false;
    else
        return true;
...
~~~

What we&rsquo;re doing here is checking to see if we&rsquo;ve downloaded a
file tied to a [private tracker][1]. In the event that our software tries to
download a privately-tracked torrent, it&rsquo;ll receive a file named
download_torrent.html instead of a standard .torrent file. If we didn&rsquo;t
check for this file, our program would read this as a false positive and
incorrectly increment the torrent episode to the next value causing us to miss
that episode. Word of caution: the check we do for privately tracked torrents
is specifically designed for the site whose RSS feed we&rsquo;re using to pull
torrents; it may not work if you decide to code the app to look at another
site&rsquo;s feed.

# Pulling and Reading the Feed

Now that we&rsquo;ve covered how to download the torrent&rsquo;s from a URL,
let&rsquo;s take a moment and look at the code that pulls those URL&rsquo;s
from the torrent site:

~~~ruby
...
# Create new SQLite3 database connection
db_connection = SQLite3::Database.new('fiend.db');
# Create the table for shows if it doesn't exist to prevent the app from
# crashing
create_table_query = '
    CREATE TABLE IF NOT EXISTS shows (
        id INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        current_season INTEGER NOT NULL,
        last_episode INTEGER NOT NULL
    )
';

db_connection.execute(create_table_query);
# Make sure I can reference records in the query result by column name instead
# of index number
db_connection.results_as_hash = true;
# Grab all TV shows from the shows table
query = '
    SELECT
        id,
        name,
        current_season,
        last_episode
    FROM
        shows
    ORDER BY
        name
';
# Run through each record in the result set
db_connection.execute(query) { |show|
    # Pad the current season number with a zero for later user in a search query
    season = '%02d' % show['current_season'].to_s;
    # Calculate the next episode number and pad with a zero
    next_episode = '%02d' % (Integer(show['last_episode']) + 1).to_s;
    # Store the name of the show
    name = show['name'];
    # Generate the URL of the RSS feed that will hold the list of torrents
    feed_url = URI.encode("http://btjunkie.org/rss.xml?query=#{name} " +
        S#{season}E#{next_episode}&o=52");
    # Generate a simple string the denotes the show, season and episode number
    # being retrieved
    episode_id = "#{name} S#{season}E#{next_episode}";
    puts "Loading feed for #{name}..";
    # Store the response from the download of the feed
    feed_download_response = Net::HTTP.get_response(URI.parse(feed_url));
    # Store the contents of the response (in this case, XML data)
    xml_data = feed_download_response.body;
    puts "Feed Loaded. Parsing items.."
    # Create a new REXML Document and pass in the XML from the Net::HTTP
    # response
    doc = REXML::Document.new(xml_data);
    # Loop through each  in the feed
    doc.root.each_element('//item') { |item|
        # Find and store the URL of the torrent we wish to download
        torrent_url = item.elements['link'].text + '/download.torrent';
        puts "Downloading #{episode_id} from #{torrent_url}";
        if download_torrent(episode_id, torrent_url) == true then
            update_show_listing(db_connection, show['id']);
        end
        break;
  }

}
~~~

The first thing we do in this code block is grab all the shows from our SQLite
database and begin to loop through them. Once inside the loop, we pad the
episode and season number with zeros and create a dynamic URL that we can send
to the torrent site to get the RSS feed full of available torrents (again,
this logic is specific to the torrent site listed in the code). For example,
we were looking for season one, episode one of _Found_, our search string
would end up being ``Found S01E01``.

Once we&rsquo;ve generated the feed, we loop through the items and attempt to
download each one until we get a success message from our
``download_torrent()`` function. Once the success message is received, we
increment the last downloaded episode number, save it to the database, and
repeat the whole process with the next show on our list.

# Using the Program

To use TorrentFiend, all you need to do is fill the shows table with the TV
shows you want to watch (I&rsquo;ll assume these are shows that are totally f
ree and legal to download via bittorrent) along with the current season and
last episode number (for new shows start with episode number 0). Once
you&rsquo;ve done that, just schedule the script to run via the ruby command
on an interval of your choosing (I ran mine once a week), and you&rsquo;re
good to go. If you want the shows to download automatically, just drop the
script into a folder that&rsquo;s monitored by your bittorrent application.

# Final Thoughts

For me, TorrentFiend was a great exercise in file retrieval and database
manipulation using Ruby. It gave me a solid foundation for creating other
helpful utility scripts in Ruby as well as a firm springboard into the more
advanced aspects of the language. Hopefully, you found it helpful too.
If you&rsquo;d like to download a copy of the complete source code (
including the original Perl version), checkout [github][2].