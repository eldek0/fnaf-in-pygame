import pygame
from pygame.locals import QUIT

import files.game.draw as dr
from files.import_imp import import_images
from files.animations.animations_init import animations_init
from files.game.game_objects import GameObjects
from files.game.game_controller import Game
from files.menu.menu import Menu
from files.save.save import save
from files.menu.warning_init import WarningInit
import include.pygame_shaders as pygame_shaders
from files.minigames.minigame import Minigame
from files.utils import get_shader_diff
from files.shaders.gameplay.vertex import vertex
from files.shaders.gameplay.fragment import fragment
from files.shaders.minigames.vertex import min_vertex
from files.shaders.minigames.fragment import min_fragment

default = (pygame_shaders.DEFAULT_VERTEX_SHADER, pygame_shaders.DEFAULT_FRAGMENT_SHADER)
gameplay = (vertex, fragment)
minigames = (min_vertex, min_fragment)

class App:
	def __init__(self, initial_dimentions=(1024, 768), caption="Five Nights at Freddy's 2 python edition"):
		self.playing = True
		self.loaded = False

		# Surface init
		pygame.init() # Starts the pygame timer
		pygame.mixer.init() # Init the mixer
		self.dimentions = initial_dimentions
		self.surface = pygame.display.set_mode( self.dimentions, vsync=True, flags= pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE | pygame.FULLSCREEN )
		pygame.display.set_caption(caption) # Win's name

		# Icon
		icon = pygame.image.load("icon.ico")
		pygame.display.set_icon(icon)

		# Shaders
		self.set_shaders()

		# Fps configurations
		self.clock = pygame.time.Clock()
		self.frames_per_second = 60

		self.warning_init = WarningInit(self)
		self.inital_warning = pygame.image.load("sprites/menu/logos/4.png").convert()
		
		self.update(self)
		
		self.assets = import_images()
		self.scene = 0

		# Game events
		self.ctrl_adv = False

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
		self.minigame:Minigame = None

		self.loaded = True

		self.debug = False # debugging the game

		if self.debug: print("Game on debug mode")

	def set_shaders(self):
		self.uiSurface = pygame.Surface(self.dimentions, pygame.SRCALPHA, 32)
		self.uiSurface.convert_alpha()

		self.minigamesSurface = pygame.Surface(self.dimentions, pygame.SRCALPHA, 32)
		self.minigamesSurface.convert_alpha()

		self.shaderMain = pygame_shaders.Shader(gameplay[0], gameplay[1], self.surface)
		self.uiShader = pygame_shaders.Shader(default[0], default[1], self.uiSurface)
		self.minigamesShader = pygame_shaders.Shader(minigames[0], minigames[1], self.minigamesSurface)

	def get_deltatime(self):
		self.deltaTime = self.clock.tick(self.frames_per_second) / 10.3

	def loop(self):
		while self.playing == True:
			
			events = pygame.event.get()

			# Update mouse's hitbox and pressed buttons
			diff = get_shader_diff(self.surface)
			p = pygame.mouse.get_pos()
			self.mouse_hitbox.left, self.mouse_hitbox.top = p
			self.mouse_hitbox.x -= p[0]*diff[0]
			self.mouse_hitbox.y -= p[1]*diff[1]

			# Frames per second
			self.game_fps = self.clock.tick(self.frames_per_second)

			if self.debug:
				pygame.display.set_caption(str(round(self.clock.get_fps(), 2)) ) # Win's name

			#DeltaTime
			self.get_deltatime()

			self.game_events(events)

			self.update(events)


	def quit_game(self):
		if self.warning_init.is_finished():
			save(self)
		self.playing = False

	def game_events(self, events):
		for event in events:
			if event.type == QUIT:
				self.quit_game()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_F11:
					pygame.display.toggle_fullscreen()

				if self.debug:
					if event.key == pygame.K_l:
						self.quit_game()
					
					elif event.key == pygame.K_m:
						self.minigame.startMinigame(self)

					elif event.key == pygame.K_g:
						if self.menu.inNight < 7: 
							self.menu.inNight += 1
						self.menu.init_menu_and_save_vars(self)
						self.menu.nightToPlay = self.menu.inNight
						self.menu.start_state = 7


					elif event.key == pygame.K_f:
						if self.menu.inNight > 1: 
							self.menu.inNight -= 1
						self.menu.init_menu_and_save_vars(self)
						self.menu.nightToPlay = self.menu.inNight
						self.menu.start_state = 7
					try:
						if event.key == pygame.K_r:
							if self.objects.gameTimer.times[0] == 12:
								self.objects.gameTimer.times[0] = 1
							else:
								self.objects.gameTimer.times[0] += 1

						elif event.key == pygame.K_e:
							if self.objects.gameTimer.times[0] == 1:
								self.objects.gameTimer.times[0] = 12
							else:
								self.objects.gameTimer.times[0] -= 1
					except Exception:
						pass
						
	def update(self, events):
		self.surface.fill((0,0,0, 0))
		self.uiSurface.fill((0, 0, 0, 0))
		#Draw on screen
		dr.Draw(self)

		if self.warning_init.is_finished():
			self.shaderMain.render_direct(pygame.Rect(0, 0, self.dimentions[0], self.dimentions[1]))

			if (self.minigame.isInMinigame()):
				self.minigamesShader.render_direct(pygame.Rect(0, 0, self.dimentions[0], self.dimentions[1]))

		# This surface will be responsable about the ui
		self.uiShader.render_direct(pygame.Rect(0, 0, self.dimentions[0], self.dimentions[1]))
	

		# Update each frame
		pygame.display.flip()

