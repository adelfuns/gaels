#!/usr/bin/env python

import webapp2
import jinja2
import os

import model.user as user_info_model

from google.appengine.api import users
from model.appinfo import AppInfo

# Defines path to templates
templates_path = os.path.join(os.path.dirname(__file__),'..','templates')

# Defines de Jinja environment
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(templates_path),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class ProfileHandler(webapp2.RequestHandler):
	def get(self, username):
		user = users.get_current_user()
		access_link = users.create_logout_url("/")
		user_info = user_info_model.retrieve_by_nickname(username)
		my_profile = user_info_model.retrieve(user)
		form_info = "readonly"
		template = JINJA_ENVIRONMENT.get_template("profile.html")

		if user_info:
			if user.user_id() == user_info.user_id:
				form_info = "enabled"
				template = JINJA_ENVIRONMENT.get_template("update-profile.html")
		else:
			self.redirect("/home")

		template_values = {
			'form': form_info,
			'usr_info': user_info,
			'info': AppInfo,
			'access_link': access_link,
		}

		self.response.write(template.render(template_values))


class UpdateProfile(webapp2.RequestHandler):
	def load_input(self):
		self.nickname = self.request.POST['nickname-input']
		self.level = self.request.POST['level-input']
		self.pmc = self.request.POST['pmc-input']

	def post(self, username):
		self.load_input()
		user = users.get_current_user()
		user_info = user_info_model.retrieve(user)

		if user.user_id() == user_info.user_id:
			if user_info.is_admin():
				pemissions_level = 100
			else:
				pemissions_level = 10
			user_to_update = user_info_model.create(user,self.nickname,pemissions_level,\
				int(self.level,10), self.pmc)
			user_to_update.key = user_info.key
			user_info_model.insert(user_to_update)

		self.redirect("/profile/"+self.nickname)


def handle_404(request, response, exception):
    response.write('Oops! I could swear this page was here!')
    response.set_status(404)


def handle_500(request, response, exception):
    response.write('A server error occurred!')
    response.set_status(500)

app = webapp2.WSGIApplication([
	webapp2.Route(r'/profile/<username>',\
		handler=ProfileHandler, name="profile"),
	webapp2.Route(r'/update-profile/<username>',\
		handler=UpdateProfile, name="update-profile")
], debug=True)

app.error_handlers[404] = handle_404
app.error_handlers[500] = handle_500