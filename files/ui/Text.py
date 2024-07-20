import pygame
from pygame.locals import *

def Lock_to(lock:str, position:tuple, width:float, height:float, screen_areas:pygame.Rect):
	x = position[0]
	y = position[1]

	if lock == "x":
		return ( x + screen_areas.width/2 - width/2 , y)

	elif lock == "y":
		return (x, y + screen_areas.height/2 - height/2 )

	elif lock == "xy":
		return (x + screen_areas.width/2 - width/2, y + screen_areas.height/2 - height/2 )

	return 0

class Text:
	def __init__(self, App, txt:str, position:tuple, font:pygame.font.Font, color:tuple, lock:str=None, lock_surf=None):

		self.x = position[0]
		self.y = position[1]
		self.color = color
		self.font = font
		self.txt = txt

		self.update_text()

		self.w = self.Text.get_rect().width
		self.h = self.Text.get_rect().height
		self.Lock_formula = (0,0)

		if not lock_surf: lock_surf = App.surface.get_rect()

		if not lock == None:
			self.Lock_formula = Lock_to(lock, (self.x, self.y), self.w, self.h, lock_surf )

	def update_text(self):
		self.Text = self.font.render(self.txt,1,(self.color))

	def draw(self, surface:pygame.surface.Surface):
		surface.blit(self.Text,(self.Lock_formula[0] + self.x,self.Lock_formula[1] + self.y))

	def getHitbox(self):
		return pygame.Rect(self.Lock_formula[0] + self.x, self.Lock_formula[1] + self.y, self.w, self.h)

	def getWidth(self):
		return self.w

	def setCoords(self, x, y):
		self.x = x
		self.y = y

	def underline(self, state:bool):
		self.font.set_underline(state)