
class Player(object):
	def __init__(self, role, alive, moderator):
		self.role = role
		self.alive = alive
		self.moderator = moderator

class Werewolf(Player):
	role = "Werewolf"
	alive = True
	def getAlive(self):
		return self.alive
	def getRole(self):
		return self.role

class Villager(Player):
	role = "Villager"
	alive = True
	def getAlive(self):
		return self.alive
	def getRole(self):
		return self.role

class Moderator(Player):
	role = "Moderator"
	
class Action(object):
	def death(killed):
		killed.alive = False
	def receiveRole(player, role):
		player.role = role
		
class Village(object):
	def __init__(self, players):
		self.players = players
		
class Time(object):
	pass