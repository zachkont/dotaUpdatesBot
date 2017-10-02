#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import requests
import time
import json
import re
import datetime
import binascii
from bs4 import BeautifulSoup
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

def addUser(userID, userName, filename):
	user = {
		userID : userName
	}
	with open(filename + '.json') as f:
		data = json.load(f)
	data.update(user)
	with open(filename + '.json', 'w') as f:
		json.dump(data, f)

def loadjson(filename):
	with open(filename + '.json') as f:
		data = json.load(f)
		if filename == "suggestion" or filename == 'todo':
			data = SortedDict(data)
	return data

def deljson(value, filename):
	data = loadjson(filename)
	for key in data.keys():
		if key == value:
			del data[key]
			with open(filename + '.json', 'w') as f:
				json.dump(data, f)
			return True
			break
		elif data[key] == value:
			del data[key]
			with open(filename + '.json', 'w') as f:
				json.dump(data, f)
			return True
	return False

def intime(message):
	timeRange = time.mktime(datetime.now().timetuple())
	if int(timeRange - message.date) < 10:
		if message.forward_from == None:
			return True
	else:
		return False
