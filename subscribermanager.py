#!/usr/bin/env python
from datamanager import DictManager

USERFILE = 'userlist.json'
GROUPFILE = 'grouplist.json'

def addUser(user_id, username):
	manager = DictManager(USERFILE)
	manager.add((user_id, username))

def getUsers():
	manager = DictManager(USERFILE)
	return manager.data()

def deleteUser(user_id):
	manager = DictManager(USERFILE)
	return manager.delete(user_id)

def addGroup(group_id, group_name):
	manager = DictManager(GROUPFILE)
	manager.add((group_id, group_name))

def getGroups():
    manager = DictManager(GROUPFILE)
    return manager.data()

def deleteGroup(group_id):
    manager = DictManager(GROUPFILE)
    return manager.delete(group_id)