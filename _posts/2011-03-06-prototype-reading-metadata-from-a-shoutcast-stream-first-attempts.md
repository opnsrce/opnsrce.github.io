---
title: 'Prototype: Reading Metadata from a Shoutcast Stream (First Attempts)'
date: 2011-03-06T22:12:34+00:00
author: Levi Hackwith
layout: post
code: true
categories:
  - Programming / Web Development
tags:
  - Audio
  - PHP
  - Shoutcast
---

[1]: http://stackoverflow.com/questions/4911062/pulling-track-info-from-an-audio-stream-using-php
[2]: http://stackoverflow.com/questions/4911062/pulling-track-info-from-an-audio-stream-using-php/4914538#4914538
[3]: http://us3.php.net/fsockopen
[4]: http://us3.php.net/curl

As a programmer, I listen to a lot of techno music. Recently, I began wondering
if it&rsquo;d be possible to parse the data from the Shoutcast streams using
PHP just like Winamp or Rythmbox. So far, I haven&rsquo;t been very successful.
For now, I&rsquo;m going to dump what code I have in attempt to chronicle
where I&rsquo;m at with this project as well as put the word out to there and
see if anyone can help me out.

<!--more-->

# Initial Research

Before beginning this project, I [posted a question Stackoverflow][1] asking
if anyone knew if what I was trying to attempt was even possible.
[I got some really solid answers][2] and set out writing a class.

# Getting the List of Available Streams

The first thing I had to do was screen-scrape the HTML from the mobile version
of Digitally imported, and get the list of channels:

~~~php
<?php
...
/**
 * Parses the channel URL and stores an array of playlists inside of
 * {@link playlists).
 * @author Levi Hackwith <evi.hackwith@gmail.com>
 * @access public
 * @return boolean
 */
private function setPlaylists() {
    $playlists = array();
    $html = @file_get_contents($this->channelListUrl);
    if($html) {
        $this->domDocument->loadHTML($html);
        $tableRows = $this->domDocument->getElementsByTagName('tr');
        foreach($tableRows as $tableRow) {
            $playlist = array();
            if($tableRow->getAttribute('class') == 'channel') {
                $columns = $tableRow->getElementsByTagName('td');
                foreach($columns as $column) {
                    $playlistLink = $column->getElementsByTagName('a');
                    if($column->getAttribute('class') == 'chantitle') {
                        $playlist['title'] = $column->nodeValue;
                    } elseif($playlistLink->length > 0) {
                        $playlist['url'] = $this->baseURL .
                            $playlistLink->item(0)->getAttribute('href');
                        $playlist['bitrate'] = $playlistLink->item(0)
                            ->nodeValue;
                        $playlists[] = $playlist;
                    }
                }
            }
        }
        $this->playlists = $playlists;
        return TRUE;
    } else {
        throw new DomainException(
            "Unable to retrieve data from $this->channelListUrl"
        );
    }
}
...
~~~

I won&rsquo;t bore you with the nuances of parsing HTML, but here&rsquo;s a
high-level breakdown of what&rsquo;s going on here:

  1. Grab every table row in the HTML page and loop through it.
  2. For each row, check for a table cell that has a class of ``chantitle`` and
     grab that cell&rsquo;s value
  3. Store that value in the $playlists array
  4. Return the array of available channel&rsquo;s

# Parsing the .pls file

Digitally Imported uses ``pls`` (playlist) files. Here&rsquo;s an example of one
of those files:

~~~
NumberOfEntries=5
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
~~~

A ``pls`` file is nothing more than an ``ini`` file full of URLs (in
this case, Shoutcast URLs). With this in mind, we can easily parse and store
the Shoutcast streams listed in the file. Let&rsquo;s take a look at that
function:

~~~php
<?php
/**
 * Takes in a URL to a .pls file, parses it, and then returns the stream
 * URL(s) it finds
 * @param string $playlistUrl The URL to the .pls file that will be parsed
 * @return array
 */
public function parsePlaylist($playlistUrl) {
    $playlistUrlData = parse_url($playlistUrl);
    $headers = array();
    $userAgent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; rv:1.7.3) " .
        "Gecko/20041001 Firefox/0.10.1";
    $curlRequest = curl_init();
    curl_setopt($curlRequest, CURLOPT_USERAGENT, $userAgent);
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
?>
~~~

What&rsquo;s going on here is pretty straight forward, so I won&rsquo;t go
into detail.

# Streaming the Music and Reading the Data (Where Everything Goes Wrong)

The Code:

~~~php
<?php
public function startStreaming($streamUrl) {
    if($this->streamConnection) {
        return FALSE;
    }
    $headers = array();
    $streamUrlData = parse_url($streamUrl);
    $headers[] = "GET / HTTP/1.1";
    $headers[] = 'Content-type: audio/mpeg';
    $headers[] = 'Accept:application/xml,application/xhtml+xml,text/html' +
        ';q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5';
    $headers[] = 'User-Agent: WinampMPEG/2.9';
    $headers[] = 'Accept-Charset:ISO-8859-1,utf-8;q=0.7,*;q=0.3';
    $headers[] = 'Accept-Encoding:gzip,deflate,sdch';
    $headers[] = 'Accept-Language:en-US,en;q=0.8';
    $headers[] = 'Cache-Control:max-age=0';
    $headers[] = 'Connection:keep-alive';
    $headers[] = 'Host:' . $streamUrl;
    $headers[] = 'Icy-MetaData:1';
    $headers[] = "\r\n";
    $this->streamConnection = @fsockopen(
        $streamUrlData['host'], 80, $errorNumber, $errorMsg, 30);
    if(!$this->streamConnection) {
        die("No connection");
    }
    fwrite($this->streamConnection, implode("\r\n", $headers));
    while(!feof($this->streamConnection)) {
        echo fgets($this->streamConnection);
    }
    $this->stopStreaming();
}
public function stopStreaming() {
    @fclose($this->streamConnection);
    $this->streamConnection = NULL;
    return TRUE;
}
?>
~~~

What&rsquo;s going on here is pretty simple: I&rsquo;m opening up a connection
to the Shoutcast stream, sending some header data and then outputting the
response from the server. I&rsquo;ve tried connecting with both [fsockopen][3]
and [CURL][4] and I get different results depending on which method I use. If
I connect with fsockopen I get an HTML page containing what appears to be some
basic statistical data about the server (song genre, currently playing song,
etc.,). If I connect with CURL, I get some binary data that I haven&rsquo;t
quite identified yet but the headers at least line up to what
I&rsquo;m expecting. And that&rsquo;s just it: I think the real problem lies
within the headers I&rsquo;m sending to the server.

# Help Wanted

I&rsquo;m going to keep doing some research and playing around with headers and
connection settings. If anyone out there has done something similar using PHP
or can at least point me in the right direction, let me know in the comments.