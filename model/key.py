#!/usr/bin/env python

from google.appengine.ext import ndb
from google.appengine.api import users


class GameKey(ndb.Model):
	name = ndb.TextProperty(indexed=True, required=True)
	image_path = ndb.TextProperty(indexed=True, required=True)
	keymap = ndb.TextProperty(indexed=True, required=True)
	description = ndb.TextProperty(indexed=True)

	def __str__(self):
		return unicode(self).encode('utf-8')

	def __unicode__(self):
		return self.name + " from " + self.keymap


def create(name,image_path=None,keymap="UNKNOWN",description=""):
	toret = GameKey()

	toret.name = name
	toret.image_path = image_path
	toret.keymap = keymap
	toret.description = description

	return toret;


@ndb.transactional
def insert(key):
	return key.put()


def retrieve_all_keys():
	toret = []

	found_keys = GameKey.query().order(-GameKey.keymap).fetch()

	for key_entity in found_keys:
		toret.append(key_entity)

	return toret


def retrieve_all_keys_by_map(map):
	toret = []

	found_keys = GameKey.query(GameKey.keymap == map).fetch()

	for key_entity in found_keys:
		toret.append(key_entity)

	return toret


def retrieve_key(name):

	found_key = GameKey.query(GameKey.name == name)

	if found_key.count() == 0:
		return None

	return found_key.iter().next()