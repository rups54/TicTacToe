import scene
import ui

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
		self.make_board()
	
	def make_board(self):
		for k, v in create_b.items():
			main_b = self.make_button(k, v[0], v[1], 'card:BackBlue1')
			main_b.action = self.button_tapped_game
			main_b.background_color = 'white'
			self.view.add_subview(main_b)
			
			
	def make_button(self, bname, bh, bw, bimage):
		a = ui.Button(name=bname)
		print(bname)
		a.frame = (bh, bw, 90, 90)
		a.flex = 'LRTB'
		a.border_width = 1
		a.corner_radius = 6
		a.background_image = ui.Image.named(bimage)
		return a
		
	def button_create():
		print('testing')
		
	def button_tapped_game(self, sender):
		print('im here')
		self.sel_square(sender)
		sender.enabled = False
		win = self.check_winner()
		if not self.win:
			self.switch_player()
		else:
			z = sender.superview
			for v in sender.superview.subviews:
				print (v.name)
			print(win)
			for i in win:
				z[str(i)].background_color= 'yellow'
			w,h = self.size
			restart_b = self.make_button('restart', 10, 10,'typb:Back' )
			restart_b.background_color = 'white'
			self.view.add_subview(restart_b)
			restart_b.action = self.restart_game
			
	def restart_game(self,sender):
		self.player = 1
		self.win = False
		self.p1moves = []
		self.p2moves = []
		

	
	def sel_square(self, sender):
		print(sender.name)
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
		print('checking winner')
		combo = [[1, 2, 3], [1, 5, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7],
		[4, 5, 6], [7, 8, 9]]
		
		for wincombo in combo:
			if self.player == 1:
				mylist = self.p1moves
			else:
				mylist = self.p2moves
				print(mylist)
			a = set(wincombo) & set(mylist)
			if len(a) == 3:
				print('winner found, player ,',self.player, wincombo)
				self.win = True
				break
		return wincombo
				
				
scene.run(Session())

