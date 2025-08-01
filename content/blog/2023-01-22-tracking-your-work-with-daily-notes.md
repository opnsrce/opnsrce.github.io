---
title: Tracking Your Work with Daily Notes
description: "Stop trying to remember what you did last week."
summary: |
  A practical guide to using daily notes to track your work, remember key 
  details, and make performance reviews painless.
tags:
  - daily-notes
  - work-tracking
  - productivity
--- 

As a developer, remembering what you worked on last week—let alone last year—can
be tough. By keeping a daily log of your work, you'll have less to remember and
more information to help you do your job.

## Organizing Your Notes

Organize your notes in a folder for each year and a separate file for each day
you work:

```text
2022
2023
├─ 2023-01-02.md
├─ 2023-01-03.md
├─ 2023-01-04.md
├─ 2023-01-05.md
├─ 2023-01-06.md
```

## What to Track

### Meetings

Track every meeting you attend during the day. Make sure to document what was
discussed, any decisions that were made, and any links to relevant documentation
or resources.

```markdown
# January 05, 2023

## Meeting: Discuss Root Cause of Last Week's Outage

Met with the team to discuss the root cause of the 12/15/2022 outage. Steve
walked us through the [Splunk logs][01] and the [New Relic data][02] and
highlighted the Spike in bot traffic that occurred shortly before the site went
down. Based on these findings, we're going to set up a follow-up meeting with
the Security team to go over our findings and see what solutions they recommend.

[01]: https://url-to-splunk-logs
[02]: https://url-to-new-relic-data
```

Not every meeting can (or should) be clearly documented. Meetings that are
fairly routine or where sensitive information is discussed should be noted as
simply occurring:

```markdown
# January 05, 2023

## Meeting: Ticket Grooming

Groomed tickets in the backlog.

## Meeting: One-on-one with Manager

Met with my manager for our 1:1.
```

### Tickets

Document every ticket you worked on during the day, even if the work spans
multiple days. Each day you work on a task, document what was completed, what
problems you ran into, and any relevant conversations:

```markdown
# January 05, 2023

## [TCKT-9867][01]: Add New Headers to Standard Fetch Library

[Touched base with Carl][02] and got clarity around the requirements. Started
updating the unit tests to reflect the new headers. 

[01]: https://jira.com/browse/tckt-9867
[02]: https://url-to-slack-conversation
```

```markdown
# January 06, 2023

## [TCKT-9867][01]: Add New Headers to Standard Fetch Library

Finished updating the unit tests. Ran into issues with CORS requests failing due
to upstream services not being prepared to handle the new header values. I've
[reached out to the services team][02] to get a timeline for the updates on
their end.

[01]: https://jira.com/browse/tckt-9867
[02]: https://url-to-slack-conversation
```

```markdown
# January 07, 2023

## [TCKT-9867][01]: Add New Headers to Standard Fetch Library

Now that the upstream services can handle the update, I was able to complete my
testing and open and [MR][02].

[01]: https://jira.com/browse/tckt-9867
[02]: https://url-to-merge-request
```

```markdown
# January 08, 2023

## [TCKT-9867][01]: Add New Headers to Standard Fetch Library

Release this [to production][02].

[01]: https://jira.com/browse/tckt-9867
[02]: https://link-to-production-release
```

### Tasks

A task is anything you were asked to do that didn't have a ticket assigned to
it:

```markdown
# January 08, 2023

## Task: Update Expired Certificate in Dev Environment

[Susan asked me][01] to update the expired certs in our dev environment.

[01]: https://url-to-slack-conversation
```

If a task takes more than a day or two, convert it into an official ticket for
better tracking.

### Support Questions

Answering questions for your fellow engineers takes time. Since a lot of this
work is ad-hoc and not necessarily tied to a particular ticket, document it
separately from other work:

```markdown
# January 08, 2023

## Support: Help Chuck Debug His Release Pipeline

[Chuck asked me for help][01] debugging their pipeline issues. Turns out that
the logs were being truncated. Once we dug through the Splunk log, we were able
to see the actual authentication error causing the pipeline to fail and
update the credentials.

[01]: https://url-to-slack-conversation
```

### Accomplishments

If you accomplish something worth mentioning during a performance review, mark
it with a gold star (⭐):

```markdown
# January 07, 2023

## [TCKT-9837][01]: Fix Bundle Size Issues ⭐

I released the changes [to production][02]. This reduced the main bundle size by
90KB.

[01]: https://jira.com/browse/tckt-9837
[02]: https://url-to-merge-request
```

When your manager asks you for a list of major accomplishments for the last 6
months or year, you'll be able to quickly search your notes for the ⭐ symbol and
generate a list of noteworthy items.

## Best Practices

### Link Back to Everything

Whether it's a Slack thread, Jira ticket, or merge request, make sure you link
to it in your notes for later reference. Linking to relevant external resources
will help provide context if you're ever asked—and you will be—why a particular
decision was made or a task completed.

If you decide to use Markdown, I recommend you use [reference style
links](https://www.markdownguide.org/basic-syntax/#reference-style-links) to
make notes with a lot of links more legible.

### Be Careful What You Document

Consider your notes to be public (internally to your company). Don't document
anything you wouldn't want read aloud at the company Christmas party. Don't
document anything confidential (e.g., feedback for your peers, notes from
interviews, customer data, etc.,)

### Be Consistent

There's a lot of ways to document your daily work. Whatever you format you
choose to use, make sure it's consistent and that you document *everything* you
work on, no matter how small.

Choose a format you're comfortable with. I use Markdown but Confluence pages or
even plain text files also work.

### Avoid Third Party Tools

As tempting as it may be to store your notes in applications like Evernote or
Notion, I strongly advise against it. Because your notes could include
proprietary information, you may run into trouble if that data ends up being
stored on servers that don't belong to your company. An exception applies if
your company manages its own account with one of these vendors.

I store my notes in a git repository hosted on my company's servers.

## Closing Thoughts

Documenting everything you work on every day sounds like a lot of work. At
first, it may seem like it's not worth it. But the longer you take daily notes,
the more valuable they become. Recently, I was asked by leadership when a
project had launched, why certain design decisions were made, and who was
involved in those decisions—from 2019. Because I had consistently documented the
project (every meeting, every task, every ticket), I was able to gather all the
relevant documentation (including Slack threads) and deliver the information in
*minutes*.
