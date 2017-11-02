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

def match_short_description(match):
	"""Creates a short Markdown description for given match with ID, Dotabuff link, league, teams, and winner"""
	# Match ID with link
	# Match league if exists
	# Teams if both exist
	# Winner

	dotabuff_url = 'https://www.dotabuff.com/matches/'

	match_id = match['match_id']
	match_url = dotabuff_url + unicode(match_id)
	match_text = '[{id}]({url})'
	match_text = match_text.format(id=match_id, url=match_url)

	league = match['league_name']
	league_text = u'\n{league}'
	league_text = league_text.format(league=league) if league is not None else ''

	radiant_name = match['radiant_name']
	dire_name = match['dire_name']
	team_names = u'\n{radiant} vs. {dire}'
	team_names = team_names.format(radiant=radiant_name, dire=dire_name) if radiant_name and dire_name else ''

	if match['radiant_win']:
		if radiant_name is not None:
			winner = radiant_name
		else:
			winner = 'Radiant'
	else:
		if dire_name is not None:
			winner = dire_name
		else:
			winner = 'Dire'

	winner_text = '\nWinner: {winner}'
	winner_text = winner_text.format(winner=winner)

	text = '{id}```{league}{names}{winner}```'
	text = text.format(id=match_text, league=league_text, names=team_names, winner=winner_text)

	return text
