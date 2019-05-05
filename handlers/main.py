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


class HomeHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()
		user_info = user_info_model.retrieve(user)

		if user and user_info:
			access_link = users.create_logout_url("/")
		else:
			access_link = users.create_login_url("/")

		template_values = {
			'usr_info': user_info,
			'info': AppInfo,
			'access_link': access_link,
		}

		template = JINJA_ENVIRONMENT.get_template("start-page.html")
		self.response.write(template.render(template_values))


def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('Oops! I could swear this page was here!')
    response.set_status(404)


def handle_500(request, response, exception):
    logging.exception(exception)
    response.write('A server error occurred!')
    response.set_status(500)


app = webapp2.WSGIApplication([
	webapp2.Route(r'/', handler=HomeHandler),
	webapp2.Route(r'/home', handler=HomeHandler),
	webapp2.Route(r'/home/', handler=HomeHandler, name='home'),
], debug=True)

app.error_handlers[404] = handle_404
app.error_handlers[500] = handle_500