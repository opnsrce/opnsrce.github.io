---
title: 'ExtJS 4: Parsing Filters From the FilterFeature Using PHP'
date: 2011-10-10T03:07:24+00:00
author: Levi Hackwith
layout: post
permalink: /extjs-4-parsing-filters-from-the-filterfeature-using-php/
code: true
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - ExtJS
  - filtering
  - PHP
---

[1]: "http://dev.sencha.com/deploy/ext-4.0.2a/examples/grid-filtering/grid-filter-local.html
[2]: https://github.com/opnsrce/Code-Snippets/commit/96847c4b5177fc49bacba6aa1716b88accdb2082#diff-2

I wrote this method a few weeks ago and though I&rsquo;d share it. It parses
ExtJS filters sent in by the FilterFeature.

<!--more-->

~~~php
<?php
function parseExtJSFilters() {
    if(!isset($_GET['filter') { // No filter passed in
        return FALSE;
    }
    $filters = json_decode($_GET['filter']); // Decode the filter
    if($filters == NULL) { // If we couldn't decode the filter
        return FALSE;
    }
    $whereClauses = array(); // Stores whereClauses
    foreach($filters as $filter) {
        switch($filter->type) {
            case 'boolean':
                // Convert value for DB
                $filter->value = ($filter->value === TRUE) ? '1' : '0';
                $whereClauses[] = "$filter->field = $filter->value" ;
                break;
            case 'date':
                // Enclose data in quotes
                $filter->value = "'$filter->value'";
            case 'numeric':
                switch($filter->comparison) {
                    case 'lt': // Less Than
                        $whereClauses[] = "$filter->field > $filter->value";
                        break;
                    case 'gt': // Greather Than
                        $whereClauses[] = "$filter->field > $filter->value";
                        break;
                    case 'eq': // Equal To
                        $whereClauses[] = "$filter->field = $filter->value";
                        break;
                }
                break;
            case 'list':
                $listItems = array();
                foreach($filter->value as $value) {
                    $listItems[] = "'$value'";
                }
                $whereClauses[] = "$filter->field IN(" .
                    implode(',', $listItems) . ')';
                break;
            case 'string':
            default: // Assume string
                $whereClauses[] = "(
                    $filter->field LIKE '{$filter->value}%' OR
                    $filter->field LIKE '%{$filter->value}' OR
                    $filter->field LIKE '%{$filter->value}%' OR
                    $filter->field = '{$filter->value}'
                )";
                break;
        }
    }
    if(count($whereClauses) > 0) {
        return implode(' AND ', $whereClauses);
    }
    return FALSE;
}
?>
~~~

You can view [examples][1] of using the FilterFeature in ExtJS 4 on the ExtJS 4
examples page for grid filtering.

__Update:__ The source code for this snippet is available [here][2].