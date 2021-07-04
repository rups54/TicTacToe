import scene
import ui

class Session(scene.Scene):
	def setup(self):
		self.player = 1
		self.p1moves = []
		self.p2moves = []
		self.win = False
		self.image = 'emj:Red_Ring'
		print(self.player)
		w,h = self.size
		print(w)
		print(h)
		mw = 46
		mh = 37
		gap = 100
		create_b = {
		'1': [410, 280],
		'2': [510, 280],
		'3': [610, 280],
		'4': [410, 380],
		'5': [510, 380],
		'6': [610, 380],
		'7': [410, 480],
		'8': [510, 480],
		'9': [610, 480]
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
			s = scene.get_screen_size()
			print(s)
			print(self.size /2  )
			
		
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
			w,h = self.size
			winnertext = scene.LabelNode('Winner!!!!',font=('Helvetica', 100))
			winnertext.position = self.size / 2
			self.add_child(winnertext)
			reset = ui.Button(name='reset')
			reset.frame = (10, 10, 90, 90)
			reset.flex = 'LRTB'
			reset.border_width = 1
			reset.corner_radius = 6
			self.view.add_subview(reset)
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
				
				
				
scene.run(Session())

