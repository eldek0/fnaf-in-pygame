import pygame
import time
from pygame.locals import QUIT

import files.draw as dr
from files.import_imp import import_images
from files.animations.animations_init import animations_init
from files.game_objects import GameObjects


class App:
	def __init__(self, initial_dimentions=(1024, 768), caption="Five Nights at Freddy's - made with pygame"):
		self.playing = True

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

		# Game animations
		self.animations = animations_init(self)

		# Game object initialize
		self.objects = GameObjects(self)

		self.gameOver = False

		pygame.mixer.music.set_volume(0.5)
		pygame.mixer.music.play(-1)
		pygame.mixer.Channel(1).set_volume(0.8)
		pygame.mixer.Channel(2).set_volume(0) # Music box
		pygame.mixer.Channel(3).set_volume(1) # Sounds effects
		pygame.mixer.Channel(4).set_volume(1) # Mask breathing
		pygame.mixer.Channel(5).set_volume(1) # Stare at an animatrionic
		pygame.mixer.Channel(6).set_volume(1) # Mangle noise
		pygame.mixer.Channel(7).set_volume(1) # Baloon boy laugh

		self.TIME_PLAYING = pygame.time.get_ticks()
		self.ambiance_sound = pygame.time.get_ticks()

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
				self.playing = False
				
	def update(self, events):
		self.surface.fill((105,105,105))

		# Draw on screen
		dr.Draw(self)

		# Update each frame
		pygame.display.update()

