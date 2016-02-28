---
title: Order Your Methods to Add Clarity to Your Code
date: 2012-01-30T00:00:39+00:00
author: Levi Hackwith
excerpt: 'In general we want function call dependencies to point in the
downward direction. That is, a function that is called should be below a
function that does the calling.2This creates a nice flow down the source code
module from high level to low level.'
code: true
layout: post
categories:
  - Programming / Web Development
tags:
  - Clean Code
  - Code Formatting
  - PHP
  - Robert Martin
---
[1]: http://www.amazon.com/Clean-Code-Handbook-Craftsmanship-ebook/dp/B001GSTOAM/ref=tmm_kin_title_0?ie=UTF8&m=AG56TWVU5XWC2

Recently I&rsquo;ve been reading _[Clean Code][1]_ by Robert C Martin and come
across this wonderful piece of programming advice from Chapter 5:

> In general we want function call dependencies to point in the downward
> direction. That is, a function that is called should be below a function that
> does the calling.This creates a nice flow down the source code module from
> high level to low level.
>
> As in newspaper articles, we expect the most important concepts to come
> first, and we expect them to be expressed with the least amount of polluting
> detail. We expect the low-level details to come last. This allows us to skim
> source files, getting the gist from the first few functions, without having
> to immerse ourselves in the details.

<!--more-->



When I first read this, I was just stunned. During my career I&rsquo;ve
encountered (and written) classes that were very difficult to read and follow
despite their methods being well-written and documented. It wasn&rsquo;t until
 I&rsquo;d discovered this piece of coding advice, that I understood why.

To illustrate the point Mr. Martin is trying to make, let&rsquo;s take a look
at an example class I put together:

~~~php

<?php
class SalesReport {

    private $startDate = '';
    private $endDate = '';
    private $salesQuarter = 0;
    private $salesTeamMembers = array();

    public function setEndDate($date) {
        $this->endDate = $date;
    }

    public function __construct() {

    }

    public function setStartDate($date) {
        $this->startDate = $date;
    }

    public function setSalesTeamMembers($teamMemberIds) {
        if(is_array($teamMemberIds)) {
            $this->salesTeamMembers = $teamMemberIds;
        } else {
            throw new Exception('SalesReport::setSalesTeamMembers only ' .
                'accepts an array of team member ids');
        }
    }

    public function generateReportQueryLimitClause() {
        // Generate Limit clause
    }

    public function generate() {
        $whereClause = $this->generateReportQueryWhereClause();
        $orderByClause = $this->generateReportQueryOrderByClause();
        $limitClause = $this->generateReportQueryLimitClause();
        $query = "
            SELECT
                /* Field Listing */
            FROM
                sales
            $whereClause
            $orderByClause
            $limitClause
        ";
        // execute query
        return TRUE;
    }

    public function generateReportQueryWhereClause() {
        // Generate WHERE clause based on report selection criteria
    }

    public function generateReportQueryOrderByClause() {
        // Generate ORDER BY clause
    }

    public function load() {
        // Load report results from temporary table
    }

    public function setSalesQuarter($salesQuarter) {
        if(is_int($salesQuarter)) {
            $this->salesQuarter = $salesQuarter;
        } else {
            throw new Exception('Sales Quarter must be an integer');
        }
    }

}
?>
~~~

Take a glance at the above class. Do you notice how your eyes have to keep
jumping around the class in order to follow what&rsquo;s going on? By having
the methods randomly scattered throughout the code, you really have to focus
in on (and possibly get lost in) the details of the code.  Now let&rsquo;s
rearrange the methods of the class to more closely match the order in which
things are called and referenced:

~~~php
<?php
class SalesReport {

    private $startDate = '';
    private $endDate = '';
    private $salesQuarter = 0;
    private $salesTeamMembers = array();

    public function __construct() {

    }

    public function setEndDate($date) {
        $this->endDate = $date;
    }

    public function setStartDate($date) {
        $this->startDate = $date;
    }

    public function setSalesQuarter($salesQuarter) {
        if(is_int($salesQuarter)) {
            $this->salesQuarter = $salesQuarter;
        } else {
            throw new Exception('Sales Quarter must be an integer');
        }
    }

    public function setSalesTeamMembers($teamMemberIds) {
        if(is_array($teamMemberIds)) {
            $this->salesTeamMembers = $teamMemberIds;
        } else {
            throw new Exception('SalesReport::setSalesTeamMembers only ' .
                'accepts an array of team member ids');
        }
    }

    public function generate() {
        $whereClause = $this->generateReportQueryWhereClause();
        $orderByClause = $this->generateReportQueryOrderByClause();
        $limitClause = $this->generateReportQueryLimitClause();
        $query = "
            SELECT
                /* Field Listing */
            FROM
                sales
            $whereClause
            $orderByClause
            $limitClause
        ";
        // execute query
        return TRUE;
    }

    public function generateReportQueryWhereClause() {
        // Generate WHERE clause based on report selection criteria
    }

    public function generateReportQueryOrderByClause() {
        // Generate ORDER BY clause
    }

    public function generateReportQueryLimitClause() {
        // Generate Limit clause
    }

    public function load() {
        // Load report results from temporary table
    }
}
?>
~~~

See the difference? Notice how the code naturally flows from one method to the
next, allowing you to quickly ascertain what the class is doing and when
it&rsquo;s doing it. By ordering the methods so the calling method (caller) is
declared before the method being called (callee), you drastically increase
your code&rsquo;s readability.