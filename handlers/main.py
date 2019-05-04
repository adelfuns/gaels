#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import webapp2
import jinja2
import os

import model.user as user_info_model

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

		template_values = {
			'usr_info': 
			'info': AppInfo,
		}

		template = JINJA_ENVIRONMENT.get_template("start-page.html")
		self.response.write(template.render(template_values))



app = webapp2.WSGIApplication([
	webapp2.Route(r'/', handler=HomeHandler),
	webapp2.Route(r'/home', handler=HomeHandler),
	webapp2.Route(r'/home/', handler=HomeHandler, name='home'),
], debug=True)