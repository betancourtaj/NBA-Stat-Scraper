import re 

class Player(object):
	def __init__(self, name, position, player_team_name, minutes, fg, three_point, ft, oreb, dreb, reb, stl, blk, to, pts):
		self.name = name
		self.position = position
		self.player_team_name = player_team_name
		self.minutes = minutes
		self.three_point = three_point
		self.ft = ft
		self.oreb = oreb
		self.dreb = dreb
		self.reb = reb
		self.stl = stl
		self.blk = blk
		self.to = to
		self.pts = pts

	def get_first_name(self):
		return self.name.split()[0]
	def get_last_name(self):
		return self.name.split()[1]

	def get_three_pointers_made(self):
		if self.three_point == '0':
			return '0'
		else:
			return self.three_point.replace('-', ' ').split(' ')[0]
	
	def get_three_pointers_attempted(self):
		if self.three_point == '0':
			return '0'
		else:
			return self.three_point.replace('-', ' ').split(' ')[1]

	def get_free_throws_made(self):
		if self.ft == '0':
			return '0'
		else:
			return self.ft.replace('-', ' ').split(' ')[0]
	
	def get_free_throws_attempted(self):
		if self.ft == '0':
			return '0'
		else:
			return self.ft.replace('-', ' ').split(' ')[1]




