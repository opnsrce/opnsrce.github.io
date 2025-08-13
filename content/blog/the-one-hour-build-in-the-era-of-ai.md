---
author: Levi Hackwith
date: 2025-08-13
description: |
    When code really breaks (and it will), you can't fix it with a
    prompt.
draft: false
summary: |
  Twelve years ago, I built the One Hour Build repo to improve how I think
  about code. Now that AI can crank out code in minutes, it's worth
  remembering why thinking about code still matters.
tags:
  - one-hour-build
  - personal-development
  - artificial-intelligence
title: "The One Hour Build In the Era of AI: Why Thinking About Code Still Matters"
---

Twelve years ago, I built the [One Hour Build repo][01] to improve how I think
about code.

Now that AI can crank out code in minutes, it's worth remembering that thinking
about code still matters.

It's easy to confuse output with creation. Saying you "wrote" an app because you
came up with the prompt is like saying you cooked a burger because you told the
chef, "medium rare; extra pickles; no onions." You didn't make anything---and
just like an undercooked burger, the consequences of poorly made code are dire.

Writing code starts with thinking about it. Skip that, and you won't be able to
[debug problems effectively][02] when the code blows up. The recent replacement
of software development with "prompt engineering" has convinced a lot of junior
devs that typing a well-structured wish into a textbox ("make me a Tetris app
that runs in Canvas") is the same as building software. It's not.

An LLM cannot tailor its output to the long-term needs of your project or your
organization, it can't consider the needs of your users, and---*critically*---it
cannot be held accountable for the "decisions" it makes. An LLM will happily
create a login system with unsafe authentication, letting attackers slip in
under the wrong identity---if it means getting to the user’s desired output
faster.

Speed is easy; quality is hard. The best engineers are measured by how easily
their code can be understood, maintained, and [secured][03].

I'm not anti-AI---it's great for boilerplate, scaffolding, understanding error
messages, and documentation. Hell, I even used it to clean up the punctuation
and grammar in this post (the em dashes are mine, thank you very much). The
point is to use AI for the *rote*, boring crap so you can focus on actually
writing and understanding your code.

Because when the kitchen catches fire, you can't put it out by shouting at
the chef.

[01]: https://github.com/opnsrce/one-hour-builds
[02]: https://www.windowscentral.com/software-apps/copilot-and-chatgpt-makes-you-dumb-new-microsoft-study
[03]: https://ieeexplore.ieee.org/document/9833571
