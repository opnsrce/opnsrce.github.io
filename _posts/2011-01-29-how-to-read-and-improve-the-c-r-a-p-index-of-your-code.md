---
id: 15
title: How to Read and Improve the C.R.A.P Index of your code
date: 2011-01-29T00:00:52+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=15
permalink: /how-to-read-and-improve-the-c-r-a-p-index-of-your-code/
icy_video_embed_code:
  - 
categories:
  - Programming / Web Development
tags:
  - PHP
---
When I first started using PHPUnit to test my code, I ran across a statistic I had never seen before: the C.R.A.P index. After doing a little research and <a href="http://stackoverflow.com/questions/4731774/how-to-read-improve-c-r-a-p-index-calculated-by-php" target="_blank">asking the right questions</a>, I was able to get a firm grasp on what the C.R.A.P index is and what it means for my code.

<!--more-->

## What is the C.R.A.P Index?

According to <a href="http://www.artima.com/weblogs/viewpost.jsp?thread=210575" target="_blank">Alberto Savoia, the creator of the index</a>, C.R.A.P is:

> The C.R.A.P. (Change Risk Analysis and Predictions) index is designed to analyze and predict the amount of effort, pain, and time required to maintain an existing body of code.

Basically it&#8217;s a number designed to highlight potential problem areas in the code you&#8217;ve written. The higher the number, the crappier your code may be and the more likely it should be reexamined and refactored.

## Testing This Theory &#8211; Write Some Crappy Code

In order to see just how the C.R.A.P index works, we must first write some crappy code. In the following snippet, I&#8217;ve created a PHP object called CrapClass that contains the method listCities:

<pre class="brush: php; title: ; notranslate" title="">&lt;?php
class CrapClass {
    /**
     * Prints a short list of cities within a given state
     * @access public
     * @author Levi Hackwith
     * @param string $state The state whose cities we want to list
     * @return boolean Returns true if everything ran fine, or throws an UnexpectedValueException
     */
    public function listCities($state){
        if($state == 'Nebraska') {
            print('Omaha, Lincoln, Bellevue, LaVista');
        } elseif ($state == 'Iowa') {
            print('Des Moines, Council Bluffs, Red Oak');
        } elseif ($state == 'Florida') {
            print('Tampa, Pensacola, Miami');
        } elseif($state == 'Massachusetts') {
            print('Acton, Andover, Bedford');
        } elseif($state == 'Alabama') {
            print('Abbeville, Adamsville, Addison');
        } else {
            throw new UnexpectedValueException("Unknown State: '$state'");
        }
        return TRUE;
    }
}
</pre>

Yeah, that&#8217;ll do nicely. Now let&#8217;s create a unit test that doesn&#8217;t really test any of the code:

<pre class="brush: php; title: ; notranslate" title="">&lt;?php
require_once dirname(__FILE__) . '/../CrapClass.php';
class CrapClassNoTest extends PHPUnit_Framework_TestCase {

    /**
     * @var CrapClass
     */
    protected $crapClass;

    /**
     * Sets up the fixture, for example, opens a network connection.
     * This method is called before a test is executed.
     */
    protected function setUp() {
        $this-&gt;crapClass = new CrapClass;
    }

    /**
     * Tears down the fixture, for example, closes a network connection.
     * This method is called after a test is executed.
     */
    protected function tearDown() {

    }

    /**
     * @todo Implement testListCities().
     */
    public function testListCities() {
        // Remove the following lines when you implement this test.
        $this-&gt;markTestIncomplete('This test has not been implemented yet.');
    }

}
?&gt;</pre>

When we run the code coverage report for this test case, this is what we get (click for a larger view):

<p style="text-align: center;">
  <a href="http://www.levihackwith.com/wp-content/uploads/2011/01/crapClassNoTest.png"><img class="aligncenter size-full wp-image-18" title="crapClassNoTest" src="http://www.levihackwith.com/wp-content/uploads/2011/01/crapClassNoTest.png" alt="" width="727" height="87" srcset="http://www.levihackwith.com/wp-content/uploads/2011/01/crapClassNoTest-1024x122.png 1024w, http://www.levihackwith.com/wp-content/uploads/2011/01/crapClassNoTest.png 1212w" sizes="(max-width: 727px) 100vw, 727px" /></a>
</p>

Wow, a C.R.A.P index of 42. Why so high? Well, in addition to the 6 possible logic paths inside of the listCities method, the amount of code-coverage provided by the unit test class is at zero percent. So what&#8217;s the first step in improving our code?

## Write More Complete Unit Tests

Part of what makes up the C.R.A.P index is how much of your code is covered by unit tests. The more the code is covered, the lower the C.R.A.P index. Let&#8217;s see what happens when we add a few tests to our testing class:

<pre class="brush: php; title: ; notranslate" title="">&lt;?php

require_once dirname(__FILE__) . '/../CrapClass.php';

/**
 * Test class for CrapClass.
 * Generated by PHPUnit on 2011-01-22 at 19:01:20.
 */
class CrapClasPartialTest extends PHPUnit_Extensions_OutputTestCase {

    /**
     * @var CrapClass
     */
    protected $crapClass;

    /**
     * Sets up the fixture, for example, opens a network connection.
     * This method is called before a test is executed.
     */
    protected function setUp() {
        $this-&gt;crapClass = new CrapClass();
    }

    /**
     * Tears down the fixture, for example, closes a network connection.
     * This method is called after a test is executed.
     */
    protected function tearDown() {

    }
    public function statesProvider() {
        return array(
            array('Nebraska'),
            array('Iowa')
        );
    }
    /**
     * @dataProvider statesProvider
     */
    public function testListCities($state) {
        switch($state) {
            case 'Nebraska':
                $this-&gt;expectOutputString('Omaha, Lincoln, Bellevue, LaVista');
                break;
            case 'Iowa':
                $this-&gt;expectOutputString('Des Moines, Council Bluffs, Red Oak');
                break;
        }
        $this-&gt;crapClass-&gt;listCities($state);
    }

}
?&gt;</pre>

And here&#8217;s the new coverage report:

<div id="attachment_19" style="width: 740px" class="wp-caption aligncenter">
  <a href="http://www.levihackwith.com/wp-content/uploads/2011/01/crapClassPartialTest.png"><img class="size-full wp-image-19  " title="Code Coverage Report After Adding a Few Unit Tests" src="http://www.levihackwith.com/wp-content/uploads/2011/01/crapClassPartialTest.png" alt="" width="730" height="86" srcset="http://www.levihackwith.com/wp-content/uploads/2011/01/crapClassPartialTest-300x35.png 300w, http://www.levihackwith.com/wp-content/uploads/2011/01/crapClassPartialTest-1024x120.png 1024w, http://www.levihackwith.com/wp-content/uploads/2011/01/crapClassPartialTest.png 1216w" sizes="(max-width: 730px) 100vw, 730px" /></a>
  
  <p class="wp-caption-text">
    Code Coverage Report After Adding a Few Unit Tests
  </p>
</div>

By adding a unit test that covers just two of the 6 possible paths in our listCities method, we&#8217;ve dropped the C.R.A.P index from 42 to 11.62, a marked improvement. Let&#8217;s see what happens when we write tests to cover all the code:

<pre class="brush: php; title: ; notranslate" title="">&lt;?php

require_once dirname(__FILE__) . '/../CrapClass.php';

/**
 * Test class for CrapClass.
 * Generated by PHPUnit on 2011-01-22 at 19:01:20.
 */
class CrapClassCompleteTest extends PHPUnit_Extensions_OutputTestCase {

    /**
     * @var CrapClass
     */
    protected $crapClass;

    /**
     * Sets up the fixture, for example, opens a network connection.
     * This method is called before a test is executed.
     */
    protected function setUp() {
        $this-&gt;crapClass = new CrapClass();
    }

    /**
     * Tears down the fixture, for example, closes a network connection.
     * This method is called after a test is executed.
     */
    protected function tearDown() {

    }
    public function statesProvider() {
        return array(
            array('Nebraska'),
            array('Iowa'),
            array('Florida'),
            array('Massachusetts'),
            array('Alabama')
        );
    }
    /**
     * @dataProvider statesProvider
     */
    public function testListCities($state) {
        switch($state) {
            case 'Nebraska':
                $this-&gt;expectOutputString('Omaha, Lincoln, Bellevue, LaVista');
                break;
            case 'Iowa':
                $this-&gt;expectOutputString('Des Moines, Council Bluffs, Red Oak');
                break;
            case 'Florida':
                $this-&gt;expectOutputString('Tampa, Pensacola, Miami');
                break;
            case 'Massachusetts':
                $this-&gt;expectOutputString('Acton, Andover, Bedford');
                break;
            case 'Alabama':
                $this-&gt;expectOutputString('Abbeville, Adamsville, Addison');
                break;
        }
        $this-&gt;crapClass-&gt;listCities($state);
    }
    /**
     * @expectedException UnexpectedValueException
     */
    public function testListCitiesException() {
        try {
            $this-&gt;crapClass-&gt;listCities('California');
        } catch(UnexpectedValueException $e) {
            throw $e;
        }
    }

}
?&gt;</pre>

<div id="attachment_20" style="width: 741px" class="wp-caption aligncenter">
  <a href="http://www.levihackwith.com/wp-content/uploads/2011/01/crapClassCompleteTest.png"><img class="size-full wp-image-20 " title="Code Coverage Report after writing complete tests" src="http://www.levihackwith.com/wp-content/uploads/2011/01/crapClassCompleteTest.png" alt="" width="731" height="85" srcset="http://www.levihackwith.com/wp-content/uploads/2011/01/crapClassCompleteTest-1024x119.png 1024w, http://www.levihackwith.com/wp-content/uploads/2011/01/crapClassCompleteTest.png 1219w" sizes="(max-width: 731px) 100vw, 731px" /></a>
  
  <p class="wp-caption-text">
    Code Coverage Report after writing complete tests
  </p>
</div>

Just by writing more complete unit tests, our C.R.A.P index for the listCities method went from 11.62 to 6. While this is all well and good, the C.R.A.P index doesn&#8217;t just take into account code coverage, it also calculates code complexity. Which brings me to another method of lowering the C.R.A.P index of our code:

## Write Less-Complex Code

The other factor used in calculating the C.R.A.P index, is the number of logic &#8220;paths&#8221; found within the code. The more individual paths found, the harder the code is to maintain and the higher the index will be. Before we begin refactoring, let&#8217;s take a closer look at our listCities method (I&#8217;ve numbered all the possible logic-paths):

<pre class="brush: php; title: ; notranslate" title="">&lt;?php
class CrapClass {
    /**
     * Prints a short list of cities within a given state
     * @access public
     * @author Levi Hackwith
     * @param string $state The state whose cities we want to list
     * @return boolean Returns true if everything ran fine, or throws an UnexpectedValueException
     */
    public function listCities($state){
        if($state == 'Nebraska') { // 1
            print('Omaha, Lincoln, Bellevue, LaVista');
        } elseif ($state == 'Iowa') { // 2
            print('Des Moines, Council Bluffs, Red Oak');
        } elseif ($state == 'Florida') { // 3
            print('Tampa, Pensacola, Miami');
        } elseif($state == 'Massachusetts') { // 4
            print('Acton, Andover, Bedford');
        } elseif($state == 'Alabama') { // 5
            print('Abbeville, Adamsville, Addison');
        } else { // 6
            throw new UnexpectedValueException("Unknown State: '$state'");
        }
        return TRUE;
    }
}
?&gt;</pre>

There are a total of six possible logic-paths in this method. Let&#8217;s reduce that number, rereun the unit tests, and see what happens:

<pre class="brush: php; title: ; notranslate" title="">&lt;?php
class CrapClass {
    private $states = array();

    public function __construct() {
        $this-&gt;states = array(
            'Nebraska' =&gt; array('Omaha', 'Lincoln', 'Bellevue', 'LaVista'),
            'Iowa' =&gt; array('Des Moines', 'Council Bluffs', 'Red Oak'),
            'Florida' =&gt; array('Tampa', 'Pensacola', 'Miami'),
            'Massachusetts' =&gt; array('Acton', 'Andover', 'Bedford'),
            'Alabama' =&gt; array('Abbeville', 'Adamsville', 'Addison')
        );
        return TRUE;
    }
    /**
     * Prints a short list of cities within a given state
     * @access public
     * @author Levi Hackwith
     * @param string $state The state whose cities we want to list
     * @return boolean True if everything ran fine, or throws an UnexpectedValueException
     */
    public function listCities($state){
        if(isset($this-&gt;states[$state])) {
            echo implode(', ', $this-&gt;states[$state]);
            return TRUE;
        } else {
            throw new UnexpectedValueException("Unknown State: '$state'");
        }
    }
}
?&gt;</pre>

<div id="attachment_21" style="width: 733px" class="wp-caption aligncenter">
  <a href="http://www.levihackwith.com/wp-content/uploads/2011/01/CrapClassRefactoredTest.png"><img class="size-full wp-image-21 " title="Code Coverage Report After Refactoring the listCities method" src="http://www.levihackwith.com/wp-content/uploads/2011/01/CrapClassRefactoredTest.png" alt="" width="723" height="101" srcset="http://www.levihackwith.com/wp-content/uploads/2011/01/CrapClassRefactoredTest-1024x142.png 1024w, http://www.levihackwith.com/wp-content/uploads/2011/01/CrapClassRefactoredTest.png 1205w" sizes="(max-width: 723px) 100vw, 723px" /></a>
  
  <p class="wp-caption-text">
    Code Coverage Report After Refactoring the listCities method
  </p>
</div>

By refactoring our code, we were able to lower our method&#8217;s C.R.A.P index to 2 and make the listCities method much more maintainable.

## Final Thoughts

While lowering the C.R.A.P index of our code is always a good goal, it can easily create more problems than it solves. Refactoring your code just lower a number on a report is never a good idea. By arbitrarily lowering the C.R.A.P index, or any other programming metric for that matter, you not only go against the metric&#8217;s original intent, but you add an artificial and unnecessary complexity to your code that could end up doing more harm than good.

> &#8230;software metrics, in general, are just tools. No single metric can tell the whole story; it’s just one more data point. Metrics are meant to be used by developers, not the other way around – the metric should work for you, you should not have to work for the metric. Metrics should never be an end unto themselves. Metrics are meant to help you think, not to do the thinking for you. <cite>~Alberto Savoia</cite>