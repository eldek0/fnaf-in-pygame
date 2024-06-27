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
from files.menu.warning_init import WarningInit
import include.pygame_shaders as pygame_shaders

default = (pygame_shaders.DEFAULT_VERTEX_SHADER, pygame_shaders.DEFAULT_FRAGMENT_SHADER)
gameplay = ("files/shaders/gameplay/vertex.glsl", "files/shaders/gameplay/fragment.glsl")
sepia = (pygame_shaders.DEFAULT_VERTEX_SHADER, "files/shaders/sepia/fragment.glsl")

class App:
	def __init__(self, initial_dimentions=(1024, 768), caption="Five Nights at Freddy's - made with pygame"):
		self.playing = True
		self.loaded = False

		# Surface init
		pygame.init() # Starts the pygame timer
		pygame.mixer.init() # Init the mixer
		self.dimentions = initial_dimentions
		self.surface = pygame.display.set_mode( self.dimentions, vsync=True, flags= pygame.OPENGL | pygame.DOUBLEBUF )
		pygame.display.set_caption(caption) # Win's name

		# Shaders
		self.set_shaders()

		# Icon
		icon = pygame.image.load("icon.ico")
		pygame.display.set_icon(icon)

		# Fps configurations
		self.clock = pygame.time.Clock()
		self.frames_per_second = 60

		self.warning_init = WarningInit(self)
		self.inital_warning = pygame.image.load("sprites/menu/logos/4.png").convert()
		self.update(self)
		
		self.assets = import_images()
		self.scene = 0
		# Mouse
		self.mouse_hitbox = pygame.Rect((self.dimentions[0]/2,self.dimentions[1]/2), (1,1))

		# DeltaTime variables
		self.prev_time, self.now_time = 0, 0

		# Animations
		self.animations = animations_init(self)

		# Menu will be initialized in draw, and game / gameObjects in menu
		self.objects:GameObjects = None
		self.game:Game = None
		self.menu:Menu = None

		self.loaded = True

		self.debug = True # debugging the game

	def set_shaders(self):
		self.uiSurface = pygame.Surface(self.dimentions, pygame.SRCALPHA, 32)
		self.uiSurface.convert_alpha()

		self.shaderMain = pygame_shaders.Shader(gameplay[0], gameplay[1], self.surface)
		self.uiShader = pygame_shaders.Shader(default[0], default[1], self.uiSurface)

	def get_deltatime(self):
		self.deltaTime = self.clock.tick(self.frames_per_second) / 10.3

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
				if self.warning_init.is_finished():
					save(self)
				self.playing = False
				
	def update(self, events):
		self.surface.fill((0,0,0))
		self.uiSurface.fill((0, 0, 0, 0))

		#Draw on screen
		dr.Draw(self)

		self.shaderMain.render_direct(pygame.Rect(0, 0, self.dimentions[0], self.dimentions[1]))

		# This surface will be responsable about the ui
		self.uiShader.render_direct(pygame.Rect(0, 0, self.dimentions[0], self.dimentions[1]))
		

		# Update each frame
		pygame.display.flip()

