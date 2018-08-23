#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import telebot
import requests
import feedparser
import dota2api
import HTMLParser

from utils import intime, getCID, getContent, bot, addBlogPostInstantView
from settings import DOTA2API_TOKEN
import subscribermanager as subman

telebot.logger.setLevel(logging.ERROR)
api = dota2api.Initialise(DOTA2API_TOKEN)

heroes_list = api.get_heroes()
heroes_list = heroes_list["heroes"]

parser = HTMLParser.HTMLParser()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['help'])
def get_help(message):
    gitUrl = "https://github.com/zachkont/dotaUpdatesBot"
    redditUrl = "https://www.reddit.com/message/compose/?to=karaflix"
    bot.reply_to(message,
                    u'Did you find a bug or have any questions?\n'
                    + u'Visit the [GitHub page]({gitUrl})'.format(gitUrl=gitUrl)
                    + u' for more information or contact'
                    + u' [/u/karaflix]({redditUrl})'.format(redditUrl=redditUrl)
                    + u' on reddit!',
                    parse_mode="Markdown",
                    disable_web_page_preview=True)

@bot.message_handler(commands=['info'])
def get_info(message):
    gitUrl = "https://github.com/zachkont/dotaUpdatesBot"
    bot.reply_to(message,
                    u'The main use of this bot is to notify you whenever a Dota update gets released.\n'
                    + u'Visit the [GitHub page]({gitUrl})'.format(gitUrl=gitUrl)
                    + u' for more information on what you can do or how to contribute!',
                    parse_mode="Markdown",
                    disable_web_page_preview=True)


@bot.message_handler(commands=['dotanews', 'dotanew', 'dnews', 'dnew'])
def dota_news(message):
    if intime(message):
        cid = getCID(message)
        content = getContent(message)
        url = "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=570&count=1&maxlength=300&format=json"
        request = requests.get(url)
        data = request.json()
        if content != "?":
            if request.status_code == 200:
                title = data['appnews']['newsitems'][0]['title']
                content = data['appnews']['newsitems'][0]['contents']
                content_nice = content.replace(" - ", "\n - ")
                content_nice = content_nice.replace("*", "\n*")
                content_nice = parser.unescape(content_nice)
                url = data['appnews']['newsitems'][0]['url']
                bot.send_message(
                    cid,
                    u'*{title}*```> \n{content_nice}\n[...]\n```'.format(title=title, content_nice=content_nice)
                    + u'[More info here]({url})'.format(url=url),
                    parse_mode="Markdown",
                    disable_web_page_preview=True)
            else:
                bot.reply_to(
                    message,
                    "`There has been an error, the number {error} to be specific.`"
                        .format(error=request.status_code),
                    parse_mode="Markdown")
        else:
            bot.reply_to(
                message,
                "`Send this command alone and I will show you the last Steam News for Dota2 entry`",
                parse_mode="Markdown")


@bot.message_handler(commands=['dotablog', 'dotablognew', 'dblog', 'dblognew'])
def dota_blog(message):
    if intime(message):
        cid = getCID(message)
        dota_blog_rss_url = "http://blog.dota2.com/feed/"
        feed = feedparser.parse(dota_blog_rss_url)
        post_title = feed["items"][0]["title"]
        post_link = addBlogPostInstantView(feed["items"][0]["link"])
        bot.send_message(
            cid,
            u'*{title}* ```\n\n```'
            .format(title = post_title)
            + u'[Read the latest blog post in your browser]({url})'
            .format(url = post_link),
            parse_mode = "Markdown")


@bot.message_handler(commands=['subscribe', 'letmeknow'])
def start_subscription(message):
    uid = str(message.from_user.id)
    cid = str(message.chat.id)

    if message.chat.type == 'private':
        if uid not in subman.getUsers():
            subman.addUser(uid, message.from_user.first_name)
            bot.send_message(uid, 'You will now receive updates!', parse_mode="Markdown")
        else:
            bot.send_message(uid, 'halloooooo', parse_mode="Markdown")
    elif message.chat.type == 'group' or message.chat.type == 'supergroup':
        if cid not in subman.getGroups():
            bot.reply_to(
                message,
                'Hello fans, this awesome group is now added and I will keep you guys up to date',
                parse_mode="Markdown")
            gid = str(message.chat.id)
            gname = message.chat.title
            subman.addGroup(gid, gname)
        else:
            bot.send_message(cid, 'Hello again fans, your group has already been registered', parse_mode="Markdown")
    else:
        pass


@bot.message_handler(commands=['unsubscribe', 'enough', 'unsub'])
def end_subscription(message):
    uid = str(message.from_user.id)
    cid = str(message.chat.id)

    if message.chat.type == 'private':
        if uid in subman.getUsers():
            subman.deleteUser(uid)
            bot.send_message(uid, 'You have been removed from the subscription list', parse_mode="Markdown")
        else:
            bot.send_message(uid, 'You can\'t unsubscribe without subscribing first dummy!', parse_mode="Markdown")
    elif message.chat.type == 'group' or message.chat.type == 'supergroup':
        if cid in subman.getGroups():
            bot.reply_to(message, 'Oh, no more updates? Okay...', parse_mode="Markdown")
            gid = str(message.chat.id)
            subman.deleteGroup(gid)
        else:
            bot.send_message(cid, 'Not subscibed yet', parse_mode="Markdown")
    else:
        pass


@bot.message_handler(regexp="match (\d.*?)(\D|$)")
def find_match(message):
    if intime(message):
        cid = getCID(message)
        content = getContent(message)

        match_id = message.text
        match_id = match_id.split()[1]
        try:
            match = api.get_match_details(match_id)

            url = match.url
            request = requests.get(url)
            match_data = request.json()

            if content != "?":
                if request.status_code == 200:
                    hero_list = []
                    if match_data['result']['radiant_win']:
                        title = "Radiant!"
                    else:
                        title = "Dire!"

                    url = "http://www.dotabuff.com/matches/" + match_id

                    radiant_content = ""
                    dire_content = ""
                    for player in match_data['result']['players']:
                        if player['player_slot'] < 100:  # radiant
                            for hero in heroes_list:
                                if hero['id'] == player['hero_id']:
                                    hero_list.append(hero['localized_name'])
                                    radiant_content = (radiant_content +
                                        hero['localized_name'] + " " +
                                        str(player['kills']) + "/" +
                                        str(player['deaths']) + "/" +
                                        str(player['assists']) + '\n')
                        else:  # dire
                            for hero in heroes_list:
                                if hero['id'] == player['hero_id']:
                                    hero_list.append(hero['localized_name'])
                                    dire_content = (dire_content +
                                        hero['localized_name'] + " " +
                                        str(player['kills']) + "/" +
                                        str(player['deaths']) + "/" +
                                        str(player['assists']) + '\n')

                    bot.send_message(
                        cid,
                        'Winner:  *{title}* \n _Radiant:_ \n{radiant}\n _Dire:_\n{dire}\n'
                        .format(title=title, radiant=radiant_content, dire=dire_content)
                        + '[Dotabuff link]({url})'.format(url=url),
                        parse_mode="Markdown",
                        disable_web_page_preview=True)
                else:
                    bot.reply_to(
                        message,
                        "`There has been an error, the number {error} to be specific.`".format(error=request.status_code),
                        parse_mode="Markdown")
            else:
                bot.reply_to(message, "`wat`", parse_mode="Markdown")
        except Exception as ex:
            bot.reply_to(
                message,
                "There has been an error, its message is:\n `{error}`".format(error=ex.msg),
                parse_mode="Markdown")


bot.polling(none_stop=True, interval=0)

