
import pygame as pg
from .. import tools

class Menu(tools.States):
	def __init__(self, screenrect):
		tools.States.__init__(self)
		self.screenrect = screenrect
		
	def get_event(self, event, keys):
		if event.type == pg.QUIT:
			self.quit = True
	
	def update(self, now, keys):
		pass
		
	def render(self, screen):
		screen.fill((0,0,0))
			
	def cleanup(self):
		pass
		
	def entry(self):
		pass
