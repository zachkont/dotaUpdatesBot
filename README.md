[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ba82c2f871a44d3db708b88abeed5f7a)](https://www.codacy.com/app/zachkont/dotaUpdatesBot?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=zachkont/dotaUpdatesBot&amp;utm_campaign=Badge_Grade)

# dotaUpdatesBot

Telegram Bot for Dota2 Updates

Running publicly as [@announcebot](http://telegram.me/announcebot), licensed under the GNU General Public License.

# Index

- [About the project](#about-dotaupdatesbot)
  - [What is Telegram](#what-is-telegram)
  - [What are Telegram bots](#what-are-telegram-bots)
  - [What is Dota2](#what-is-dota2)

# About dotaUpdatesBot

This bot serves a simple purpose, provide an easy interface for Telegram users to get their dose of Dota2!

Dota is an old game and the way it keeps the players interested is through constant updates. However they are irregular and the userbase is basically craving for them. The big changes have an official changelog at the [official blog](https://blog.dota2.com). Some smaller patches get notes in steam news but the rest never see the light of day.

However, the game's [Reddit page](https://www.reddit.com/r/DotA2/) is quite active and every new patch, changelog or update is posted there. Thanks to some users (specifically u/SirBelvedere and u/magesunite at the time of writing this) who take the time to read through the diffs over at [SteamDB](https://steamdb.info/patchnotes/), the community gets a nice changelog in a Reddit post.

Some users, including the owner of this repo, felt like they needed a notification system without the hassle of an extra app (like IFTTT) so a bot was the most obvious solution for Telegram users.

## What is Telegram

[Telegram](https://telegram.org/) is a messaging application, similar to WhatsApp or Signal. The main differences are:

- texts are not end-to-end encypted by default (which allows for a single account to use multiple clients seamlessly)
- the encryption algorithm is not open source
- it has a ton more features than any other messaging app
- it supports bots!

## What are Telegram Bots

[Telegram bots](https://core.telegram.org/bots) basically work like any other messenger bot (e.g. Discord bots, Messenger bots, etc) but are a bit simpler to implement thanks to the [Telegram Bot API](https://core.telegram.org/bots/api). A Python wrapper for the API used in this project (*pyTelegramBotAPI*) can be found [here](https://github.com/eternnoir/pyTelegramBotAPI/).

## What is Dota2

[Dota2](https://www.dota2.com) originated as custom map for WarcraftIII made by Eul and after much controversy it now is the most successful 100% free-to-play game by Valve and Icefrog.

## Setting up dotaUpdatesBot

1. Download this repository

2. Setup your [Telegram API key](https://core.telegram.org/api/obtaining_api_id) and [Dota2 API key](https://dota2api.readthedocs.io/en/latest/tutorial.html#getting-an-api-key)

3. Install [eternoir](https://github.com/eternnoir/pyTelegramBotAPI/) Telegram bot API

4. Install [joshuaduffy](https://github.com/joshuaduffy/dota2api) Dota2API

## Commands

|Command | Brief explanation|
:----------------| -------------
|`/help`|Displays the basic help menu|
|`/dotanews`|Returns the latest Steam News entry related to Dota2 |
|`/dotablog`|Returns the latest blog post from [blog.dota2.com](https://blog.dota2.com)|
|`/subscribe`|Adds the user or group to the subscription list|
|`/unsubscribe`|Removes the user or group from the subscription list|
|`/match <match_id>`|Returns some info about match with match_id|

## How To Contribute

Read [CONTRIBUTING.MD](https://github.com/zachkont/dotaUpdatesBot/blob/master/CONTRIBUTING.md#how-to-contribute)

## Disclaimer

This program is provided "as is" without warranty of any kind.
