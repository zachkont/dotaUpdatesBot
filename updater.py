from __future__ import print_function

import time
from datetime import datetime
import sys
import telebot
import json
import feedparser
from utils import loadjson

from settings import BOT_TOKEN
from settings import CRISIS_ACCOUNT



print("updater started")

dota_blog_rss_url = "http://blog.dota2.com/feed/"
steam_news_json_url = "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=570&maxlength=300&format=json"
belvedere_reddit_rss_url = "https://www.reddit.com/user/SirBelvedere/.rss"
cyborgmatt_reddit_rss_url = "https://www.reddit.com/user/Cyborgmatt/.rss"
magesunite_reddit_rss_url = "https://www.reddit.com/user/Magesunite/.rss"

bot = telebot.TeleBot(BOT_TOKEN)

stdout =  open('stdout.txt', 'a')
sys.stdout = stdout

log = open(r'log.txt', 'a')

while True:

    try:
        blog_feed = feedparser.parse( dota_blog_rss_url )
        #print ("Blog feed status= " + blog_feed.status)
        if blog_feed.status == 200:
            blog_content = unicode(blog_feed["items"][0]["summary"])
            try:
                blog_content, trash = blog_content.split('&#8230', 1 )
            except:
                print ("%s no &#8230 found" %str(datetime.now()), file=log)
        else:
            blog_content = None
    except:
        blog_content = None
        print ("%s Unexpected error. ECODE:1001"%str(datetime.now()), file=log)

    #try:
    #    request = requests.get(steam_news_json_url)
    #    if request.status_code == 200:
    #        data = request.json()
    #    else:
    #        data = None
    #except:
    #    print ("%s Unexpected error. ECODE:1002"%str(datetime.now()), file=log)

    try:
        belve_feed = feedparser.parse( belvedere_reddit_rss_url )
        #print ("Belve feed status= " + belve_feed.status)
        if belve_feed.status == 200:
            belve_content = belve_feed["items"][0]["summary"]
            belve_content = belve_content[1:100]
        else:
            belve_content = None
    except:
        belve_content = None
        print ("%s Unexpected error. ECODE:1003"%str(datetime.now()), file=log)

    try:
        cyborgmatt_feed = feedparser.parse( cyborgmatt_reddit_rss_url )
        #print ("Cybrogmatt feed status= " + cyborgmatt_feed.status)
        if cyborgmatt_feed.status == 200:
            cyborgmatt_content = cyborgmatt_feed["items"][0]["summary"]
            cyborgmatt_content = cyborgmatt_content[1:100]
        else:
            cyborgmatt_content = None
    except:
        cyborgmatt_content = None
        print ("%s Unexpected error. ECODE:1013"%str(datetime.now()), file=log)

	try:
        magesunite_feed = feedparser.parse( magesunite_reddit_rss_url )
        #print ("Magesunite feed status= " + magesunite_feed.status)
        if magesunite_feed.status == 200:
            magesunite_content = magesunite_feed["items"][0]["summary"]
            magesunite_content = magesunite_content[1:100]
        else:
            magesunite_content = None
    except:
        magesunite_content = None
        print ("%s Unexpected error. ECODE:1023"%str(datetime.now()), file=log)
		
    if blog_content is not None:
        #try:
        #    print (blog_feed["items"][0]["title"] + " |time: %s" %str(datetime.now()))
        #except:
        #    print ("%s MANASU. ECODE:9001"%str(datetime.now()), file=log)
        for blogpost in blog_feed.entries:
            if blogpost.title not in loadjson("previousblogposts"):
                for uid in loadjson("userlist"):
                    try:
                        bot.send_message(uid, '[New blog post!]({url}) \n\n *{title}* ```\n\n{content}...\n\n```'.format(url = blogpost.link, title=blogpost.title, content=blog_content), parse_mode="Markdown")
                    except:
                        print ("%s Unexpected error. ECODE:0001"%str(datetime.now()), file=log)
                for gid in loadjson("grouplist").keys():
                    try:
                        bot.send_message(gid, '[New blog post!]({url}) \n\n *{title}* ```\n\n{content}...\n\n```'.format(url = blogpost.link, title=blogpost.title, content=blog_content), parse_mode="Markdown")
                    except:
                        print ("%s Unexpected error. ECODE:0002"%str(datetime.now()), file=log)

                entry = { blogpost.title : blogpost.link }
                with open('previousblogposts.json') as f:
                    data = json.load(f)
                data.update(entry)
                with open('previousblogposts.json', 'w+') as f:
                    json.dump(data, f)

    #if data is not None:
    #   jsonid = data['appnews']['newsitems'][0]['gid']
    #    jsontitle = data['appnews']['newsitems'][0]['title']
    #    jsoncontent = data['appnews']['newsitems'][0]['contents']
    #    jsoncontent_nice = jsoncontent.replace(" - ", "\n - ")
    #    jsonurl = data['appnews']['newsitems'][0]['url']
    #
    #    if jsonid not in loadjson("previousjasons") and "Dota 2 Update" in jsontitle:
    #        for uid in loadjson("userlist"):
    #            try:
    #                bot.send_message(uid, '*{title}*```> \nSteam news entry!\n\n{content_nice}\n\n```'.format(title=jsontitle, content_nice=jsoncontent_nice) + '[More info here]({url})'.format(url=jsonurl), parse_mode="Markdown", disable_web_page_preview=True)
    #            except:
    #                print ("%s Unexpected error. ECODE:0003 "%str(datetime.now()), file=log)
    #        for gid in loadjson("grouplist").keys():
    #            try:
    #                bot.send_message(gid, '*{title}*```> \nSteam news entry!\n\n{content_nice}\n\n```'.format(title=jsontitle, content_nice=jsoncontent_nice) + '[More info here]({url})'.format(url=jsonurl), parse_mode="Markdown", disable_web_page_preview=True)
    #            except:
    #                print ("%s Unexpected error. ECODE:0004"%str(datetime.now()), file=log)
    #
    #        entry = { jsonid : jsonurl }
    #        with open('previousjasons.json') as f:
    #            data = json.load(f)
    #        data.update(entry)
    #        with open('previousjasons.json', 'w') as f:
    #            json.dump(data, f)

    if belve_content is not None:
        #try:
        #    print (belve_feed["items"][0]["title"] + " |time: %s" %str(datetime.now()))
        #except:
        #    print ("%s MANASU. ECODE:9002"%str(datetime.now()), file=log)
        for post in belve_feed.entries:
            if post.title not in loadjson("previousbelvedere"):
                if (("/u/SirBelvedere on" not in post.title) and ("Dota 2 Update" in post.title)):
                    for uid in loadjson("userlist"):
                        try:
                            bot.send_message(uid, '[New post from SirBelvedere!]({url}) \n\n *{title}* ```\n\n```'.format(url = post.link ,title=post.title), parse_mode="Markdown")
                        except:
                            print ("%s Unexpected error. ECODE:0005"%str(datetime.now()), file=log)
                    for gid in loadjson("grouplist").keys():
                        try:
                            bot.send_message(gid, '[New post from SirBelvedere!]({url}) \n\n *{title}* ```\n\n```'.format(url = post.link ,title=post.title), parse_mode="Markdown")
                        except:
                            print ("%s Unexpected error. ECODE:0006"%str(datetime.now()), file=log)
                    entry = { post.title : post.link }
                    with open('previousbelvedere.json') as f:
                        data = json.load(f)
                    data.update(entry)
                    with open('previousbelvedere.json', 'w+') as f:
                        json.dump(data, f)
						
	if mages_content is not None:
        #try:
        #    print (belve_feed["items"][0]["title"] + " |time: %s" %str(datetime.now()))
        #except:
        #    print ("%s MANASU. ECODE:9002"%str(datetime.now()), file=log)
        for post in belve_feed.entries:
            if post.title not in loadjson("previousmagesunite"):
                if (("/u/Magesunite on" not in post.title) and ("Dota 2 Update" in post.title)):
                    for uid in loadjson("userlist"):
                        try:
                            bot.send_message(uid, '[New post from Magesunite!]({url}) \n\n *{title}* ```\n\n```'.format(url = post.link ,title=post.title), parse_mode="Markdown")
                        except:
                            print ("%s Unexpected error. ECODE:0015"%str(datetime.now()), file=log)
                    for gid in loadjson("grouplist").keys():
                        try:
                            bot.send_message(gid, '[New post from Magesunite!]({url}) \n\n *{title}* ```\n\n```'.format(url = post.link ,title=post.title), parse_mode="Markdown")
                        except:
                            print ("%s Unexpected error. ECODE:0016"%str(datetime.now()), file=log)
                    entry = { post.title : post.link }
                    with open('previousmagesunite.json') as f:
                        data = json.load(f)
                    data.update(entry)
                    with open('previousmagesunite.json', 'w+') as f:
                        json.dump(data, f)
					

    if cyborgmatt_content is not None:
        #try:
        #    print (cyborgmatt_feed["items"][0]["title"] + " |time: %s" %str(datetime.now()))
        #except:
        #    print ("%s MANASU. ECODE:9002"%str(datetime.now()), file=log)
        for post in cyborgmatt_feed.entries:
            if post.title not in loadjson("previouscyborgmatt"):
                if (("/u/Cyborgmatt on" not in post.title) and ("Dota 2 Update" in post.title)):
                    for uid in loadjson("userlist"):
                        try:
                            bot.send_message(uid, '[New post from Cyborgmatt!]({url}) \n\n *{title}* ```\n\n```'.format(url = post.link ,title=post.title), parse_mode="Markdown")
                        except:
                            print ("%s Unexpected error. ECODE:0025"%str(datetime.now()), file=log)
                    for gid in loadjson("grouplist").keys():
                        try:
                            bot.send_message(gid, '[New post from Cyborgmatt!]({url}) \n\n *{title}* ```\n\n```'.format(url = post.link ,title=post.title), parse_mode="Markdown")
                        except:
                            print ("%s Unexpected error. ECODE:0026"%str(datetime.now()), file=log)
                    entry = { post.title : post.link }
                    with open('previouscyborgmatt.json') as f:
                        data = json.load(f)
                    data.update(entry)
                    with open('previouscyborgmatt.json', 'w+') as f:
                        json.dump(data, f)

    time.sleep(180)

try:
    bot.send_message("76932858", "Something terrible has happenned!!!!!!!!!!")
except:
    print ("%s Unexpected error. ECODE:1111"%str(datetime.now()), file=log)
