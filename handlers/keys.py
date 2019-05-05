#!/usr/bin/env python

import webapp2
import jinja2
import os

import model.user as user_info_model
import model.key as key_model
import model.appinfo as AppInfo

from google.appengine.api import users

# Defines path to templates
templates_path = os.path.join(os.path.dirname(__file__),'..','templates')

# Defines de Jinja environment
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(templates_path),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class KeyHandler(webapp2.RequestHandler):
	def get(self):
		# User data
		user = users.get_current_user()
		user_info = user_info_model.retrieve(user)

		# Key data
		all_keys = key_model.retrieve_all_keys()

		access_link = users.create_login_url("/")
		template = JINJA_ENVIRONMENT.get_template("keys.html")

		# If the user is logged
		if user_info:
			access_link = users.create_logout_url("/")

		template_values = {
			'keylist': all_keys,
			'usr_info': user_info,
			'info': AppInfo,
			'access_link': access_link,
		}

		self.response.write(template.render(template_values))


class KeyInfoHandler(webapp2.RequestHandler):
	def get(self, keyname):
		# User data
		user = users.get_current_user()
		user_info = user_info_model.retrieve(user)

		# Key data
		unique_key = key_model.retrieve_key(keyname)

		access_link = users.create_login_url("/")
		template = JINJA_ENVIRONMENT.get_template("info-key.html")

		# If the user is logged
		if user_info:
			access_link = users.create_logout_url("/")

		template_values = {
			'key': unique_key,
			'usr_info': user_info,
			'info': AppInfo,
			'access_link': access_link,
		}

		self.response.write(template.render(template_values))


class MapKeyHandler(webapp2.RequestHandler):
	def get(self, keymap):
		# User data
		user = users.get_current_user()
		user_info = user_info_model.retrieve(user)

		# Key data
		keys_by_map = key_model.retrieve_all_keys_by_map(keymap)

		access_link = users.create_login_url("/")
		template = JINJA_ENVIRONMENT.get_template("map-key.html")

		# If the user is logged
		if user_info:
			access_link = users.create_logout_url("/")

		template_values = {
			'keylist': keys_by_map,
			'usr_info': user_info,
			'info': AppInfo,
			'access_link': access_link,
		}

		self.response.write(template.render(template_values))


def createKeys():
	key_model.insert(key_model.create("LkASP Key (Lab Key Alarm System Control Panel)",\
		"","LABS"))
	key_model.insert(key_model.create("LkASR Key (Lab Key Arsenal Storage Room)",\
		"","LABS"))
	key_model.insert(key_model.create("LkSA Key (Lab Key Security Arsenal)",\
		"","LABS"))
	key_model.insert(key_model.create("LkEA Key (Lab Key Experiment's Area)",\
		"","LABS"))
	key_model.insert(key_model.create("LkBL2 Key (Lab Key Laboratory Block Level 2)",\
		"","LABS"))
	key_model.insert(key_model.create("LkMO Key (Lab Key Manager Office)",\
		"","LABS"))
	key_model.insert(key_model.create("LkSP Key (Lab Key Security Post)",\
		"","LABS"))
	key_model.insert(key_model.create("LkQZ key (Lab Key Quarantine Zone)",\
		"","LABS"))
	key_model.insert(key_model.create("LkTA (Lab Key Testing Area weapon)",\
		"","LABS"))
	key_model.insert(key_model.create("Factory Key",\
		"", "FACTORY"))
	key_model.insert(key_model.create("Key (pumping station)",\
		"", "FACTORY"))
	key_model.insert(key_model.create("Key (admin)",\
		"", "FACTORY"))
	key_model.insert(key_model.create("ZB-014",\
		"", "WOODS"))
	key_model.insert(key_model.create("Yotota",\
		"", "WOODS"))
	key_model.insert(key_model.create("Customs Key",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Cabinet Key",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Key (black handle)",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Key (black handle: portable cabin key)",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Unknown Key",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Cabin Key",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Checkpoint Key",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Machinery Key",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Cabin Key (trailer park)",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Dorm Guard Desk key",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Room 104",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Room 105",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Room 206",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Room 110",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Room 114",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Room 108",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Room 108 (Typo: 103)",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Room 118",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Room 203",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Room 204",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Room 214",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Room 218",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Room 220",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Room 303",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Room 306",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Room 308",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Marked Room (314)",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Room 315",\
		"", "CUSTOMS"))
	key_model.insert(key_model.create("Cottage Back Entrance Key",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("Cottage Safe Key",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("SMW Car Key",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("Sanatorium Key",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("Shoreline Utility KeyHealth Resort",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("Health Resort Management Office Safe Key",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("Health Resort Warehouse Safe Key",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("Office 104 West Wing",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("Office 112 West Wing",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("West Wing 203 (205)",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("West Wing 207",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("West Wing 216",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("West Wing 218 (221, 222)",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("West Wing 219",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("West Wing 220",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("West Wing 301",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("West Wing 303",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("West Wing 306",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("West Wing 309",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("321 Safe Key",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("West Wing 323",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("Office 107 East Wing",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("East Wing 206 (+205)",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("East Wing 218 (+221)",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("East Wing 222 (+226)",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("East Wing 301",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("East Wing 306 (+308)",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("East Wing 310",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("East Wing 313 (+315)",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("East Wing 314",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("East Wing 316",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("East Wing 322",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("East Wing 328",\
		"", "SHORELINE"))
	key_model.insert(key_model.create("Goshan Register Keygas station",\
		"", "INTERCHANGE"))
	key_model.insert(key_model.create("IDEA Register Key",\
		"", "INTERCHANGE"))
	key_model.insert(key_model.create("OLI Register Key",\
		"", "INTERCHANGE"))
	key_model.insert(key_model.create("OLI Logistics KeyCustoms",\
		"", "INTERCHANGE"))
	key_model.insert(key_model.create("OLI Admin Office Key",\
		"", "INTERCHANGE"))
	key_model.insert(key_model.create("OLI Utility Room Key",\
		"", "INTERCHANGE"))
	key_model.insert(key_model.create("Pharmacy Key",\
		"", "INTERCHANGE"))
	key_model.insert(key_model.create("Emercom Medical Key",\
		"", "INTERCHANGE"))
	key_model.insert(key_model.create("Substation Utility Key",\
		"", "INTERCHANGE"))
	key_model.insert(key_model.create("KIBA Key",\
		"", "INTERCHANGE"))
	key_model.insert(key_model.create("KIBA Key 2",\
		"", "INTERCHANGE"))
	key_model.insert(key_model.create("Weapons Safe Key",\
		"", "UNKNOWN"))
	key_model.insert(key_model.create("(VAZ) Sixpack Key",\
		"", "UNKNOWN"))
	key_model.insert(key_model.create("Weather Station Safe Key",\
		"", "UNKNOWN"))
	key_model.insert(key_model.create("Gas Station Safe Key",\
		"", "UNKNOWN"))
	key_model.insert(key_model.create("Car Key",\
		"", "UNKNOWN"))


def handle_404(request, response, exception):
    response.write('Oops! I could swear this page was here!')
    response.set_status(404)


def handle_500(request, response, exception):
    response.write('A server error occurred!')
    response.set_status(500)


app = webapp2.WSGIApplication([
	webapp2.Route(r'/keys', handler=KeyHandler, name='keys'),
	webapp2.Route(r'/keys/e/<keyname>', handler=KeyInfoHandler, name='keyinfo'),
	webapp2.Route(r'/keys/m/<keymap>', handler=MapKeyHandler, name='mapkeys'),
], debug=True)

# app.error_handlers[404] = handle_404
# app.error_handlers[500] = handle_500