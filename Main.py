import ui
#rups

class Session(object):
	def __init__(self):
		self.player = 1
		self.p1moves = []
		self.p2moves = []
		self.win = False
		self.image = 'emj:Red_Ring'
		print(self.player)
		self.view = ui.View()
		w, h = ui.get_screen_size()
		print(w, h)
		self.view.name = 'Rups Tic Tac Toe'  # [2]
		self.view.background_color = 'white'  # [3]
		
		create_b = {
		'1': [3, 3],
		'2': [5, 3],
		'3': [7, 3],
		'4': [3, 5],
		'5': [5, 5],
		'6': [7, 5],
		'7': [3, 7],
		'8': [5, 7],
		'9': [7, 7]
		}
		for k, v in create_b.items():
			a = 'button' + k
			a = ui.Button(name=k)
			a.frame = (v[0], v[1], 90, 90)
			a.flex = 'LRTB'
			a.border_width = 1
			a.corner_radius = 6
			a.action = self.button_tapped
			a.background_image = ui.Image.named('card:BackBlue1')
			self.view.add_subview(a)
		self.view.present()
		
	def button_create():
		print('testing')
		
	def button_tapped(self, sender):
		self.sel_square(sender)
		sender.enabled = False
		self.check_winner()
		if not self.win:
			self.switch_player()
		else:
			sender.title = 'WINNER'
			
	def sel_square(self, sender):
		sender.background_image = ui.Image.named(self.image)
		if self.player == 1:
			self.p1moves.append(int(sender.name))
		else:
			self.p2moves.append(int(sender.name))
			
			
	def switch_player(self):
		if self.player == 1:
			self.player = 2
			self.image = 'emj:Cross_Mark'
		else:
			self.player = 1
			self.image = 'emj:Red_Ring'
			
	def check_winner(self):
		combo = [[1, 2, 3], [1, 5, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7],
		[4, 5, 6], [7, 8, 9]]
		
		for x in combo:
			if self.player == 1:
				mylist = self.p1moves
			else:
				mylist = self.p2moves
			a = set(x) & set(mylist)
			if len(a) == 3:
				print('winner found, player ,',self.player, x)
				self.win = True
				break
				
				
				
v = Session()

