---
id: 189
title: How to Run Buster.js Unit Tests in (and Against) the Browser
date: 2013-01-21T00:00:54+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=189
permalink: /how-to-run-buster-js-unit-tests-in-and-against-the-browser/
icy_video_embed_code:
  - 
categories:
  - Programming / Web Development
tags:
  - Browser
  - Buster.js
  - JavaScript
  - unit testing
---
[Previously](http://www.levihackwith.com/getting-started-with-buster-js/ "Getting Started With Buster.js"), I gave a brief introduction to Buster.js and how it&#8217;s used. Today, I&#8217;m going to show you how to set up Buster.js to run tests against a browser as well as how to use `setUp` and `tearDown` to reduce redundancy in your unit tests.

<!--more-->

## A Quick Review

As a refresher, let&#8217;s bring up our `NumberCruncher` object from the previous lesson:

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

As well as the unit test for the `add` method:

<pre class="brush: jscript; title: ; notranslate" title="">var buster = require('buster'),
    NumberCruncher = require('./NumberCruncher');

buster.testCase('Number Cruncher', {
    'can add numbers': function() {
        var numberCruncher = new NumberCruncher();

        buster.assert.equals(8, numberCruncher.add(5,3), 'NumberCruncher cannot add');
    }
});
</pre>

Previously, the tests got run straight from the terminal. Now you&#8217;ll be configuring Buster to run your tests in and against a browser.

## Configure Buster for the Browser

The first step is to set up the config file. This tells Buster where to find all the files it needs to run your tests properly. Go ahead and create a file called `buster.js` in the project directory. Also, create two folders called `src` and `test` and move the `NumberCruncher.js` and `test_numberCruncer.js` files into them, respectively.

Now that that&#8217;s out of the way, go ahead and paste the following code into the `buster.js` file:

<pre class="brush: jscript; title: ; notranslate" title="">var config = module.exports;

config['NumberCruncher Tests'] = {
    rootPath: '../',
    environment: 'browser',
    sources: [
        'src/NumberCruncher.js'
    ],
    tests: [
        'test/test_*.js'
    ]
};
</pre>

The `buster.js` file is a config file that tells Buster where to start looking for the files required to run the test (`rootPath`), what environment the tests will be run in (`environment`), what files will be tested (`sources`), and what tests are will be run (`tests`). I&#8217;d also like to point out that both the `sources` and `tests` config parameters take wildcard values. In the example above, the `tests` parameter has a wildcard for its first and only value that makes sure that any JavaScript files in the `test` directory that that start with &#8220;test_&#8221; get run as a unit test. Speaking of unit tests, go ahead and _remove_ the following lines from the `test_number_cruncher.js` file:

<pre class="brush: jscript; title: ; notranslate" title="">var buster = require('buster'),
    NumberCruncher = require('./NumberCruncher');
</pre>

Because everything is going to be included via the config file, you no longer need to explicitly include either Buster or the `NumberCruncher` object in your unit test files.

## Booting Up the Buster.js Server

To make testing against multiple browsers as easy as possible, Buster.js comes with its own test server that each browser being tested can connect to. Go ahead and start up the test server by opening up a terminal, navigating to the directory where you are keeping all the files related to this project, and typing the following:

`buster server`

If everything runs smoothly, you should see the following in your terminal:

`buster-server running on http://localhost:1111`

What this means is that Buster has launched a server on port `1111` on your local machine. Go ahead and open up a new browser window and navigate to `http://localhost:1111`. You should see something similar to this:

<a href="http://www.levihackwith.com/?attachment_id=193" rel="attachment wp-att-193"><img class="aligncenter size-full wp-image-193" alt="buster server" src="http://www.levihackwith.com/wp-content/uploads/2013/01/buster-server.png" width="825" height="280" /></a>

Go ahead and click the &#8220;capture&#8221; button. This &#8220;captures&#8221; your browser and lets Buster know that it has at least one environment to test against. If you wish to test against multiple browsers, just open up each browser and repeat the capture process. Once that&#8217;s done, open up a _new_ terminal window, navigate to the project, and type the following:

`buster test`

This fires up Buster and makes it run through all the tests listed in the config file. If everything is configured properly, you should see something like this:``[Previously](http://www.levihackwith.com/getting-started-with-buster-js/ "Getting Started With Buster.js"), I gave a brief introduction to Buster.js and how it&#8217;s used. Today, I&#8217;m going to show you how to set up Buster.js to run tests against a browser as well as how to use `setUp` and `tearDown` to reduce redundancy in your unit tests.

<!--more-->

## A Quick Review

As a refresher, let&#8217;s bring up our `NumberCruncher` object from the previous lesson:

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

As well as the unit test for the `add` method:

<pre class="brush: jscript; title: ; notranslate" title="">var buster = require('buster'),
    NumberCruncher = require('./NumberCruncher');

buster.testCase('Number Cruncher', {
    'can add numbers': function() {
        var numberCruncher = new NumberCruncher();

        buster.assert.equals(8, numberCruncher.add(5,3), 'NumberCruncher cannot add');
    }
});
</pre>

Previously, the tests got run straight from the terminal. Now you&#8217;ll be configuring Buster to run your tests in and against a browser.

## Configure Buster for the Browser

The first step is to set up the config file. This tells Buster where to find all the files it needs to run your tests properly. Go ahead and create a file called `buster.js` in the project directory. Also, create two folders called `src` and `test` and move the `NumberCruncher.js` and `test_numberCruncer.js` files into them, respectively.

Now that that&#8217;s out of the way, go ahead and paste the following code into the `buster.js` file:

<pre class="brush: jscript; title: ; notranslate" title="">var config = module.exports;

config['NumberCruncher Tests'] = {
    rootPath: '../',
    environment: 'browser',
    sources: [
        'src/NumberCruncher.js'
    ],
    tests: [
        'test/test_*.js'
    ]
};
</pre>

The `buster.js` file is a config file that tells Buster where to start looking for the files required to run the test (`rootPath`), what environment the tests will be run in (`environment`), what files will be tested (`sources`), and what tests are will be run (`tests`). I&#8217;d also like to point out that both the `sources` and `tests` config parameters take wildcard values. In the example above, the `tests` parameter has a wildcard for its first and only value that makes sure that any JavaScript files in the `test` directory that that start with &#8220;test_&#8221; get run as a unit test. Speaking of unit tests, go ahead and _remove_ the following lines from the `test_number_cruncher.js` file:

<pre class="brush: jscript; title: ; notranslate" title="">var buster = require('buster'),
    NumberCruncher = require('./NumberCruncher');
</pre>

Because everything is going to be included via the config file, you no longer need to explicitly include either Buster or the `NumberCruncher` object in your unit test files.

## Booting Up the Buster.js Server

To make testing against multiple browsers as easy as possible, Buster.js comes with its own test server that each browser being tested can connect to. Go ahead and start up the test server by opening up a terminal, navigating to the directory where you are keeping all the files related to this project, and typing the following:

`buster server`

If everything runs smoothly, you should see the following in your terminal:

`buster-server running on http://localhost:1111`

What this means is that Buster has launched a server on port `1111` on your local machine. Go ahead and open up a new browser window and navigate to `http://localhost:1111`. You should see something similar to this:

<a href="http://www.levihackwith.com/?attachment_id=193" rel="attachment wp-att-193"><img class="aligncenter size-full wp-image-193" alt="buster server" src="http://www.levihackwith.com/wp-content/uploads/2013/01/buster-server.png" width="825" height="280" /></a>

Go ahead and click the &#8220;capture&#8221; button. This &#8220;captures&#8221; your browser and lets Buster know that it has at least one environment to test against. If you wish to test against multiple browsers, just open up each browser and repeat the capture process. Once that&#8217;s done, open up a _new_ terminal window, navigate to the project, and type the following:

`buster test`

This fires up Buster and makes it run through all the tests listed in the config file. If everything is configured properly, you should see something like this:`` 
  
Which, if you remember from the previous lesson, means that all the unit tests are passing.

## Expanding the `NumberCruncher` Object

Before continuing on, go ahead and add a method called `multiply` to the `NumberCruncher` object. Replace the code in `NumberCruncher.js` with the following:

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
        },
        multiply: function() {
            var product = 1,
                len,
                i;

            for (len = arguments.length - 1, i = len; i &gt;= 0; i--) {
                product = product * arguments[i];
            }

            return product;
        }
    }
    return N;
}());
</pre>

Also add in the necessary unit tests for the new method:

<pre class="brush: jscript; title: ; notranslate" title="">buster.testCase('Number Cruncher', {
    'can add numbers': function() {
        var numberCruncher = new NumberCruncher();

        buster.assert.equals(8, numberCruncher.add(5,3), 'NumberCruncher cannot add');
    },
    'can multiply numbers': function() {
        var numberCruncher = new NumberCruncher();

        buster.assert.equals(15, numberCruncher.multiply(5,3), 'NumberCruncher cannot multiply');
    }
});
</pre>

## Reducing Redundancy with `setUp()` and `tearDown()`

Take a close look at the updated code in `test_number_cruncher.js`. Notice anything amiss? Look at the opening lines of each tests: they&#8217;re the same. Every time a test is added to the file, a new instance of the `NumberCruncher` object is created. To remove this code redundancy, you can use `setUp` and `tearDown` methods.

When Buster.js prepares to run a testcase, it looks for two methods: `setUp` and `tearDown`. The `setUp` method gets called _before_ each individual test is run and `tearDown` gets run _after_ each individual test is run. Since since a new instance of the `NumberCruncher` object needs to be created for each test, it&#8217;s safe to move the instantiation logic into the `setUp` method. In addition, you can add some garbage collection logic to the `tearDown` method to help guarantee that we get rid of any references to `NumberCruncher` after each test:

<pre class="brush: jscript; title: ; notranslate" title="">buster.testCase('Number Cruncher', {
    setUp: function() {
        var numberCruncher = new NumberCruncher();
    },
    tearDown: function() {
        numberCruncher = nothing
    },
    'can add numbers': function() {
        buster.assert.equals(8, numberCruncher.add(5,3), 'NumberCruncher cannot add');
    },
    'can multiply numbers': function() {
        buster.assert.equals(15, numberCruncher.multiply(5,3), 'NumberCruncher cannot multiply');
    }
});
</pre>

Rerun the tests using same `buster test` command used earlier:
  
```[Previously](http://www.levihackwith.com/getting-started-with-buster-js/ "Getting Started With Buster.js"), I gave a brief introduction to Buster.js and how it&#8217;s used. Today, I&#8217;m going to show you how to set up Buster.js to run tests against a browser as well as how to use `setUp` and `tearDown` to reduce redundancy in your unit tests.

<!--more-->

## A Quick Review

As a refresher, let&#8217;s bring up our `NumberCruncher` object from the previous lesson:

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

As well as the unit test for the `add` method:

<pre class="brush: jscript; title: ; notranslate" title="">var buster = require('buster'),
    NumberCruncher = require('./NumberCruncher');

buster.testCase('Number Cruncher', {
    'can add numbers': function() {
        var numberCruncher = new NumberCruncher();

        buster.assert.equals(8, numberCruncher.add(5,3), 'NumberCruncher cannot add');
    }
});
</pre>

Previously, the tests got run straight from the terminal. Now you&#8217;ll be configuring Buster to run your tests in and against a browser.

## Configure Buster for the Browser

The first step is to set up the config file. This tells Buster where to find all the files it needs to run your tests properly. Go ahead and create a file called `buster.js` in the project directory. Also, create two folders called `src` and `test` and move the `NumberCruncher.js` and `test_numberCruncer.js` files into them, respectively.

Now that that&#8217;s out of the way, go ahead and paste the following code into the `buster.js` file:

<pre class="brush: jscript; title: ; notranslate" title="">var config = module.exports;

config['NumberCruncher Tests'] = {
    rootPath: '../',
    environment: 'browser',
    sources: [
        'src/NumberCruncher.js'
    ],
    tests: [
        'test/test_*.js'
    ]
};
</pre>

The `buster.js` file is a config file that tells Buster where to start looking for the files required to run the test (`rootPath`), what environment the tests will be run in (`environment`), what files will be tested (`sources`), and what tests are will be run (`tests`). I&#8217;d also like to point out that both the `sources` and `tests` config parameters take wildcard values. In the example above, the `tests` parameter has a wildcard for its first and only value that makes sure that any JavaScript files in the `test` directory that that start with &#8220;test_&#8221; get run as a unit test. Speaking of unit tests, go ahead and _remove_ the following lines from the `test_number_cruncher.js` file:

<pre class="brush: jscript; title: ; notranslate" title="">var buster = require('buster'),
    NumberCruncher = require('./NumberCruncher');
</pre>

Because everything is going to be included via the config file, you no longer need to explicitly include either Buster or the `NumberCruncher` object in your unit test files.

## Booting Up the Buster.js Server

To make testing against multiple browsers as easy as possible, Buster.js comes with its own test server that each browser being tested can connect to. Go ahead and start up the test server by opening up a terminal, navigating to the directory where you are keeping all the files related to this project, and typing the following:

`buster server`

If everything runs smoothly, you should see the following in your terminal:

`buster-server running on http://localhost:1111`

What this means is that Buster has launched a server on port `1111` on your local machine. Go ahead and open up a new browser window and navigate to `http://localhost:1111`. You should see something similar to this:

<a href="http://www.levihackwith.com/?attachment_id=193" rel="attachment wp-att-193"><img class="aligncenter size-full wp-image-193" alt="buster server" src="http://www.levihackwith.com/wp-content/uploads/2013/01/buster-server.png" width="825" height="280" /></a>

Go ahead and click the &#8220;capture&#8221; button. This &#8220;captures&#8221; your browser and lets Buster know that it has at least one environment to test against. If you wish to test against multiple browsers, just open up each browser and repeat the capture process. Once that&#8217;s done, open up a _new_ terminal window, navigate to the project, and type the following:

`buster test`

This fires up Buster and makes it run through all the tests listed in the config file. If everything is configured properly, you should see something like this:``[Previously](http://www.levihackwith.com/getting-started-with-buster-js/ "Getting Started With Buster.js"), I gave a brief introduction to Buster.js and how it&#8217;s used. Today, I&#8217;m going to show you how to set up Buster.js to run tests against a browser as well as how to use `setUp` and `tearDown` to reduce redundancy in your unit tests.

<!--more-->

## A Quick Review

As a refresher, let&#8217;s bring up our `NumberCruncher` object from the previous lesson:

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

As well as the unit test for the `add` method:

<pre class="brush: jscript; title: ; notranslate" title="">var buster = require('buster'),
    NumberCruncher = require('./NumberCruncher');

buster.testCase('Number Cruncher', {
    'can add numbers': function() {
        var numberCruncher = new NumberCruncher();

        buster.assert.equals(8, numberCruncher.add(5,3), 'NumberCruncher cannot add');
    }
});
</pre>

Previously, the tests got run straight from the terminal. Now you&#8217;ll be configuring Buster to run your tests in and against a browser.

## Configure Buster for the Browser

The first step is to set up the config file. This tells Buster where to find all the files it needs to run your tests properly. Go ahead and create a file called `buster.js` in the project directory. Also, create two folders called `src` and `test` and move the `NumberCruncher.js` and `test_numberCruncer.js` files into them, respectively.

Now that that&#8217;s out of the way, go ahead and paste the following code into the `buster.js` file:

<pre class="brush: jscript; title: ; notranslate" title="">var config = module.exports;

config['NumberCruncher Tests'] = {
    rootPath: '../',
    environment: 'browser',
    sources: [
        'src/NumberCruncher.js'
    ],
    tests: [
        'test/test_*.js'
    ]
};
</pre>

The `buster.js` file is a config file that tells Buster where to start looking for the files required to run the test (`rootPath`), what environment the tests will be run in (`environment`), what files will be tested (`sources`), and what tests are will be run (`tests`). I&#8217;d also like to point out that both the `sources` and `tests` config parameters take wildcard values. In the example above, the `tests` parameter has a wildcard for its first and only value that makes sure that any JavaScript files in the `test` directory that that start with &#8220;test_&#8221; get run as a unit test. Speaking of unit tests, go ahead and _remove_ the following lines from the `test_number_cruncher.js` file:

<pre class="brush: jscript; title: ; notranslate" title="">var buster = require('buster'),
    NumberCruncher = require('./NumberCruncher');
</pre>

Because everything is going to be included via the config file, you no longer need to explicitly include either Buster or the `NumberCruncher` object in your unit test files.

## Booting Up the Buster.js Server

To make testing against multiple browsers as easy as possible, Buster.js comes with its own test server that each browser being tested can connect to. Go ahead and start up the test server by opening up a terminal, navigating to the directory where you are keeping all the files related to this project, and typing the following:

`buster server`

If everything runs smoothly, you should see the following in your terminal:

`buster-server running on http://localhost:1111`

What this means is that Buster has launched a server on port `1111` on your local machine. Go ahead and open up a new browser window and navigate to `http://localhost:1111`. You should see something similar to this:

<a href="http://www.levihackwith.com/?attachment_id=193" rel="attachment wp-att-193"><img class="aligncenter size-full wp-image-193" alt="buster server" src="http://www.levihackwith.com/wp-content/uploads/2013/01/buster-server.png" width="825" height="280" /></a>

Go ahead and click the &#8220;capture&#8221; button. This &#8220;captures&#8221; your browser and lets Buster know that it has at least one environment to test against. If you wish to test against multiple browsers, just open up each browser and repeat the capture process. Once that&#8217;s done, open up a _new_ terminal window, navigate to the project, and type the following:

`buster test`

This fires up Buster and makes it run through all the tests listed in the config file. If everything is configured properly, you should see something like this:`` 
  
Which, if you remember from the previous lesson, means that all the unit tests are passing.

## Expanding the `NumberCruncher` Object

Before continuing on, go ahead and add a method called `multiply` to the `NumberCruncher` object. Replace the code in `NumberCruncher.js` with the following:

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
        },
        multiply: function() {
            var product = 1,
                len,
                i;

            for (len = arguments.length - 1, i = len; i &gt;= 0; i--) {
                product = product * arguments[i];
            }

            return product;
        }
    }
    return N;
}());
</pre>

Also add in the necessary unit tests for the new method:

<pre class="brush: jscript; title: ; notranslate" title="">buster.testCase('Number Cruncher', {
    'can add numbers': function() {
        var numberCruncher = new NumberCruncher();

        buster.assert.equals(8, numberCruncher.add(5,3), 'NumberCruncher cannot add');
    },
    'can multiply numbers': function() {
        var numberCruncher = new NumberCruncher();

        buster.assert.equals(15, numberCruncher.multiply(5,3), 'NumberCruncher cannot multiply');
    }
});
</pre>

## Reducing Redundancy with `setUp()` and `tearDown()`

Take a close look at the updated code in `test_number_cruncher.js`. Notice anything amiss? Look at the opening lines of each tests: they&#8217;re the same. Every time a test is added to the file, a new instance of the `NumberCruncher` object is created. To remove this code redundancy, you can use `setUp` and `tearDown` methods.

When Buster.js prepares to run a testcase, it looks for two methods: `setUp` and `tearDown`. The `setUp` method gets called _before_ each individual test is run and `tearDown` gets run _after_ each individual test is run. Since since a new instance of the `NumberCruncher` object needs to be created for each test, it&#8217;s safe to move the instantiation logic into the `setUp` method. In addition, you can add some garbage collection logic to the `tearDown` method to help guarantee that we get rid of any references to `NumberCruncher` after each test:

<pre class="brush: jscript; title: ; notranslate" title="">buster.testCase('Number Cruncher', {
    setUp: function() {
        var numberCruncher = new NumberCruncher();
    },
    tearDown: function() {
        numberCruncher = nothing
    },
    'can add numbers': function() {
        buster.assert.equals(8, numberCruncher.add(5,3), 'NumberCruncher cannot add');
    },
    'can multiply numbers': function() {
        buster.assert.equals(15, numberCruncher.multiply(5,3), 'NumberCruncher cannot multiply');
    }
});
</pre>

Rerun the tests using same `buster test` command used earlier:
  
``` 
  
Uh-oh. What went wrong? Well, if you take a look at the code, you&#8217;ll notice that the `numberCruncher` variable is declared locally inside the `setUp` method. It appears that removing the redundant object instantiation from each test has also removed the object from the necessary scope required to run the tests. To remedy this, the instance of the `numberCruncher` object needs to be made a property of the testcase:

<pre class="brush: jscript; title: ; notranslate" title="">buster.testCase('Number Cruncher', {
    setUp: function() {
        this.numberCruncher = new NumberCruncher();
    },
    tearDown: function() {
        delete this.numberCruncher
    },
    'can add numbers': function() {
        buster.assert.equals(8, this.numberCruncher.add(5,3), 'NumberCruncher cannot add');
    },
    'can multiply numbers': function() {
        buster.assert.equals(15, this.numberCruncher.multiply(5,3), 'NumberCruncher cannot multiply');
    }
});
</pre>

Now when we rerun the tests, everything should pass as expected.

Well, I hope I&#8217;ve opened your eyes to all the possibilites there are with unit testing and Buster.js. Keep in mind that browser testing isn&#8217;t just limited to what&#8217;s on your machine. Any browser, even mobile devices, can connect to the server and be tested against.