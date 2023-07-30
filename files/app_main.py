import pygame
import time
from pygame.locals import QUIT

import files.game.draw as dr
from files.import_imp import import_images
from files.animations.animations_init import animations_init
from files.game.game_objects import GameObjects
from files.game.game_controller import Game
from files.menu.menu import Menu
from files.save.save import save, read


class App:
	def __init__(self, initial_dimentions=(1024, 768), caption="Five Nights at Freddy's - made with pygame"):
		self.playing = True

		#data = read(self)
		data = None

		# Surface init
		pygame.init() # Starts the pygame timer
		pygame.mixer.init() # Init the mixer
		self.dimentions = initial_dimentions
		self.surface = pygame.display.set_mode( self.dimentions ,vsync=True )
		pygame.display.set_caption(caption) # Win's name

		# Fps configurations
		self.clock = pygame.time.Clock()
		self.frames_per_second = 60

		self.assets = import_images()
		self.scene = 0
		# Mouse
		self.mouse_hitbox = pygame.Rect((0,0), (1,1))

		# DeltaTime variables
		self.prev_time, self.now_time = 0, 0

		# Animations
		self.animations = animations_init(self)

		# Will be initialized in menu
		self.objects:GameObjects = None
		self.game:Game = None

		self.menu = Menu(self)

		if data:
			self.menu.inNight = data["Night"]
			self.menu.played_once = data["Played"]
			self.menu.custom_night_menu.completed_nights = data["Custom"]

	def get_deltatime(self):
		self.now_time = time.time()
		self.deltaTime = self.now_time - self.prev_time
		self.prev_time = self.now_time

	def loop(self):
		while self.playing == True:
			
			events = pygame.event.get()

			# Update mouse's hitbox and pressed buttons
			self.mouse_hitbox.left, self.mouse_hitbox.top = pygame.mouse.get_pos()

			# Frames per second
			self.game_fps = self.clock.tick(self.frames_per_second)

			#pygame.display.set_caption(str(round(self.clock.get_fps(), 2)) ) # Win's name

			#DeltaTime
			self.get_deltatime()

			self.game_events(events)

			self.update(events)

	def game_events(self, events):
		for event in events:
			if event.type == QUIT:
				save(self)
				self.playing = False
				
	def update(self, events):
		self.surface.fill((0,0,0))

		# Draw on screen
		dr.Draw(self)

		# Update each frame
		pygame.display.update()

