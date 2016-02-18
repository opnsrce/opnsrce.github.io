---
id: 52
title: 'Prototype: Reading Metadata from a Shoutcast Stream (First Attempts)'
date: 2011-03-06T22:12:34+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=52
permalink: /prototype-reading-metadata-from-a-shoutcast-stream-first-attempts/
icy_video_embed_code:
  - 
categories:
  - Programming / Web Development
tags:
  - Audio
  - PHP
  - Shoutcast
---
As a programmer, I listen to a lot of techno music. Recently, I began wondering if it&#8217;d be possible to parse the data from the Shoutcast streams using PHP just like Winamp or Rythmbox. So far, I haven&#8217;t been very successful. For now, I&#8217;m going to dump what code I have in attempt to chronicle where I&#8217;m at with this project as well as put the word out to there and see if anyone can help me out.

<!--more-->

## Initial Research

Before beginning this project, I [posted a question Stackoverflow](http://stackoverflow.com/questions/4911062/pulling-track-info-from-an-audio-stream-using-php) asking if anyone knew if what I was trying to attempt was even possible. [I got some really solid answers](http://stackoverflow.com/questions/4911062/pulling-track-info-from-an-audio-stream-using-php/4914538#4914538) and set out writing a class.

## Getting the List of Available Streams

The first thing I had to do was screen-scrape the HTML from the mobile version of Digitally imported, and get the list of channels:

<pre class="brush: php; title: ; notranslate" title="">...
/**
 * Parses the channel URL and stores an array of playlists inside of {@link playlists).
 * @author Levi Hackwith &lt;levi.hackwith@gmail.com&gt;
 * @access public
 * @return boolean
 */
private function setPlaylists() {
    $playlists = array();
    $html = @file_get_contents($this-&gt;channelListUrl);
    if($html) {
        $this-&gt;domDocument-&gt;loadHTML($html);
        $tableRows = $this-&gt;domDocument-&gt;getElementsByTagName('tr');
        foreach($tableRows as $tableRow) {
            $playlist = array();
            if($tableRow-&gt;getAttribute('class') == 'channel') {
                $columns = $tableRow-&gt;getElementsByTagName('td');
                foreach($columns as $column) {
                    $playlistLink = $column-&gt;getElementsByTagName('a');
                    if($column-&gt;getAttribute('class') == 'chantitle') {
                        $playlist['title'] = $column-&gt;nodeValue;
                    } elseif($playlistLink-&gt;length &gt; 0) {
                        $playlist['url'] = $this-&gt;baseURL . $playlistLink-&gt;item(0)-&gt;getAttribute('href');
                        $playlist['bitrate'] = $playlistLink-&gt;item(0)-&gt;nodeValue;
                        $playlists[] = $playlist;
                    }
                }
            }
        }
        $this-&gt;playlists = $playlists;
        return TRUE;
    } else {
        throw new DomainException("Unable to retrieve data from $this-&gt;channelListUrl");
    }
}
...
</pre>

I won&#8217;t bore you with the nuances of parsing HTML, but here&#8217;s a high-level breakdown of what&#8217;s going on here:

  1. Grab every table row in the HTML page and loop through it.
  2. For each row, check for a table cell that has a class of &#8216;chantitle&#8217; and grab that cell&#8217;s value
  3. Store that value in the $playlists array
  4. Return the array of available channel&#8217;s

## Parsing the .pls file

Digitally Imported uses pls (playlist) files. Here&#8217;s an example of one of those files:

<pre class="brush: php; title: ; notranslate" title="">NumberOfEntries=5
File1=http://u14.di.fm:80/di_trance
Title1=Trance
Length1=-1
File2=http://u15c.di.fm:80/di_trance
Title2=Trance
Length2=-1
File3=http://u15.di.fm:80/di_trance
Title3=Trance
Length3=-1
File4=http://u12.di.fm:80/di_trance
Title4=Trance
Length4=-1
File5=http://u10.di.fm:80/di_trance
Title5=Trance
Length5=-1
Version=2
</pre>

A pls file is nothing more than an ini file full of url&#8217;s (in this case, Shoutcast URL&#8217;s). With this in mind, we can easily parse and store the Shoutcast streams listed in the file. Let&#8217;s take a look at that function:

<pre class="brush: php; title: ; notranslate" title="">...
/**
 * Takes in a URL to a .pls file, parses it, and then returns the stream URL(s) it finds
 * @param string $playlistUrl The URL to the .pls file that will be parsed
 * @return array
 */
public function parsePlaylist($playlistUrl) {
    $playlistUrlData = parse_url($playlistUrl);
    $headers = array();
    $curlRequest = curl_init();
    curl_setopt($curlRequest, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 5.1; rv:1.7.3) Gecko/20041001 Firefox/0.10.1" );
    curl_setopt($curlRequest, CURLOPT_URL, $playlistUrl);
    curl_setopt($curlRequest, CURLOPT_HEADER, FALSE);
    curl_setopt($curlRequest, CURLOPT_FOLLOWLOCATION, TRUE);
    curl_setopt($curlRequest, CURLOPT_RETURNTRANSFER, TRUE);
    curl_setopt($curlRequest, CURLOPT_FORBID_REUSE, TRUE);
    curl_setopt($curlRequest, CURLOPT_MAXREDIRS, 5);
    $response = curl_exec($curlRequest);
    curl_close($curlRequest);
    $playlist = parse_ini_string($response);
    $streamUrls = array();
    for($i = 1; $i &lt;= intval($playlist['NumberOfEntries']); $i++) {
        $streamUrls[] = $playlist['File' . $i];
        break;
    }
    return $streamUrls;
}
...
</pre>

What&#8217;s going on here is pretty straight forward, so I won&#8217;t go into detail.

## Streaming the Music and Reading the Data (Where Everything Goes Wrong)

The Code:

<pre class="brush: php; title: ; notranslate" title="">...
public function startStreaming($streamUrl) {
    if($this-&gt;streamConnection) {
        return FALSE;
    }
    $headers = array();
    $streamUrlData = parse_url($streamUrl);
    $headers[] = "GET / HTTP/1.1";
    $headers[] = 'Content-type: audio/mpeg';
    $headers[] = 'Accept:application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5';
    $headers[] = 'User-Agent: WinampMPEG/2.9';
    $headers[] = 'Accept-Charset:ISO-8859-1,utf-8;q=0.7,*;q=0.3';
    $headers[] = 'Accept-Encoding:gzip,deflate,sdch';
    $headers[] = 'Accept-Language:en-US,en;q=0.8';
    $headers[] = 'Cache-Control:max-age=0';
    $headers[] = 'Connection:keep-alive';
    $headers[] = 'Host:' . $streamUrl;
    $headers[] = 'Icy-MetaData:1';
    $headers[] = "\r\n";
    $this-&gt;streamConnection = @fsockopen($streamUrlData['host'], 80, $errorNumber, $errorMsg, 30);
    if(!$this-&gt;streamConnection) {
        die("No connection");
    }
    fwrite($this-&gt;streamConnection, implode("\r\n", $headers));
    while(!feof($this-&gt;streamConnection)) {
        echo fgets($this-&gt;streamConnection);
    }
    $this-&gt;stopStreaming();
}
public function stopStreaming() {
    @fclose($this-&gt;streamConnection);
    $this-&gt;streamConnection = NULL;
    return TRUE;
}
...
</pre>

What&#8217;s going on here is pretty simple: I&#8217;m opening up a connection to the Shoutcast stream, sending some header data and then outputting the response from the server. I&#8217;ve tried connecting with both [fsockopen](http://us3.php.net/fsockopen) and [CURL](http://us3.php.net/curl) and I get different results depending on which method I use. If I connect with fsockopen I get an HTML page containing what appears to be some basic statistical data about the server (song genre, currently playing song, etc.,). If I connect with CURL, I get some binary data that I haven&#8217;t quite identified yet but the headers at least line up to what I&#8217;m expecting. And that&#8217;s just it: I think the real problem lies within the headers I&#8217;m sending to the server.

## Help Wanted

I&#8217;m going to keep doing some research and playing around with headers and connection settings. If anyone out there has done something similar using PHP or can at least point me in the right direction, let me know in the comments