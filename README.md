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

Some users, including the owner of this repo, felt like they needed a notification system without the hassle of an extra app (like [IFTTT](https://play.google.com/store/apps/details?id=com.ifttt.ifttt&hl=en)) so a bot was the most obvious solution for Telegram users.

## What is Telegram

[Telegram](https://telegram.org/) is a messaging application, similar to WhatsApp or Signal. The main differences are:

- texts are not end-to-end encypted by default (which allows for a single account to use multiple clients seamlessly)
- the encryption algorithm is not open source
- it has a ton more features than any other messaging app
- it supports bots!

## What are Telegram Bots

[Telegram bots](https://core.telegram.org/bots) basically work like any other messenger bot (e.g. Discord bots, Messenger bots, etc) but are a bit simpler to implement thanks to the [Telegram Bot API](https://core.telegram.org/bots/api). A Python wrapper for the API used in this project (*pyTelegramBotAPI*) can be found [here](https://github.com/eternnoir/pyTelegramBotAPI/).

## What is Dota2

[Dota2](https://www.dota2.com) originated as custom map for [Warcraft III](http://us.blizzard.com/en-us/games/war3/) made by Eul and after much controversy it now is the most successful 100% free-to-play game by Valve and Icefrog.

## Setting up dotaUpdatesBot

1. Download or clone this repository using `git clone https://github.com/zachkont/dotaUpdatesBot.git`

2. Make sure `python2.7` and `pip` version 9+ are installed

3. Setup your [Telegram API key](https://core.telegram.org/api/obtaining_api_id) and optionally your [Dota2 API key](https://dota2api.readthedocs.io/en/latest/tutorial.html#getting-an-api-key)

4. Copy the `settings.py.example` into `settings.py` and fill in your API keys. You can leave the `crisis account` variable empty or delete it alltogether.

5. Create the required `.json` files and initalize them with `{}`. These are:

* previousblogposts.json
* previouscyborgmatt.json
* previousjasons.json
* previousmagesunite.json
* previoussirbelvedere.json
* previouswykrhm.json
* userlist.json
* grouplist.json

or just copy and paste the following command on Linux:
```
echo {} > previousblogposts.json &&
cp previousblogposts.json previouscyborgmatt.json &&
cp previousblogposts.json previousjasons.json &&
cp previousblogposts.json previousmagesunite.json &&
cp previousblogposts.json previoussirbelvedere.json &&
cp previousblogposts.json previouswykrhm.json &&
cp previousblogposts.json userlist.json &&
cp previousblogposts.json grouplist.json
```

6. Install the requirements using pip via `pip install -r requirements.txt`

7. Run main.py for the command functionality with
`python main.py`
or updater.py for the dota update subscription functionality with
`python updater.py` 

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

This program is provided under the GNU GPLv3 License. As such it is shipped "as is" and the authors are not liable and provide no warranty. [Read more](LICENSE).
