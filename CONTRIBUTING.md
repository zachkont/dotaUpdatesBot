# Contributing to dotaUpdatesBot

Greetings fellow [Dota2](http://store.steampowered.com/app/570/Dota_2/), [Telegram](https://telegram.org/) or [Python](https://www.python.org/) enthusiast:tada:
It's great to have you here, I could really use your help!

The following is a set of guidelines for contributing to dotaUpdatesBot which is a self-hosted Telegram bot that runs publicly as [@announcebot](http://telegram.me/announcebot). These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

#### Table Of Contents

- [Contributing to dotaUpdatesBot](#contributing-to-dotaupdatesbot)
      - [Table Of Contents](#table-of-contents)
  * [The team](#the-team)
  * [Where can I ask a question?](#where-can-i-ask-a-question-)
  * [About the project](#about-the-project)
    + [What is Telegram](#what-is-telegram)
    + [What are telegram bots](#what-are-telegram-bots)
    + [What is dota2](#what-is-dota2)
    + [So what is this for?](#so-what-is-this-for-)
  * [How to contribute](#how-to-contribute)
    + [Non-code contribution](#non-code-contribution)
    + [Code contribution](#code-contribution)
  * [How to test your code](#how-to-test-your-code)
    + [Automated Linter](#automated-linter)
    + [Styling guide](#styling-guide)
      - [Git Commit Messages](#git-commit-messages)
      - [Python Styleguide](#python-styleguide)

## The team

The developer team is basically just the owner of the project (and his alt account) but there have been quite a few contributions in github already. One of them could be you!

## Where can I ask a question?

> **Note:** Please don't file an issue to ask a question.

You can reach me in reddit for any questions that you might have, my username is `/u/karaflix`

## About the project

### What is Telegram

[Telegram](https://telegram.org/) is a messaging application, similar to whatsapp or signal. The main differences are:
* texts are not end-to-end encypted by default (which allows for a single account to use multiple clients seamlessly),  
* the encryption algorithm is not open source
* it has a ton more features than any other messaging app
* it supports bots!

### What are telegram bots

[Telegram bots](https://core.telegram.org/bots) basically work like any other messenger bot (e.g. discord bots, messenger bots etc.) but are a bit simpler to implement thanks to the [Telegram bot API](https://core.telegram.org/bots/api). A python wrapper for that (which is also used in this project) is the [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI/) by eternoir.

### What is dota2

Dota2 is the best game ever. It originated as custom map for WarcraftIII made by Eul and after much controversy it now is the most successful 100% free-to-play game by Valve and Icefrog. Its worst characteristic is the games unique ability to suck up your life. It also has quite a steep learning curve.

### So what is this for?

Dota is an old game and the way it keeps the players interested is through constant updates. However they are irregular and the userbase is basically craving for them. The big changes have an official changelog at the [official blog](blog.dota2.com). Some smaller patches get notes in steam news but the rest never see the light of day. 

However, the game's [reddit page](https://www.reddit.com/r/DotA2/) is quite active and every new patch, changelog or update is posted there. Thanks to some users (specifically u/SirBelvedere and u/magesunite at the time of writing this) who take the time to read through the diffs over at steam.db, the community gets a nice changelog in a reddit post. 

Some users, including the owner of this repo, felt like they needed a notification system for that without the need for an extra app (like IFTTT) so this was the most obvious solution for telegram users.

## How to contribute

### Non-code contribution

The easiest way to contribute is to report a bug or submit a feature request. To do that you can use githubs issue system which only requires a github account.
Please make your bug reports as simple and as clear as possible. There is only one of me and I have very limited time for this project. 
Likewise, any extreme suggestions will be probably ignored, or at least postponed for much, much later.

### Code contribution

The hot stuff. So, in order to make a code contribution, please follow these steps:
* Either choose or create a new issue describing what your contribution will do. If you create a new issue, make it simple but self-explanatory. 
* Fork the project's **master** branch
* Do your thing
* Test your thing
* Test your thing again
* Submit a PR for the **development** branch

If you are new to python, issues labeled with `easy` are a good starting point.

## How to test your code

At this point, I will assume you are familiar with basic Python requirements and development. Most of what is needed is provided at the README file. Please consult it if you need any more info.

> **Note:** If you believe these instruction are incomplete, please create an issue with the problem you encountered but wasn't explained in either this file or the README, and I will try to include it

The first step is to create your own bot. After installing telegram (alternatively, you can use the web version) message the [BotFather](@BotFather). He will help you create a new bot and will give you the corresponding `BOT TOKEN`. Use that in the 
`settings.py` file. 

Depending on your changes, you may also need to create a [Dota2 API token](http://steamcommunity.com/dev/apikey) (requires a steam account) and familiarize yourself with the [Dota2 API wrapper](https://dota2api.readthedocs.io/en/latest/). Use the token in the `settings.py` file.

### Automated Linter

The project is automatically monitored by [Codacy](https://www.codacy.com/app/zachkont/dotaUpdatesBot/dashboard). After a PR is submitted, a review will be posted marking the PR as good or bad. Please spare the time to fix any issues it may suggest.

### Styling guide

#### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests

#### Python Styleguide

The project, finaly, adheres to the [PEP8](https://www.python.org/dev/peps/pep-0008/) guidelines (mostly) except for line length, which I don't really care but will accept as a PR if someone goes into the trouble for it. The most important thing is to use ** 4 spaces** instead of tabs.

Also, if there is a lightweight library, that does the task adequately, it is better to use that instead of writing your own function.

Any functionality that adds to `main.py` should be written in `utils.py`, so that `main.py` only includes bot commands.

---

Finally, I would like to thank you for reading this, even if you don't end up submitting anything. Interest in this project is the only thing that keeps it alive. I appreciate your time.


