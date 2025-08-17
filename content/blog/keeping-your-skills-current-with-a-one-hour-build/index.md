---
cover:
  alt: A pen, notebook, and glasses on a desk.
  caption: Photo by [David Travis](https://unsplash.com/@dtravisphd) on Unsplash
  image: cover.jpg
date: 2021-06-23T00:00:00.000Z
description: |
  Learn how a One Hour Build sharpens skills through focused, time-boxed
  projects.
showtoc: true
summary: |
  A guide to using One Hour Builds to stay sharp, scope small projects, and
  build faster with purpose.
tags:
  - one-hour-build
  - personal-development
title: Keeping Your Skills Current With a One Hour Build
tocopen: false
---

Staying current with the latest technologies can feel overwhelming. The One
Hour Build makes it easier by giving you a clear, time-boxed way to practice.

## What is a One Hour Build?

A One Hour Build is a software project that teaches you a new technology and
only takes an hour to complete. Unlike casual research or tinkering, a One Hour
Build is a scoped, documented, and---most importantly---a *complete* project.

## Why One Hour?

One of the biggest problems with side projects is that they never get
finished. Limiting a project to one hour forces focus. It's enough time to make
something meaningful, but not enough time to get lost in the weeds.

## Set Up the Project

A One Hour Build has three main steps:

### 1. Decide on a Goal

The purpose is to learn a new skill. When deciding what to build, choose
something with clear, narrow parameters.

Think "Learn how to accept user input from the terminal in Ruby," not "Learn
Ruby."

Example project description:

> The goal of this build project was to familiarize myself with the following
> concepts in Ruby:
>
> - Writing a command line application
> - Accepting user input from the command line
> - Conditional statements (`unless`)
> - Sanitizing user input (`chomp`, `strip`)
> - Outputting strings and variables to the command line

### 2. Create a Spec Document

Once you have a project in mind, write the spec doc. Even for a small project,
it keeps you focused. Plus, writing spec docs is a valuable skill that many
developers rarely get to practice.

Your spec doc should include:

- Purpose of the application
- Happy path user flow
- Negative path user flow
- Error handling

Write it as if you're handing the project to another developer.

Example:

> Write a command line Ruby application that prompts the user to answer the
> following questions (in order):
>
> - What's your name?
> - How old are you (in years)?
> - What is your favorite color?
> - Who is your favorite author?
>
> The program should prompt the user to answer each question individually before
> showing the next question. The user should be allowed to skip a question by
> leaving the answer blank. No validation should be applied to any of the
> answers provided. Once the user has answered the questions, the program should
> output the following (including line breaks):
>
> Hello, [name]!
>
> Today, I learned the following things about you:
>
> - You are [age] years old.
> - Your favorite color is [color].
> - Your favorite author is [author].

### 3. Build the Prerequisites

Some One Hour Builds require setup outside the project's scope. For example, to
build a Ruby command line application, you need to first install Ruby.

The same applies to web projects. If you're learning WebRTC and need a web
form, build the form beforehand.

## Get Settled

Once everything's defined and ready, start coding. The clock runs for one
*uninterrupted* hour---not five minutes here and there. Find a distraction-free
space, set a timer, and code.

## Write the Post Mortem

After you finish, document:

- Source Lines of Code (SLOC)
- How long it actually took
- Overall experience of writing the code
- Issues you ran into

Example:

> This build didn't require much research. Towards the end, I hit a snag
> checking whether a variable was empty. When the user skipped a question,
> `gets` returned `nil` instead of an empty string. I had to adjust my approach
> and check for both `nil` and an empty string.

If the build ran over or under an hour, note why. Were some parts easier or
harder than expected? The post mortem isn't meant to be a Root Cause Analysis,
just a quick reflection.

## Benefits of a One Hour Build

One Hour Builds improve more than coding. They sharpen writing and analysis
skills.

The spec doc forces you to think from start to finish; the time constraint
keeps you focused and pushes you to define a clear [Definition of Done][1].

Most importantly, you learn exactly what you can accomplish in an hour, which
makes you better at planning and estimating future projects.

## More Examples

See more One Hour Build projects in my [One Hour Build repo][2].

[1]: https://www.leadingagile.com/2017/02/definition-of-done/
[2]: https://github.com/opnsrce/one-hour-builds
