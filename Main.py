import scene
import ui
import time

create_b = {
		'1': [280, 280, 410],
		'2': [280, 280, 510],
		'3': [280, 280, 610],
		'4': [280, 380, 410],
		'5': [280, 380, 510],
		'6': [280, 380, 610],
		'7': [280, 480, 410],
		'8': [280, 480, 510],
		'9': [280, 480, 610]
		}
class Session(scene.Scene):
	def setup(self):
		self.background_color = '5300c0'
		self.player = 1
		self.p1moves = []
		self.p2moves = []
		self.win = False
		self.image = 'emj:Red_Ring'
		print(self.player)
		self.make_board()
	
	def make_board(self):
		for k, v in create_b.items():
			main_b = self.make_button(k, v[0], v[1], 'card:BackBlue1')
			main_b.action = self.button_tapped_game
			main_b.background_color = 'white'
			def anim_board():
				self.view.add_subview(main_b)
				main_b.x = v[2]		
			ui.animate(anim_board, duration =1, delay =1)
			
			
	def make_button(self, bname, bh, bw, bimage):
		a = ui.Button(name=bname)
		print(bname)
		a.frame = (bh, bw, 90, 90)
		a.flex = 'LRTB'
		a.border_width = 1
		a.corner_radius = 6
		a.background_image = ui.Image.named(bimage)
		return a
		
	
	def button_tapped_game(self, sender):
		self.sel_square(sender)
		sender.enabled = False
		win = self.check_winner()
		if not self.win:
			self.switch_player()
		else:
			self.add_restart_button()
			
			superv = self.get_butt_superview(sender)
			self.disable_buttons(superv)
			self.anim_win(win, superv)
			
	def add_restart_button(self):
			restart_b = self.make_button('restart', 10, 10,'typb:Back' )
			restart_b.background_color = 'white'
			restart_b.action = self.restart_game
			self.view.add_subview(restart_b)
			
	def get_butt_superview(self, sender):
		return sender.superview
	
	def disable_buttons(self, superv):	
		for v in superv.subviews:
			i = 1
			while i < 10:
				superv[str(i)].enabled = False
				i = i+1
		 
						
	def anim_win(self, winner, button):
		win = winner
		z = button																
		def small():
			for i in win:
				z[str(i)].transform = ui.Transform.scale(.95, .95)

				
		def norm():
			for i in win:
				z[str(i)].transform = ui.Transform.scale(1, 1)
				
		def anim_norm():
			ui.animate(norm ,duration=.3)		
				
		def anim_small():
			ui.animate(small,duration=.3,completion=anim_norm)
		
		def anim_big():
			for i in win:
				z[str(i)].background_color= 'yellow'
				z[str(i)].transform = ui.Transform.scale(1.05, 1.05)
			
		ui.animate(anim_big, duration=.3, completion=anim_small)

	def restart_game(self,sender):
		z = sender.superview
		for v in sender.superview.subviews:
			i = 1
			while i < 10:
				z[str(i)].alpha = 0.0
				z[str(i)].background_image = ui.Image.named('card:BackBlue1')
				z[str(i)].enabled = True
				z[str(i)].background_color= 'white'
				z[str(i)].alpha = 1
				i = i+1
			
		self.player = 1
		self.image = 'emj:Red_Ring'
		self.win = False
		self.p1moves = []
		self.p2moves = []
		

	
	def sel_square(self, sender):
		print(sender.name)
		print(sender)
		
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

