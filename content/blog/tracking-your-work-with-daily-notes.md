---
date: 2023-01-22
description: Stop trying to remember what you did last week.
showtoc: true
summary: |
  A practical guide to using daily notes to track your work, remember key
  details, and make performance reviews painless.
tags:
  - daily-notes
  - work-tracking
  - productivity
title: Tracking Your Work with Daily Notes
tocopen: false
---

As a developer, remembering what you worked on last week---let alone last
year---can be tough. By keeping a daily log of your work, you'll have less to
remember and more information to help you do your job.

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

Document every meeting you attend. Note what was discussed, decisions made, and
links to relevant documentation or resources.

```markdown
# January 05, 2023

## Meeting: Discuss Root Cause of Last Week's Outage

Met with the team to discuss the root cause of the 12/15/2022 outage. Steve
walked us through the [Splunk logs][01] and the [New Relic data][02]. He
highlighted the spike in bot traffic shortly before the site went down. Based on
these findings, we set up a follow-up meeting with the Security team to review
our findings and get their recommendations.

[01]: https://url-to-splunk-logs
[02]: https://url-to-new-relic-data
```

Not every meeting needs a detailed write-up. Routine meetings or those with
sensitive information can be noted simply:

```markdown
# January 05, 2023

## Meeting: Ticket Grooming

Groomed tickets in the backlog.

## Meeting: One-on-one with Manager

Met with my manager for our 1:1.
```

### Tickets

Document every ticket you work on, even if it spans multiple days. Each day you
touch it, note what was done, problems encountered, and relevant conversations.

```markdown
# January 05, 2023

## [TCKT-9867][01]: Add New Headers to Standard Fetch Library

[Touched base with Carl][02] and got clarity on the requirements. Started
updating the unit tests to reflect the new headers.

[01]: https://jira.com/browse/tckt-9867
[02]: https://url-to-slack-conversation
```

```markdown
# January 06, 2023

## [TCKT-9867][01]: Add New Headers to Standard Fetch Library

Finished updating the unit tests. Ran into CORS request failures due to upstream
services not handling the new header values. I reached out to the services
team[02] for their update timeline.

[01]: https://jira.com/browse/tckt-9867
[02]: https://url-to-slack-conversation
```

```markdown
# January 07, 2023

## [TCKT-9867][01]: Add New Headers to Standard Fetch Library

With upstream services updated, I completed testing and opened an [MR][02].

[01]: https://jira.com/browse/tckt-9867
[02]: https://url-to-merge-request
```

```markdown
# January 08, 2023

## [TCKT-9867][01]: Add New Headers to Standard Fetch Library

Released [to production][02].

[01]: https://jira.com/browse/tckt-9867
[02]: https://link-to-production-release
```

### Tasks

Log any task you were asked to do without a ticket:

```markdown
# January 08, 2023

## Task: Update Expired Certificate in Dev Environment

[Susan asked me][01] to update the expired certs in our dev environment.

[01]: https://url-to-slack-conversation
```

If a task takes more than a couple of days, convert it into a ticket for better
tracking.

### Support Questions

Answering ad-hoc questions eats time. Since it's often unrelated to a ticket,
log it separately.

```markdown
# January 08, 2023

## Support: Help Chuck Debug His Release Pipeline

[Chuck asked me for help][01] debugging their pipeline. Logs were being
truncated. Once we dug through the Splunk log, we found the authentication error
causing the failure and updated the credentials.

[01]: https://url-to-slack-conversation
```

### Accomplishments

If you do something worth bragging about in a performance review, mark it with a
gold star (⭐):

```markdown
# January 07, 2023

## [TCKT-9837][01]: Fix Bundle Size Issues ⭐

Released the changes [to production][02]. Reduced the main bundle size by 90KB.

[01]: https://jira.com/browse/tckt-9837
[02]: https://url-to-merge-request
```

When asked for major accomplishments from the last 6 months or year, you can
quickly search for the ⭐ symbol and pull the list.

## Best Practices

### Link Back to Everything

Whether it's Slack, Jira, or a merge request, link to it in your notes. This
provides context when you're inevitably asked why something was done.

If using Markdown, [reference style links](https://www.markdownguide.org/basic-
syntax/#reference-style-links) keep link-heavy notes readable.

### Be Careful What You Document

Assume your notes are public internally. Don't write anything you wouldn't want
read aloud at the company Christmas party. Avoid confidential data (e.g.,
feedback for peers, interview notes, customer data).

### Be Consistent

Pick a method and stick to it. Whatever format you choose, use it consistently
and document *everything* you work on, no matter how small.

I use Markdown, but Confluence pages or plain text also work.

### Avoid Third Party Tools

Avoid storing notes in Evernote, Notion, or similar tools unless your company
controls the account. Proprietary data in third-party servers can be a problem.

I store my notes in a git repository hosted on company servers.

## Closing Thoughts

Documenting everything sounds like a chore. At first, it feels pointless. But
over time, the value compounds. Recently, leadership asked me when a project
launched, why certain design decisions were made, and who was involved---from
2019. Because I had documented every meeting, task, and ticket, I could pull the
Slack threads and other details in *minutes*.
