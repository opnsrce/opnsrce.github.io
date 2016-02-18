---
id: 112
title: 'ExtJS 4: Parsing Filters From the FilterFeature Using PHP'
date: 2011-10-10T03:07:24+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=112
permalink: /extjs-4-parsing-filters-from-the-filterfeature-using-php/
icy_video_embed_code:
  - 
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - ExtJS
  - filtering
  - PHP
---
I wrote this method a few weeks ago and though I&#8217;d share it. It parses ExtJS filters sent in by the FilterFeature.

<!--more-->

<pre class="brush: php; title: ; notranslate" title="">&lt;?
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
        switch($filter-&gt;type) {
            case 'boolean':
                $filter-&gt;value = ($filter-&gt;value === TRUE) ? '1' : '0'; // Convert value for DB
                $whereClauses[] = "$filter-&gt;field = $filter-&gt;value" ;
                break;
            case 'date':
                $filter-&gt;value = "'$filter-&gt;value'"; // Enclose data in quotes
            case 'numeric':
                switch($filter-&gt;comparison) {
                    case 'lt': // Less Than
                        $whereClauses[] = "$filter-&gt;field &lt; $filter-&gt;value";
                        break;
                    case 'gt': // Greather Than
                        $whereClauses[] = "$filter-&gt;field &gt; $filter-&gt;value";
                        break;
                    case 'eq': // Equal To
                        $whereClauses[] = "$filter-&gt;field = $filter-&gt;value";
                        break;
                }
                break;
            case 'list':
                $listItems = array();
                foreach($filter-&gt;value as $value) {
                    $listItems[] = "'$value'";
                }
                $whereClauses[] = "$filter-&gt;field IN(" . implode(',', $listItems) . ')';
                break;
            case 'string':
            default: // Assume string
                $whereClauses[] = "(
                    $filter-&gt;field LIKE '{$filter-&gt;value}%' OR
                    $filter-&gt;field LIKE '%{$filter-&gt;value}' OR
                    $filter-&gt;field LIKE '%{$filter-&gt;value}%' OR
                    $filter-&gt;field = '{$filter-&gt;value}'
                )";
                break;
        }
    }
    if(count($whereClauses) &gt; 0) {
        return implode(' AND ', $whereClauses);
    }
    return FALSE;
}
?&gt;&lt;?
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
        switch($filter-&gt;type) {
            case 'boolean':
                $filter-&gt;value = ($filter-&gt;value === TRUE) ? '1' : '0'; // Convert value for DB
                $whereClauses[] = "$filter-&gt;field = $filter-&gt;value" ;
                break;
            case 'date':
                $filter-&gt;value = "'$filter-&gt;value'"; // Enclose data in quotes
            case 'numeric':
                switch($filter-&gt;comparison) {
                    case 'lt': // Less Than
                        $whereClauses[] = "$filter-&gt;field &lt; $filter-&gt;value";
                        break;
                    case 'gt': // Greather Than
                        $whereClauses[] = "$filter-&gt;field &gt; $filter-&gt;value";
                        break;
                    case 'eq': // Equal To
                        $whereClauses[] = "$filter-&gt;field = $filter-&gt;value";
                        break;
                }
                break;
            case 'list':
                $listItems = array();
                foreach($filter-&gt;value as $value) {
                    $listItems[] = "'$value'";
                }
                $whereClauses[] = "$filter-&gt;field IN(" . implode(',', $listItems) . ')';
                break;
            case 'string':
            default: // Assume string
                $whereClauses[] = "(
                    $filter-&gt;field LIKE '{$filter-&gt;value}%' OR
                    $filter-&gt;field LIKE '%{$filter-&gt;value}' OR
                    $filter-&gt;field LIKE '%{$filter-&gt;value}%' OR
                    $filter-&gt;field = '{$filter-&gt;value}'
                )";
                break;
        }
    }
    if(count($whereClauses) &gt; 0) {
        return implode(' AND ', $whereClauses);
    }
    return FALSE;
}
?&gt;
</pre>

You can view examples of using the <a href="http://dev.sencha.com/deploy/ext-4.0.2a/examples/grid-filtering/grid-filter-local.html" target="_blank">FilterFeature in ExtJS 4 on the ExtJS 4 examples page for grid filtering.</a>

**Update:** The source code for this snippet is available [here](https://github.com/opnsrce/Code-Snippets/commit/96847c4b5177fc49bacba6aa1716b88accdb2082#diff-2).