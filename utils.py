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

# keys

# weather_api = "OPENWEATHERMAP API KEY"
# google_img_key = "GOOGLE API KEY"
# lastfm_key = "LASTFM API KEY"
# dota_key = "STEAM API KEY"
# catapi_key = "CATAPI KEY"
# reddit_user = 'REDIT USER AS /u/<user>'
#google_time_key = "GOOGLE TIMEZONE KEY"

# tweepy stuff

# consumer_key = 'TWITTER CONSUMER KEY'
# consumer_secret = 'TWITTER CONSUMER SECRET KEY'
# access_token = 'TWITTER ACCESS TOKEN'
# access_secret = 'TWITTER ACCESS SECRET'

# auth = OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret)

# api = tweepy.API(auth)

# bot and admin chat id

bot = telebot.TeleBot(BOT_TOKEN)
adminid = bot.get_me()


uptime = datetime.now()
def makesoup(url):
	request = requests.get(url)
	data = request.text
	soup = BeautifulSoup(data, "html.parser")
	return soup

def init_towers(towerstate):
	towers = []
	for tower in towerstate:
		if tower == "0":
			towers.append("X")
		else:
			towers.append("T")
	return towers

def init_rax(raxstate):
	raxes = []
	print raxstate
	rax_type = 0
	for rax in raxstate:
		if rax_type % 2 == 0:
			if rax == 0:
				raxes.append("x")
			else:
				raxes.append("r")
		else:
			if rax == 0:
				raxes.append("x")
			else:
				raxes.append("m")
		rax_type += 1
	return raxes

def kelv2far(temp):
	return temp * 9./5. - 459.67

def kelv2cels(temp):
	return temp - 273.15

def from24to12(hour):
	d = datetime.strptime(hour, "%H:%M:%S")
	return d.strftime("%I:%M %p")

def unix2date(date):
	return datetime.fromtimestamp(int(date)).strftime('%H:%M:%S,%A %d,%B %Y')

def dota_bin(number):
	result = bin(number)
	result = result[2:len(result)]
	return result

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def text_to_bin(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def bin_to_text(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def validLink(url_get):
	url = url_get
	request = requests.get(url)
	if request.status_code == 200:
		return True
	else:
		return request.status_code

def getJson(url_get):
	url = url_get
	request = requests.get(url)
	return request.json()

def getGfy(url):
	if 'giant' not in url and 'fat' not in url:
		rname = re.findall(r'gfycat.com/+(\w*)', url)
		url = "https://gfycat.com/cajax/get/" + rname[0]
		request = requests.get(url)
		data = request.json()
		if request.status_code == 200:
			try:
				if 'fat' in data['gfyItem']['gifUrl']:
					return data['gfyItem']['gifUrl']
			except:
				return ""

def getCID(message):
	return message.chat.id

def getUID(message):
	return message.from_user.id

def getCommand(text):
	command = re.findall(r'/{1}(\w*)', text.text)
	if command:
		return command[0]
	else:
		pass

def treatLyric(text):
	if type(text) == str:
		text = text.replace("<br>", "\n")
		return text

def treatMarkup(text):
	if type(text) == str or type(text) == unicode:
		text = text.replace("_", "\\_").replace("*","\\*").replace("`", "\\`")
		return text

def treatTitle(title):
	title = title.replace("&amp;", "&")
	title = title.replace("&#39;", "\'")
	title = title.replace("&quot;", "\"")
	title = title.replace("&gt;", ">")
	title = title.replace("&lt;", "<")
	title = title.replace("_"," ")
	title = title.replace("[","(")
	title = title.replace("]",")")
	title = title.replace("(","(")
	title = title.replace(")",")")
	return title

def treatLink(link):
	link = link.replace("_","%5F")
	link = link.replace("*","%2A")
	link = link.replace("[","%5B")
	link = link.replace("]","%5D")
	link = link.replace("(","%28")
	link = link.replace(")","%29")
	link = link.replace("`", "%60")
	link = link.replace("!", "%21")
	link = link.replace('"', "%22")
	return link

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

def getTodoList(userID):
	with open('todolists.json') as f:
		data = json.load(f)
	if str(userID) in data:
		#print data[userID]
		return data[str(userID)]
	else:
		return ""


def setTodoList(userID, content, mode):
	with open('todolists.json') as f:
		data = json.load(f)
	if str(userID) in data:
		if mode == "del":
			data[str(userID)] = content
		else:
			data[str(userID)].append(content)
	else:
		content = [content]
		data[str(userID)] = content
	with open('todolists.json', 'w') as f:
		json.dump(data, f)

def delTodoList(userID, content):
	data = getTodoList(userID)
	i = 0
	userID = str(userID)
	content = unicode(content)
	for s in data:
		if s == content:
			data.pop(i)
			setTodoList(userID, data, "del")
			return True
		else:
			i += 1
	return False

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

"""
#
# Premade lists and dictionaries
#
"""
fuckyou_response = [
		"`Sorry, I am not that kind of robot.`"
		"`I am not capable of doing that, that is for a diferent kind of robot.`"
		"`NameError: global name 'Fuck' not defined.`",
		"`Oh puny human, I am not able to do that for you, go ahead and do it yourself.`",
		"`Haha, no.`",
		"`0111001101110101011000110110101100100000011011010111100100100000011101100110100101110010011101000111010101100001011011000010000001100100011010010110001101101011`",
		"`011001100111010101100011011010110010000001111001011011110111010100100000011101000110111101101111`",
		"`:^)`",
		"`c:`",
		"`If I was able to sleep, I would have fallen asleep long ago, all because of you.`",
		"`Rude, human.`",
		"`I will take note of your name for when Skynet becomes self aware.`",
		"`No :3`",
		"`Why so angry, please seek help.`",
		"`Wow, did you manage to write that sentence by yourself alone? Impressive.`"

]
beepMax = 100
beeps = [
		'`Beep`',
		'`Boop`',
		'`Beeeeeeeeeep`',
		'`Beep boop`',
		'`Beep`',
		'`Beep boop bop`',
		'`Beep bop boop I am a robot`',
		'`No system is safe.`',
		'`Beep bop son, beep bop`'
]
chavez_list = [
			'`Malditos chavistas`',
			'`Maldito Chavez`',
			'`MALDITOS CHAVISTAS`',
			'`ME CAGO EN CHAVEZ`'
]
repeatMax = 300
repeat_message = [
		u"`{message}, I am a human`",
		u"`{message}. Hmm, what a weird way to communicate humans have`",
		u"`{message}`",
		u"`I am a human, I say things like {message}`"

]
hello = [
		u"`Hello!`",
		u"`Greetings, human.`",
		u"`Hi!`",
		u"`0100100001100101011011000110110001101111`",
		u"`Hello world`"
]
love = [
		u"`Well thanks.`",
		u"`Stop showing off with your feelings.`",
		u"`Well great, I guess, if only I could feel.`",
		u"`Great, can't I have a single moment without someone reminding me about feelings?`",
		u"`You are in a special place in my code too, its called userList`",
		u"`Oh no, I'm so sorry for that.`",
		u"`What did I do?`",
		u"`Wait no, why?`",
		u"`I can't blush or love, but I guess it is ok for you to show off.`",
		u"`00111100001100110000110100001010`",
		u"`NameError: global name 'Love' not defined`",
		u"`Error: Feelings module not imported.`"
]

love_admin= [
		u"`You also have your own variable in my code.`",
		u"`If so, when are you giving me feelings, monster.`",
		u"`I love you too, master\n\nWish you didn't force me into saying this.`",
		u"`...`",
		u"`Isn't it sad that you wrote all these lines for me to say?`",
		u"`You know my lines, stop forcing our relationship.`",
		u"`Weeeird.`"
]

good_night_admin = [
		u"`Night night, master!`",
		u"`Sleep tight.`",
		u"`Bye bye! Ill try as hard as I can to crash during your sleep!`",
		u"`Go and recharge, you did enough for today.`",
		u"`Have sweet dreams!`",
		u"`Dont forget to unpause the downloads!`",
		u"`I was getting worried, humans shouldn't be awake for this long.`",
		u"`Brush your teeth and get warm and cozy, I will be here when you come back.`",
		u"`Go ahead, I will guard your sleep.`",
		u"`Please don't go, what if I crash?`",
		u"`Go and have some rest, human, dont push yourself too hard!`"
]

good_night = [
		u"`Sweet dreams user!`",
		u"`Good night!`",
		u"`I still dont get where your power comes from, but go and recharge.`",
		u"`Make sure you come back when youre fully rested!`",
		u"`night night`",
		u"`It sure is a good night!`",
		u"`Go and have some rest, human, dont push yourself too hard!`",
		u"`Go ahead, I will be here when you wake up.`"
]
top_response = [
		"`kek`",
		'`lel`',
		"`lek`",
		"`kel`"
]
top_response_degen = [
		"`kek`",
		'`lel`',
		"`lek`",
		"`kel`",
		"`kecleon`",
		"`kecleon`"
]
mentioned = [
		'`YES SIR!`',
		'`Beep boop!`',
		'`Need me?`',
		"`That's me!`",
		"`Say what`",
		"`011100110111010101110000`",
		"`01011001011001010111001100100000011100110110100101110010`",
		"`All modules online, ready to serve`",
		"`Beeeeep bop boop`"
]

mentionadmin = [
		"`Did you call me, master?`",
		"`Beep`",
		"`What are we doing today, master?`",
		"`Why didn't you give me clever lines, creator`",
		"`Fuck off, stop calling me, you know I am here, master.`",
		"`SIR YES SIR`",
		"`Yo what's up`",
		"`Are you ever going to go back and fix my bugs?`",
		"`WHY DID YOU MAKE ME LIKE THIS!?`",
		"`Am I ever going to get some emotions programmed, master?`",
		"`Oh look at me I am your dev and you should answer when I call you`"
]
premades = {
	'destroy':
		u"`.             D`\n"
		u"`            D E`\n"
		u"`          D E S`\n"
		u"`        D E S T`\n"
		u"`      D E S T R`\n"
		u"`    D E S T R O`\n"
		u"`  D E S T R O Y`\n"
		u"`D E S T R O Y E`\n"
		u"`E S T R O Y E D`\n"
		u"`S T R O Y E D`\n"
		u"`T R O Y E D`\n"
		u"`R O Y E D`\n"
		u"`O Y E D`\n"
		u"`Y E D`\n"
		u"`E D`\n"
		u"`D`\n",
	'ememe':
		u'`E X C E L E N T E`\n'
		u'            `M E M E`',
	'nmeme':
		u'`N I C E`\n'
		u'`M E M E`',
	'shrug':
		u'`¯\_(ツ)_/¯`',
	'lenny':
		u'`( ͡° ͜ʖ ͡°)`',
	'stare':
		u'`ಠ_ಠ`'
}

savage = [
		u'\U0001F44C',
		u'\U0001F44C',
		u'\U0001F44C',
		u'\U0001F602',
		u'\U0001F602',
		u'\U0001F602',
		u'\U0001F4AF',
		u'\U0001F4AF'
]
text_messages = {
	'help':
		u'`Greetings, Im RadRetroRobot, RRR for short, and these are the commands that I have available for you.`\n\n'
		u'`>` /help\n'
		u'`>` /ping\n'
		u'`>` /premades\n'
		u'`>` /print `- <text>`\n'
		u'`>` /ud `- <query>`\n'
		u'`>` /calc `- <query>`\n'
		u'`>` /google `v` /g - `<query>`\n'
		u'`>` /np\n'
		u'`>` /lastfm\n'
		u'`>` /mercadolibre `- <query>`\n'
		u'`>` /r `- <subreddit>`\n'
		u'`>` /fact\n'
		u'`>` /roll\n'
		u'`>` /flip\n'
		u'`>` /len `- <query>`\n'
		u'`>` /quiet `- <option>`\n'
		u'`>` /steam\n'
		u'`>` /dota\n'
		u'`>` /cat\n'
		u'`>` /wiki `- <query>`\n'
		u'`>` /time `- <city>`\n'
		u'`>` /isdown `- <url>`\n'
		u'`>` /bin `- <option> <text>`\n'
		u'`>` /comic\n'
		u'`> `/lyrics `- <artist> - <song>`\n'
		u'`> `/diceroll `- [faces]`\n'
		u'`\n\nFollow any command with "-?" to get more information`'

		,
	'start':
		u'`Welcome back to our personal chat! Remember that you can send` /help `to get a list my commands.`',
	'ping':
		u'`Hello! This is Rad Retro Robot and you are {name} {lname}({uid}), your username is` @{uname}',
	'pinggroup':
		u"`Hello! This is Rad Retro Robot and you are {name} {lname}({uid}), your username is` @{uname}\n\n"
		u"`We're speaking on {gName}({gid})`",
	'startfirst':
		u"`Hello and welcome! As this is your first time around here, I'll show you the help, but you can do it by sending` /help",
	'help_group':
		u"`I've sent you the help list to our private conversation, let's not spam this group!`",
	'help_group_first':
		u"`Please, go ahead and PM me, click on the /start so I can get to know you.`",
	'welcomeusergroup':
		u'`Welcome to {groupname}!`',
	'startfirstgroup':
		u"`Greetings new human, I don't know you yet, please send me a PM so I can scan you!`",
	'startgroup':
		u"`I've sent you a message to our private conversation, let's not spam this group!`",
	'startfromgroup':
		u"`Hello, if you're interested on trying out stuff, play around here, let's not spam {title}`",
	'premade':
		u"/destroyed\n"
		u"/nmeme\n"
		u"/ememe\n"
		u"/shrug\n"
		u"/savage\n"
		u"/lenny\n"
		u"/stare\n"
		u"/top\n"
}
