#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import time
import json
import re
import datetime
from sortedcontainers import SortedDict
from datetime import datetime
from settings import BOT_TOKEN

# bot and admin chat id
bot = telebot.TeleBot(BOT_TOKEN)
adminid = bot.get_me()

uptime = datetime.now()

def getCID(message):
	return message.chat.id

def getContent(text):
	command = re.findall(r'/{1}\w+[@RadRetroRobot]*\s+(.*)', text.text, re.DOTALL)
	if command:
		whole = ""
		for line in command:
			if line == "":
				whole += "\n"
			else:
				whole += line
		return whole
	else:
		pass

def intime(message):
	timeRange = time.mktime(datetime.now().timetuple())
	if int(timeRange - message.date) < 10:
		if message.forward_from == None:
			return True
	else:
		return False

def addBlogPostInstantView(url):
  prefix = 'https://t.me/iv?url='
  postfix = '&rhash=ef812bf2b658b4'
  instant_view_link = prefix + url + postfix
  return instant_view_link
