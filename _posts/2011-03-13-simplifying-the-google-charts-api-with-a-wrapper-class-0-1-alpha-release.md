---
id: 55
title: Simplifying the Google Charts API with a Wrapper Class (0.1 Alpha Release)
date: 2011-03-13T23:03:07+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=55
permalink: /simplifying-the-google-charts-api-with-a-wrapper-class-0-1-alpha-release/
categories:
  - Programming / Web Development
tags:
  - API
  - Charting
  - Google
---
Google has a habit of making really cool API&#8217;s to do really cool things. They also have a habit of making those API&#8217;s complicated and hard to memorize due to the overwhelming amount of parameters and commands that you can use to perform a given task. My programming goal for this week was to begin work on a library that would allow me to quickly and easily generate Google Image Charts as well as switch a chart from one type to another with minimal recoding. While I wasn&#8217;t able to complete the task by the time I needed to start writing about it, I was able to get a solid enough start to feel comfortable sharing what I have so far.

<!--more-->

## Google Chart Basics &#8211; The Series

According to [the documentation](http://code.google.com/apis/chart/docs/making_charts.html#chart_elements), a series is defined as:

> A related set of data in a chart. What constitutes a series depends on the chart type: in a line chart, a series is a single line; in a pie chart, each entry is a slice, and all slices together are a series. In a bar chart, a series is all the bars from the same set of data; different series are either grouped side by side or stacked atop each other, depending on the bar chart type&#8230;

Pretty straight forward. What&#8217;s not so straight forward is all the minute differences between series of a given chart type. A series for a  chart (e.g., a pie chart) will support certain features that a series in another type of chart may not. That being said, we can still clearly and cleanly establish a base Series object that we can use on every chart, regardless of type. Let&#8217;s take a look at that now:

<pre class="brush: php; title: ; notranslate" title="">&lt;?php
/**
 * @author Levi Hackwith &lt;levi.hackwith@gmail.com&gt;
 * @version 0.1 (Alpha)
 * @copyright 2011 Levi Hackwith
 * @filesource
 */

/**
 * The base series class that every other series object extends (e.g., {@link BarChartSeries})
 * @package GoogleChartWrapper
 * @subpackage Series
 * @abstract
 * @todo Set up exception codes for error handling (may want to consider creating custom Exception object)
 * @todo Write validation and 'set' logic for {@link __construct()}
 */
abstract class Series {
    /**
     * The minimum range value of the series. Only used when using custom scaling. Values below this number will be marked as missing. Defaults to FALSE.
     * @access protected
     * @var boolean|integer
     */
    protected $minRange;
    /**
     * The maximum range value of the series. Only used when using custom scaling. Values above this number will be truncated to this value. Defaults to FALSE.
     * @access protected
     * @var boolean|integer
     */
    protected $maxRange;
    /**
     * The data that makes up the series.
     * @access protected
     * @var array
     */
    protected $data = array();
    /**
     * The format that the {@link data} will be formatted to.
     * @access protected
     * @var string
     */
    protected $format;
    /**
     * The label(s) for the x-axis.
     * @var array
     */
    protected $xAxisLabel;
    /**
     * The label(s) for the y-axis.
     * @var array
     */
    protected $yAxisLabel;
    /**
     * Class constructor.
     * @author Levi Hackwith &lt;levi.hackwith@gmail.com&gt;
     * @access public
     * @param string $format Sets the value of {@link $format}
     */
    public function __construct($format = 'basic') {
        $this-&gt;format = $format;
    }
    /**
     * Method that's called when object gets converted to a string.
     * @author Levi Hackwith &lt;levi.hackwith@gmail.com&gt;
     * @access public
     * @return string
     */
    public function  __toString() {
        $urlParameters = '';
        $urlParameters .= "&chd=" . $this-&gt;convertDataForUrl();
        if($this-&gt;xAxisLabel && $this-&gt;yAxisLabel) {
            $urlParameters .= '&chxl=' . implode('|', $this-&gt;xAxisLabel) . '|' . $this-&gt;implode('|', $this-&gt;yAxisLabel);
        } elseif($this-&gt;xAxisLabel && !$this-&gt;yAxisLabel) {
            $urlParameters .= '&chxl=' . implode('|', $this-&gt;xAxisLabel);
        } elseif(!$this-&gt;xAxisLabel && $this-&gt;yAxisLabel) {
            $urlParameters .= '&chxl=' . implode('|', $this-&gt;yAxisLabel);
        }
        return $urlParameters;
    }
    /**
     * Converts {@link $data} into format for use in image URL.
     * @author Levi Hackwith &lt;levi.hackwith@gmail.com&gt;
     * @access private
     */
    private function convertDataForUrl() {
        switch($this-&gt;format) {
            case 'custom':
                break;
            case 'extended':
                break;
            default:
            case 'basic':
                return 't:' . implode(',', $this-&gt;data);
                break;
        }
    }
    /**
     * Returns {@link $data}
     * @return array
     */
    public function getData() {
        return $this-&gt;data;
    }
    /**
     * Adds data to the series. Adds new data into existing data array.
     * @author Levi Hackwith &lt;levi.hackwith@gmail.com&gt;
     * @access public
     * @param array $data The data to add to the series
     * @throws Exception if $data is not an array
     * @return Series
     */
    public function addData($data) {
        if(!is_array($data)) {
            throw New Exception(__METHOD__ . ': Data must be a non-associative array');
        }
        $this-&gt;data = array_merge($data, $this-&gt;data);
        return $this;
    }
    /**
     * Wipes out all data from the series.
     * @author Levi Hackwith &lt;levi.hackwith@gmail.com&gt;
     * @access public
     * @return Series
     */
    public function removeData() {
        $this-&gt;data = array();
        return $this;
    }
    /**
     * Returns the value of either {@link $minRange} or {@link $maxRange} based on the value of $range.
     * @author Levi Hackwith &lt;levi.hackwith@gmail.com&gt;
     * @access public
     * @param string $range The range to return. Can either be 'min' or 'max'
     * @return boolean|integer
     */
    public function getRange($range) {
        if($range == 'min') {
            return $this-&gt;minRange;
        } elseif($range == 'max') {
            return $this-&gt;maxRange;
        } else {
            throw new Exception(__METHOD__ . ": Invalid range type '$range'");
        }
    }
    /**
     * Sets the upper and lower range of the series
     * @author Levi Hackwith &lt;levi.hackwith@gmail.com&gt;
     * @access public
     * @param integer $min The lower range of the series. Must be less than the upper range of the series
     * @param integer $max The upper range of the series. Must be greater than the lower range of the series
     * @throws Exception if $min and $max are not integer or if $max is not greater than $min (or vice versa)
     * @return Series
     */
    public function setRange($min, $max) {
        if(!is_int($min) || is_int($max) || $max &gt; $min) {
            throw new Exception(__METHOD__ . ': Range must be a valid pair of integer and the minimum range must be less than the maximum range');
        }
        $this-&gt;minRange = $min;
        $this-&gt;maxRange = $max;
        return $this;
    }
    /**
     * Returns the value of {@link $xAxisLabel}
     * @author Levi Hackwith &lt;levi.hackwith@gmail.com&gt;
     * @access public
     * @return array
     */
    public function getXAxisLabel() {
        return $this-&gt;xAxisLabel;
    }
    /**
     * Sets the value of {@link $xAxisLabel}
     * @author Levi Hackwith &lt;levi.hackwith@gmail.com&gt;
     * @access public
     * @param array $label The label(s) to use on the x-axis
     * @return Series
     */
    public function setXAxisLabel($label) {
        array_unshift($label, '0:');
        $this-&gt;yAxisLabel = $label;
        return $this;
    }
    /**
     * Returns the  value of {@link $yAxisLabel}
     * @author Levi Hackwith &lt;levi.hackwith@gmail.com&gt;
     * @access public
     * @return array
     */
    public function getYAxisLabel() {
        return $this-&gt;xAxisLabel;
    }
    /**
     * Sets the value of {@link $yAxisLabel}
     * @author Levi Hackwith &lt;levi.hackwith@gmail.com&gt;
     * @access public
     * @param array $label The label(s) to use on the y-axis
     * @return Series
     */
    public function setYAxisLabel($label) {
        array_unshift($label, '1:');
        $this-&gt;yAxisLabel = $label;
        return $this;
    }
}
?&gt;</pre>

The big thing I want to point out about this class is that it is abstract: you can&#8217;t instantiate this class directly. Instead you should be creating specific series types that inherit from this base class:

<pre class="brush: php; title: ; notranslate" title="">&lt;?php
/**
 * @author Levi Hackwith &lt;levi.hackwith@gmail.com&gt;
 * @version 0.1 (Alpha)
 * @copyright 2011 Levi Hackwith
 * @filesource
 */
class BarChartSeries extends Series {
    public function  __construct($format = 'basic') {
        parent::__construct($format);
    }
}
?&gt;&lt;/pre&gt;
Now, &lt;em&gt;clearly&lt;/em&gt; there's not a whole lot happening here. At a base level all we've really done is redeclare the original Series object under a new name via inheritance. However, the beauty of using a base object like this and then extending it is that we can now safely add custom logic that only applies to our new object (in this case a data series designed specifically for bar charts) without polluting the original class with chart-specific logic or forcing us to duplicate code when new logic needs to applied to all Series objects.
&lt;h2&gt;Connecting Charts with Series and Chaining Method Calls&lt;/h2&gt;
As we discussed earlier, a chart is made up of a collection of series. Keeping with our idea of declaring a generic base class for dealing with similar kinds of objects, let's create a base Chart object (I apologize for the lack of documentation in this example):
&lt;pre escaped="true" lang="php" line="1"&gt;&lt;?php
/**
 * @author Levi Hackwith &lt;levi.hackwith@gmail.com&gt;
 * @version 0.1 (Alpha)
 * @copyright 2011 Levi Hackwith
 * @filesource
 */

/**
 * The base chart class that every other chart object extends (e.g., {@link BarChart})
 * @package GoogleChartWrapper
 * @subpackage Series
 * @abstract
 * @todo Complete documentation
 * @todo Flesh out getChartMargins, SetChartMargins, setLegendMargins
 * @todo Get $title supported
 */
abstract class Chart {
    protected $type;
    protected $title;
    protected $width;
    protected $height;
    protected $chartMargins;
    protected $legendMargins;
    protected $baseUrl = 'https://chart.googleapis.com/chart';
    protected $series = array();
    public function __construct($type, $width, $height) {
        $this-&gt;type = $type;
        $this-&gt;width = $width;
        $this-&gt;height = $height;
    }
    public function  __toString() {
        return $this-&gt;baseUrl . '?' . $this-&gt;encode() . implode('|', $this-&gt;series);
    }
    public function getChartMargins() {

    }
    public function setChartMargins($left, $right, $top, $bottom) {
    }
    public function setLegendmargins($width, $height) {
    }
    protected function encode() {
        $urlParams = array();
        $urlParams[] = "cht=$this-&gt;type";
        $urlParams[] = "chs={$this-&gt;width}x{$this-&gt;height}";
        $urlParams[] = "chtt=$this-&gt;title";
        return implode('&', $urlParams);

    }
    public function addSeries(Series $series) {
        $this-&gt;series[] = $series;
        return $this;
    }
}
?&gt; </pre>

This class hasn&#8217;t been fleshed out all the way yet, but I still want to bring attention to some key methods and properties that will come into play later on:

<pre class="brush: php; title: ; notranslate" title="">...
protected $baseUrl = 'https://chart.googleapis.com/chart';
...</pre>

All Google charts commands are sent from the same basic URL structure. the $baseURL variable holds that URL value and gets used whenever a call is sent to the API.

<pre class="brush: php; title: ; notranslate" title="">protected function encode() {
    $urlParams = array();
    $urlParams[] = "cht=$this-&gt;type";
    $urlParams[] = "chs={$this-&gt;width}x{$this-&gt;height}";
    $urlParams[] = "chtt=$this-&gt;title";
    return implode('&', $urlParams);
}
...</pre>

This method parses out all the properties of the series and encodes them into the query string used in the URL. Now, isn&#8217;t really very complicated stuff. However, I wanted to point it out because in our child objects (e.g., BarChartSeries) need to deconstruct the value returned from this function in order to add to it:

<pre class="brush: php; title: ; notranslate" title="">...
// From BarChart.php
protected function encode() {
    $urlParams = explode('&', parent::encode());
    $urlParams[] = "chxt=$this-&gt;visibleAxis";
    return implode('&', $urlParams);
}
...</pre>

Notice how we explode the result from the parent encode method, add our additional parameters into the resulting array, and then implode it back into a query string.

<pre class="brush: php; title: ; notranslate" title="">...
public function addSeries(Series $series) {
    $this-&gt;series[] = $series;
    return $this;
}
...</pre>

This method allows us to add multiple Series objects into a chart. When encoded to a URL, the data in each series will be separated by a pipe.

## Usage and Output

Now that we&#8217;ve covered our base objects and how to extend them, here&#8217;s how to currently implement the API wrapper:

<pre class="brush: php; title: ; notranslate" title="">&lt;?php
require('charts/Chart.php');
require('charts/BarChart.php');
require('series/Series.php');
require('series/BarChartSeries.php');
require('series/PieChartSeries.php');
$chart = new BarChart(BarChart::VERTICAL_BAR_CHART_WITH_GROUPED_BARS, 200, 200);
$series = new BarChartSeries();
$series2 = new BarChartSeries();
$series-&gt;addData(array(5, 10, 15));
$series-&gt;setXAxisLabel(array('Red', 'Green', 'Blue'));
$chart-&gt;addSeries($series);
?&gt;;

&lt;img alt = "" src = "&lt;?= $chart ?&gt;"&gt;
</pre>

Which outputs:

![](https://chart.googleapis.com/chart?cht=bvg&chs=500x500&chtt=&chxt=x,y&chd=t:5,10,15&chxl=0:|Red|Green|Blue)

## Back to Work

Well, I best be getting back to work on this project. I feel it&#8217;s been very successful so far and I feel fairly confident that I&#8217;ll have production-level code ready and written about by the end of the week. If you&#8217;d like to download a complete copy of the project as it stands today, you can do an svn checkout of the [version\_0.1\_alpha tag](http://svn.levihackwith.com/google_charts/tags/version_0.1_alpha/). If you want to keep up with the project as I develop it, just checkout the [trunk](http://svn.levihackwith.com/google_charts/trunk/).

I&#8217;d also like to take a moment to thank [Andy Malichar](http://www.andymelichar.com/) for inspiring me to start this project. I feel your pain, man. 😀