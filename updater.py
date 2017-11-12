#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import json
import time
import feedparser
import telebot

from bs4 import BeautifulSoup
from datetime import datetime

from utils import bot, loadjson, addBlogPostInstantView
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

log = open('log.txt', 'a')


def get_rss_posts(url, error_message):
    feed = feedparser.parse(url)
    if feed.status == 200:  # OK
        posts = feed.entries
    else:
        posts = None
        print("{}: {}".format(datetime.now(), error_message), file=log)
    return posts


def get_dota2blog_posts():
    return get_rss_posts("http://blog.dota2.com/feed/", "Dota 2 blog feed not accessible.")


def get_reddit_user_posts(username):
    return get_rss_posts("https://www.reddit.com/user/{}/submitted/.rss?limit=3".format(username),
                         "Reddit feed of the user '{}' not accessible".format(username))


def get_reddit_preview(text):
    return BeautifulSoup(text, "html.parser").text[:266]  # 266 is Max. length of dota blog summaries


def get_relevant_sirbelvedere_posts():
    posts = get_reddit_user_posts("SirBelvedere")
    if posts:
        return [post for post in posts if ("/u/SirBelvedere on" not in post.title) and ("Dota 2 Update" in post.title)]


def get_relevant_cyborgmatt_posts():
    posts = get_reddit_user_posts("Cyborgmatt")
    if posts:
        return [post for post in posts if ("/u/Cyborgmatt on" not in post.title) and ("Dota 2 Update" in post.title)]


def get_relevant_magesunite_posts():
    posts = get_reddit_user_posts("Magesunite")
    if posts:
        return [post for post in posts if ("/u/Magesunite on" not in post.title) and ("Dota 2 Update" in post.title)]


def get_relevant_wykrhm_posts():
    posts = get_reddit_user_posts("wykrhm")
    if posts:
        return [post for post in posts if ("/u/wykrhm on" not in post.title)]


def post_is_fresh(post, filename):
    return post.title not in loadjson(filename)


def add_post_to_unfresh_list(post, filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    data.update({post.title: post.link})
    with open(filename, 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4, separators=(',', ': '))


def notify_users_and_groups(message):
    # Notify subscribed users
    for user_id in loadjson("userlist"):
        try:
            bot.send_message(user_id, message, parse_mode="Markdown")
        except Exception as ex:
            telebot.logger.error(ex)
            print("{}: Message could not be sent to users".format(datetime.now()), file=log)

    # Notify subscribed groups
    for gid in loadjson("grouplist").keys():
        try:
            bot.send_message(gid, message, parse_mode="Markdown")
        except Exception as ex:
            telebot.logger.error(ex)
            print("{}: Message could not be sent to groups".format(datetime.now()), file=log)


def notify_subscriber_about_reddit(username, posts):
    if posts is None:
        return
    for post in posts:
        if post_is_fresh(post, "previous{}".format(username.lower())):
            # Compose message text
            message_text = u'[New post from {user}!]({url}) \n\n *{title}* ```\n\n{content}...\n\n```' \
                .format(user=username, url=post.link, title=post.title, content=get_reddit_preview(post.summary))
            notify_users_and_groups(message_text)
            add_post_to_unfresh_list(post, "previous{}.json".format(username.lower()))
        else:
            break  # Post are ordered by date. If one is unfresh all the following ones also are.


def notify_subscriber_about_dota2blog(posts):
    if posts is None:
        return
    for post in posts:
        if post_is_fresh(post, "previousblogposts"):
            # Compose message text
            message_text = u'[New blog post!]({url}) \n\n *{title}* \n\n' \
                .format(
                url = addBlogPostInstantView(post.link), 
                title = post.title)
            notify_users_and_groups(message_text)
            add_post_to_unfresh_list(post, "previousblogposts.json")
        else:
            break  # Post are ordered by date. If one is unfresh all the following ones also are.


def check_for_updates_and_notify():
    posts = get_relevant_sirbelvedere_posts()
    notify_subscriber_about_reddit("SirBelvedere", posts)

    posts = get_relevant_cyborgmatt_posts()
    notify_subscriber_about_reddit("Cyborgmatt", posts)

    posts = get_relevant_magesunite_posts()
    notify_subscriber_about_reddit("Magesunite", posts)

    posts = get_relevant_wykrhm_posts()
    notify_subscriber_about_reddit("wykrhm", posts)

    posts = get_dota2blog_posts()
    notify_subscriber_about_dota2blog(posts)

print("{}: Checking for new posts has started!".format(datetime.now()), file=log)
while True:
    check_for_updates_and_notify()
    time.sleep(10)
