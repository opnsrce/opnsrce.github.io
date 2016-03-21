---
title: Using Business Modules to Improve Code Clarity and Maintenance
excerpt: 'As our applications grow in complexity, it becomes harder and harder
to document and maintain the expected functionality of an application as well as
figure out what to write unit tests against and what to leave for the automated
QA testing.'
date: 2016-03-19T00:00:00+00:00
author: Levi Hackwith
layout: post
code: true
categories:
  - Programming / Web Development
tags:
  - business module
  - unit testing
---

As our applications grow in complexity, it becomes harder and harder to
document and maintain the expected functionality of an application as well as
figure out what to write unit tests against and what to leave for the automated
QA testing.

In order to combat these problems, we can use business modules to centralize our
application&rsquo;s logic and provide clear documentation of what the expected
functionality of our application is as changes are made over time.

## What is Business Logic

&ldquo;Business Logic&rdquo; means any result that is derived from multiple
pieces of data or from data not specific to the value we're trying to
determine. For example:

~~~js
// Some JSON data we got back from the server
var apiResponse = {...};
var user = apiResponse.user;
var isAuthed = user.isAuthed;
var hasBracket = user.hasBracket;
var isQualified = user.isQualified;

if(isAuthed === true hasBracket === true && isQualified === true) {
    // Show banner congratulating user on the fact that they're still
    // qualified
}
~~~

Here, we're deriving a result from multiple pieces of data sent from the server:
whether or not to show the &ldquo;congratulations&rdquo; banner.

Because we're deciding whether or not to show the banner based on three separate
pieces of data and not based on avalue specific to what we're trying to
determine, this piece of code is considered business logic and belongs in a
business logic module.

However, if we were determining whether or not show the banner based on a
specific value from the API response

~~~js
var apiResponse = {...};

if(apiResponse.shouldShowBanner === true) {
    // Show banner congratulating user on the fact that they're still
    // qualified
}
~~~

we would not consider this to be business logic and would leave this code as-is.
Because we're checking a value specific to what we're trying to determine (
whether or not to show the banner), that logic is not going to change over time
(at least not on the client) and doesn't need to be moved into a business
module.

## What Isn't Business Logic

Any piece of logic whose result is verified visually is not business logic. In
our previous example, the call to check whether or not to show the banner is
business logic. The code that actually displays that banner correctly is not
business logic since it would be verified by opening up the browser and checking
whether or not the banner displayed properly.

## How to Create a Business Module

Here's how you would convert the logic to show / hide the banner into a business
module:

~~~js
// business.js

module.exports.shouldShowBanner = function(isAuthed, hasBracket, isQualified) {
    return (isAuthed === true && hasBracked === true && isQualified === true);
}
~~~

~~~js
// banner.js
var businessLogic = require('business.js');
var apiResponse = {...};
var user = apiResponse.user;
var isAuthed = user.isAuthed;
var hasBracket = user.hasBracket;
var isQualified = user.isQualified;

if(businessLogic.shouldShowBanner(isAuthed, hasBracket, isQualified) === true) {
    // Manipulate the DOM to show the banner
}
~~~

From here we can easily write unit tests against the business module to verify
that we've met the requirements of the project:

~~~js
// banner-test.js

var businessLogic = require('./business.js');

describe('shouldShowBanner', function() {
    it('should return true if the user is not authenticated', function() {
        expect(businessLogic.shouldShowBanner(false, true, true)).to.be.true;
    });
    ...
})
~~~

## Why You Should Use Business Modules

Business modules make code more reusable, testable, and easier to maintain. In
addition, there's a side-benefit that is often overlooked: it gives project
managers and future developers a centralized place to look in order to figure
out how an application is meant to function. I can't tell you how many times
I've looked at a bug report and asked &ldquo;Right, but how is it _supposed_
to work?&rdquo; Business modules help answer that question when it comes time
to make changes to the code.

## TL;DR

 - Business logic is functionality based off of a derived result
 - Business modules centralize business logic, making code easier to maintain
 - Write unit tests against business logic, not application functionality
