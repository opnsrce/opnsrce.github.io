---
title: Getting Started With Buster.js
date: 2013-01-07T00:00:22+00:00
author: Levi Hackwith
layout: post
icy_video_embed_code:
  -
categories:
  - Programming / Web Development
tags:
  - Assert
  - Buster.js
  - JavaScript
  - node.js
  - tdd
  - unit testing
---
<a href="http://www.busterjs.org" target="_blank">Buster.js</a> is a unit testing framework for JavaScript applications. With it, you can write web applications using the <a href="http://en.wikipedia.org/wiki/Test-driven_development" target="_blank">Test Driven Development</a> method which in turn leads to code that is easier to change and maintain.

<!--more-->

## Installing Buster.js

In order to install Buster.js, you first need to install Node.js. Head over to <a href="http://www.nodejs.org" target="_blank">http://www.nodejs.org</a> and click on &#8220;install&#8221;. This should prompt you to download the version most appropriate for your operating system. If that doesn&#8217;t work for you, head over to the <a href="http://nodejs.org/download/" target="_blank">downloads</a> page and manually choose the version you need. Once the install has finished downloading, go ahead and run the installer, moving through each of the setup wizard&#8217;s steps.

Now that you&#8217;ve got Node installed, it&#8217;s time to download Buster.js. To do this, simply pull up a command prompt and type:

`sudo npm install buster -g`

This will install the buster Node module along with the global command line tool. You&#8217;ll notice that I put `sudo` in front of this command. I did this to avoid any permission-related errors I might receive while trying to install Buster.js. If you&#8217;re on a Windows machine, just make sure that you are running the command prompt as an administrator. Okay, now that the Buster.js package is installed, navigate to the directory where you&#8217;re going to be keeping all your JavaScript files and type the following:

`sudo npm link buster`

This will link the buster module to the project.

## Write Your First Unit Test

Now that you&#8217;re all set up with Buster and Node, fire up your favorite text editor, create a new file called `test_number_cruncher.js`, and save it in your project directory. Copy and paste the following code into the file:

<pre class="brush: jscript; title: ; notranslate" title="">var buster = require('buster'),
    NumberCruncher = require('./NumberCruncher');
</pre>

The `require` method pulls a file or &#8216;module&#8217; into another file, similar to the `require` or `include` method&#8217;s in PHP. No extension is used when requesting files this way because every file is assumed to be a JavaScript file with a name equal to the passed in value. So, by passing in a value of &#8220;NumberCruncher&#8221; to the `require` method, you are telling Node to include a file called `NumberCruncher.js`.

Now that that&#8217;s out of the way, it&#8217;s time to create a test case. Go ahead and add the following code to the `test_number_cruncher.js` file:

<pre class="brush: jscript; title: ; notranslate" title="">buster.testCase('Number Cruncher', {
    'can add numbers': function() {
        var numberCruncher = new NumberCruncher();

        buster.assert.equals(8, numberCruncher.add(5,3), 'NumberCruncher cannot add');
    }
});
</pre>

In Buster.js, a test case is an object where each method is a test that will run against your code. For example, if you were writing tests against a `Car` object, you might include tests like &#8216;Can Drive&#8217; or &#8216;Can Stop&#8217;. In the above example, you&#8217;re creating a new instance of the `NumberCruncher` object (more on that later) and testing to make sure that when you pass in the numbers 5 and 3 to the `add` method, you get the number 8. If the `add` method does not return 8, then the test will fail and you&#8217;ll see the message &#8220;NumberCruncher cannot add&#8221; show in the terminal. Let&#8217;s run that test now.

## Run Your (Failing) Test

To run your tests, navigate to the directory containing the test script and type:

`node test_number_cruncher.js`

As expected, the test fails with a pretty serious error message:

``<a href="http://www.busterjs.org" target="_blank">Buster.js</a> is a unit testing framework for JavaScript applications. With it, you can write web applications using the <a href="http://en.wikipedia.org/wiki/Test-driven_development" target="_blank">Test Driven Development</a> method which in turn leads to code that is easier to change and maintain.

<!--more-->

## Installing Buster.js

In order to install Buster.js, you first need to install Node.js. Head over to <a href="http://www.nodejs.org" target="_blank">http://www.nodejs.org</a> and click on &#8220;install&#8221;. This should prompt you to download the version most appropriate for your operating system. If that doesn&#8217;t work for you, head over to the <a href="http://nodejs.org/download/" target="_blank">downloads</a> page and manually choose the version you need. Once the install has finished downloading, go ahead and run the installer, moving through each of the setup wizard&#8217;s steps.

Now that you&#8217;ve got Node installed, it&#8217;s time to download Buster.js. To do this, simply pull up a command prompt and type:

`sudo npm install buster -g`

This will install the buster Node module along with the global command line tool. You&#8217;ll notice that I put `sudo` in front of this command. I did this to avoid any permission-related errors I might receive while trying to install Buster.js. If you&#8217;re on a Windows machine, just make sure that you are running the command prompt as an administrator. Okay, now that the Buster.js package is installed, navigate to the directory where you&#8217;re going to be keeping all your JavaScript files and type the following:

`sudo npm link buster`

This will link the buster module to the project.

## Write Your First Unit Test

Now that you&#8217;re all set up with Buster and Node, fire up your favorite text editor, create a new file called `test_number_cruncher.js`, and save it in your project directory. Copy and paste the following code into the file:

<pre class="brush: jscript; title: ; notranslate" title="">var buster = require('buster'),
    NumberCruncher = require('./NumberCruncher');
</pre>

The `require` method pulls a file or &#8216;module&#8217; into another file, similar to the `require` or `include` method&#8217;s in PHP. No extension is used when requesting files this way because every file is assumed to be a JavaScript file with a name equal to the passed in value. So, by passing in a value of &#8220;NumberCruncher&#8221; to the `require` method, you are telling Node to include a file called `NumberCruncher.js`.

Now that that&#8217;s out of the way, it&#8217;s time to create a test case. Go ahead and add the following code to the `test_number_cruncher.js` file:

<pre class="brush: jscript; title: ; notranslate" title="">buster.testCase('Number Cruncher', {
    'can add numbers': function() {
        var numberCruncher = new NumberCruncher();

        buster.assert.equals(8, numberCruncher.add(5,3), 'NumberCruncher cannot add');
    }
});
</pre>

In Buster.js, a test case is an object where each method is a test that will run against your code. For example, if you were writing tests against a `Car` object, you might include tests like &#8216;Can Drive&#8217; or &#8216;Can Stop&#8217;. In the above example, you&#8217;re creating a new instance of the `NumberCruncher` object (more on that later) and testing to make sure that when you pass in the numbers 5 and 3 to the `add` method, you get the number 8. If the `add` method does not return 8, then the test will fail and you&#8217;ll see the message &#8220;NumberCruncher cannot add&#8221; show in the terminal. Let&#8217;s run that test now.

## Run Your (Failing) Test

To run your tests, navigate to the directory containing the test script and type:

`node test_number_cruncher.js`

As expected, the test fails with a pretty serious error message:

``

While that all seems rather complicated, all it&#8217;s really trying to tell you is that it couldn&#8217;t find the `NumberCruncher` module that was asked for at the top of the file.

## Create the NumberCruncher Object

Go ahead and a create the `NumberCruncher` object now. Create a new file called `NumberCruncher.js` in the project directory and paste in the following code:

<pre class="brush: jscript; title: ; notranslate" title="">var NumberCruncher = (function() {
    var N = function() {};

    N.prototype = {
        constructor: N,
        add: function() {
            return 8;
        }
    }
    return N;
}());
</pre>

Run the test again:

 `Number Cruncher: .`

1 test case, 1 test, 1 assertion, 0 failures, 0 errors, 0 timeouts

Because you&#8217;ve created the missing module, the test passes.

One thing you&#8217;ve probably noticed by now is that the `add` method in the `NumberCruncher` object doesn&#8217;t actually add any numbers together. Instead, it simply returns the value that the test written earlier expects: 8. The reason for this is found within the 3rd stage of test-driven development states (emphasis mine):

> ..Write some code that will cause the test to pass. The new **code written at this stage will not be perfect** and may, for example, pass the test in an inelegant way. That is acceptable because later steps will improve and hone it. **It is important that the code written is only designed to pass the test; no further**&#8230;

Now that you&#8217;ve written code that makes your test pass, it&#8217;s time to refactor it.

## Refactoring the code

Replace the code in `NumberCruncher.js` with the following:

<pre class="brush: jscript; title: ; notranslate" title="">var NumberCruncher = (function() {
    var N = function() {};

    N.prototype = {
        constructor: N,
        add: function() {
            var sum = 0,
                len,
                i;

            for (len = arguments.length - 1, i = len; i &gt;= 0; i--) {
                sum += arguments[i];
            }

            return sum;
        }
    }
    return N;
}());

module.exports = NumberCruncher;
</pre>

Now the `add` method can return the sum of any numbers passed into it. See what happens when you rerun the test:

 `Number Cruncher: .`

1 test case, 1 test, 1 assertion, 0 failures, 0 errors, 0 timeouts

It still passes.

## Unit Tests: Protection from Bad Code

In addition to making it easier to refactor code while still guaranteeing it returns the expected results, Buster.js and test-driven development can also protect your application against bad code. Pretend you&#8217;re a new developer who just has no clue what the `add` method is supposed to do. Replace the code in `NumberCruncher.js` with the following:

<pre class="brush: jscript; title: ; notranslate" title="">var NumberCruncher = (function() {
    var N = function() {};

    N.prototype = {
        constructor: N,
        add: function() {
            var product = 1,
                len,
                i;

            for (len = arguments.length - 1, i = len; i &gt;= 0; i--) {
                product *= arguments[i];
            }

            return product;
        }
    }
    return N;
}());

module.exports = NumberCruncher;
</pre>

Here, the `add` method has been altered so it multiplies the passed in numbers instead of adding them together. See what happens when you run your unit tests:

`<br />
Number Cruncher: F`

Failure: Number Cruncher can add numbers

[assert.equals] NumberCruncher cannot add: 15 expected to be equal to 8

at Object.buster.testCase.can add numbers (./test/test\_number\_cruncher.js:7:23)

1 test case, 1 test, 1 assertion, 1 failure, 0 errors, 0 timeouts

The test against the `add` method has failed and Buster.js has output some information that should help you solve the problem. The letter F lets you know that the test failed. In addition, the file name and line number of the failed test as well as the custom error message are included. In this example, however, all the information isn&#8217;t really necessary to solve the problem. As a developer, you&#8217;d have to be pretty oblivious to not realize that the `add` method should add numbers together, not multiply them. However, there&#8217;s a bigger picture to this example. Imagine if you were working on a much more complicated object whose methods had multiple logic paths that performed several operations. As your code grows in size and complexity, so does the potential for bugs. By creating unit tests against your code, you&#8217;re allowing even the most inexperienced developer the ability to make sweeping modifications while still guaranteeing the expectations of your code&#8217;s behavior are still being met.

Well, I hope that this quick introduction to Buster.js inspires you install it and use it against your own JavaScript projects.