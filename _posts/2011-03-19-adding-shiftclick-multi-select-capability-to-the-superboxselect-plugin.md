---
id: 57
title: Adding Shift+Click Multi-Select Capability to the SuperBoxSelect Plugin
date: 2011-03-19T17:56:38+00:00
author: Levi Hackwith
layout: post
guid: http://www.levihackwith.com/?p=57
permalink: /adding-shiftclick-multi-select-capability-to-the-superboxselect-plugin/
icy_video_embed_code:
  - 
categories:
  - Code Snippets
  - Programming / Web Development
tags:
  - ExtJS
  - JavaScript
  - SuperBoxSelect
---
&nbsp;

When I began using the <a href="http://www.sencha.com/forum/showthread.php?69307-3.x-Ext.ux.form.SuperBoxSelect" target="_blank">SuperBoxSelect plugin</a> at work, things went from good to awesome pretty damn quick. SuperBoxSelect offers a lot of great features that standard combo boxes don&#8217;t as well as directly integrating with the rest of ExtJS so you can do cool things like tie them to a JsonStore and write custom event handlers. Unfortunately, this plugin does support a commonly used feature among standard combo boxes: Shift+Click Selection.

<!--more-->

## Adding It In

Lucky for us, adding this feature is straight forward:

<pre class="brush: jscript; title: ; notranslate" title="">beforeadditem:function(self, recordValue) {
	var start = 0; // Holds the index of the first item we clicked on
	var end = 0; // Holds the index of the last item we clicked on
	var record = this.findRecord(this.valueField, recordValue);
	var recordIndex = this.store.indexOf(record);
	if(window.event.shiftKey) {
		this.multiSelectMode = true; // Prevents the combo box from collapsing when we start selecting items
		if(this.firstChoiceIndex == undefined) { // We haven't already chosen an item using shift + click
			this.firstChoiceIndex = recordIndex; // Store the index of the item we clicked
			this.view.all.item(recordIndex).addClass('x-combo-selected-shift'); // Style the item to show it's been selected
			return false; // Return false to prevent the item we selected from being added to the list of selected items
		} else { // We've already got a first item selected
			this.secondChoiceIndex = recordIndex;  // Store the item we just selected as the second item
			if(this.firstChoiceIndex &gt; this.secondChoiceIndex) { // This is where we sort out the start and end range of our loop
				start = this.secondChoiceIndex;
				end = this.firstChoiceIndex;
			} else if(this.secondChoiceIndex &gt; this.firstChoiceIndex) {
				start = this.firstChoiceIndex;
				end = this.secondChoiceIndex;
			}
			var selectedRecords = this.store.getRange(start, end); // Get all records with indexes at our between "start" and "end"
			Ext.each(selectedRecords, function(item, index, allitems) { // Add each item to the combo box
				self.addRecord(item)
			});
			// Clear out our selections
			this.firstChoiceIndex = undefined;
			this.secondChoiceIndex = undefined;
			return false;
		}
	} else { // We didn't use shift + click, so behave normally
		this.firstChoiceIndex = undefined;
		this.secondChoiceIndex = undefined;
		return true;
	}
}</pre>

To use this code, just drop it inside the &#8220;listeners&#8221; property of your SuperSelectBox instance and you&#8217;re good to go.

## Caveats

There&#8217;s a few things that you need to know about this code:

**It doesn&#8217;t work in FF:** Firefox does not support the global `window.event` object. Right now, I&#8217;m not really sure how to get around this, but when I find the solution I&#8217;ll update the post.

**It automatically fires the &#8216;additem&#8217; event for each item it adds to the list**: Usually, this wouldn&#8217;t be a problem but when you fire an event like this in rapid succession, a race condition might occur (Especially if each call results in an AJAX request). This issue will be resolved in a future update.

**You&#8217;ll need to add the `x-combo-selected-shift` class to the `superboxselect.css` file:** The x-combo-selected-shift differs from x-combo-selected in name only. The reason for this class is to prevent the code from removing the styling from the first and second items you pick once you mouse over other items in the list.

## Questions?

If anybody has any questions about the code or why I did something the way I did, feel free to leave a note in the comments. Happy coding!