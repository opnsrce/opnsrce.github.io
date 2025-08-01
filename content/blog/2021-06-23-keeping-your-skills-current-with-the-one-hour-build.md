---
title: Keeping Your Skills Current With the One Hour Build
description: |
  Learn how One Hour Builds help sharpen skills with focused, time-boxed
  projects.
summary: |
  A guide to using One Hour Builds to stay sharp, scope small projects, and
  build faster with purpose.
tags:
  - one-hour-build
  - personal-development
--- 

Staying up to date with the latest technologies can seem overwhelming. The One
Hour Build can help make staying up to date a little easier.

## What is the One Hour Build?

The One Hour Build is a software project that teaches you a new technology and
only takes an hour to complete. But, don't confuse this with casual research or
hobbyist tinkering. The One Hour Build is a scoped, documented, and most
importantly, complete project.

## Why 1 Hour?

One of the biggest problems with side projects is that they often end up
unfinished. Limiting the project to 1 hour gives it focus. It's enough time to
develop something meaningful but not enough time to lose focus.

## Set up the Project

The One Hour Build is broken down into 3 main steps:

### Decide on a Goal

The purpose of the One Hour Build is to learn a new skill. So, when deciding
what to build, aim for something with easily defined parameters. For example,
"learn Ruby" is way too broad. "Learn how to accept user input from the terminal
in Ruby" is much clearer and easier to design a program around. A good rule is:
if you can't describe the program's scope in a sentence or two, it's too
broad of a project.

Here's an example project description:

> The goal of this build project was to familiarize myself with the following
> concepts in Ruby:
>
> - Writing a command line application
> - Accepting user input from the command line
> - Conditional statements (`unless`)
> - Sanitizing user input (`chomp`, `strip`)
> - Outputting strings and variables to the command line

### Create a Spec Document

After you've decided on a project, it's time to write the spec document. Writing
a spec doc, even for a small project, will help keep you focused as you work.
Plus, writing spec docs is a good skill that a lot of developers don't often get
to practice.

The spec document should cover:

- The purpose of the application.
- Happy path user flow.
- Negative path user flow.
- Error handling.

You should write the spec doc as if you're going to hand it off to another
developer to work on. Here's an example:

> Write a command line Ruby application that prompts the user to fill in the
> answers to the following questions (in order):
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

### Build the Prerequisites

Not every One Hour Build can be developed in complete isolation. Sometimes,
there are requirements that are necessary for the project but out of scope. For
example, to build the Ruby command line application, you'll need to have Ruby
installed. The goal of the project is not to learn how to install Ruby. The same
thing also applies to web development. If you're trying to learn about WebRTC
and your application requires a web form, build the form ahead of time.

## Get Settled

Now that everything is clearly defined and set up, it's time to start coding.
The time scale for this project is one *uninterrupted* hour, not five or ten
minutes here and there until you run out of time. Make sure you're in a place
with minimal distractions where you can stay completely focused. Set a timer.
Code.

## Write the Post Mortem

Once the project is finished, document the Source Lines of Code (SLOC) and how
long it took you. Then, describe your overall experience with the project.
Mention any issues you ran into. Here's an example post mortem:

> For this build, I did not have to do a ton of research as I developed it; it
> was pretty straightforward. Towards the end, however, I did run into a snag
> when checking whether or not a given variable was empty or not and had to
> search around for the answer. When the user chooses not to answer a question
> and presses enter to move on, the `gets` command returns `nil` instead of an
> empty string like I was expecting. Because of this, I had to alter my initial
> approach and check to see if an answer was `nil` *or* an empty string instead
> of *just* an empty string.

If the project went over one hour or took significantly less than an hour, make
sure you document why. Were some requirements more or less difficult to
implement than expected? Why? You don't need to write a book here: this isn't
meant to be a Root Cause Analysis. The purpose of the post mortem is to get you
thinking about the project as a whole.

## The Benefits of a One Hour Build

There are a lot of benefits to the One Hour Build that go far beyond improving
your coding. The One Hour Build also helps you improve your writing and analysis
skills. The spec doc gets you thinking about a project from start to finish,
at a high level. The time constraint forces you to focus on a project's purpose
and nail down a [Definition of Done][1]. Most importantly, the One Hour Build
gives you a better understanding of what you are capable of in an hour. In turn,
you'll become better at planning and estimating projects in the future.

## More Examples

To see more examples of One Hour Build projects, head over to my [One Hour Build
repo][2].

[1]: https://www.leadingagile.com/2017/02/definition-of-done/
[2]: https://github.com/opnsrce/one-hour-builds
