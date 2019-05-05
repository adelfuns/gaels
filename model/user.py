from google.appengine.ext import ndb
from google.appengine.api import users


class User(ndb.Model):
	added = ndb.DateProperty(auto_now_add=True, indexed=True)
	user_id = ndb.TextProperty(required=True, indexed=True)
	nickname = ndb.TextProperty(required=True, indexed=True)
	permissions_level = ndb.IntegerProperty(required=True, indexed=True,\
		default="0")
	game_level = ndb.IntegerProperty(default=10)
	pmc_type = ndb.TextProperty(default="")
	
	def is_admin(self):
		return self.permissions_level == 100 or \
			users.is_current_user_admin()

	def is_ordinary(self):
		return self.permissions_level == 10

	def is_visitor(self):
		return self.permissions_level == 0

	def __str__(self):
		return unicode(self).encode('utf-8')

	def __unicode__(self):
		return str(self.permissions_level) + ": " + self.nickname


def create(usr, nickname="default", level=0, game_level=None, pmc_type=None):
	toret = User()
	toret.user_id = usr.user_id()
	toret.nickname = nickname
	toret.permissions_level = level
	toret.game_level = game_level
	toret.pmc_type = pmc_type

	return toret


@ndb.transactional
def insert(user):
	return user.put()


def retrieve(usr):

	toret = None

	if usr:
		usr_id = usr.user_id()
		found_user = User.query(User.user_id == usr_id)

		if (found_user.count() == 0 and users.is_current_user_admin()):
			toret = create(usr, "admin", 100)
			insert(toret)
		else:
			if found_user.count() == 0:
				toret = create(usr,nickname=usr.email())
				insert(toret)
			else:
				toret = found_user.iter().next()
				toret.usr = usr

	return toret


def retrieve_by_nickname(nickname):

	found_user = User.query(User.nickname == nickname)

	if found_user.count() == 0:
		return None

	return found_user.iter().next()

# def delete(usr):
