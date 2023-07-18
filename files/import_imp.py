import pygame
from pygame.locals import *

class import_images:

	def __init__(self):
		import_images.images(self)
		
		import_images.audios(self)

		import_images.fonts(self)

		print("Assets loaded!")

	def cropped_images(self):
		pass

	def images(self):
		# -- Monitor --
		# Animation
		self.camera_sprites = []
		
		for i in range(11):
			self.camera_sprites.append(
				pygame.image.load(f"sprites/monitor/{i+1}.png").convert_alpha()
			)
		# Button
		self.monitor_button = pygame.image.load("sprites/monitor/button.png").convert_alpha()

		# -- Office --
		# Normal office
		self.office1 = pygame.image.load("sprites/office/office.png").convert()

		# Offices with animatrionics
		self.animatrionic_offices = []
		for i in range(3):
			self.animatrionic_offices.append(
				pygame.image.load(f"sprites/office/inside/{i}.png").convert()
			)
		print(len(self.animatrionic_offices))

		#  -- Flash hallway offices --
		self.flash_offices = []
		for i in range(11):
			self.flash_offices.append(
				pygame.image.load(f"sprites/office/hallway/{i}.png").convert()
			)

		# Right vent office
		self.right_vent_offices = []
		for i in range(3):
			self.right_vent_offices.append(
				pygame.image.load(f"sprites/office/right_vents/{i}.png").convert()
			)

		# Left vent office
		self.left_vent_offices = []
		for i in range(3):
			self.left_vent_offices.append(
				pygame.image.load(f"sprites/office/left_vents/{i}.png").convert()
			)

		# Desk animation
		self.desk_animation = []
		for i in range(3):
			self.desk_animation.append(
				pygame.image.load(f"sprites/office/utils/{10 + i}.png").convert_alpha()
			)

		# -- Mask --
		# Animation
		self.mask_sprites = []
		for i in range(10):
			self.mask_sprites.append(
				pygame.image.load(f"sprites/mask/{i+1}.png").convert_alpha()
			)

		# Button
		self.mask_button = pygame.image.load("sprites/mask/button.png").convert_alpha()

		# -- Vents --
		self.right_vent_button_off, self.right_vent_button_on = pygame.image.load("sprites/office/utils/3.png").convert_alpha(), pygame.image.load("sprites/office/utils/4.png").convert_alpha()

		self.left_vent_button_off, self.left_vent_button_on = pygame.image.load("sprites/office/utils/1.png").convert_alpha(), pygame.image.load("sprites/office/utils/2.png").convert_alpha()

		# -- Cameras --
		self.camera_map = pygame.image.load("sprites/cameras/utils/Map.png").convert_alpha()
		self.camera_borderline = pygame.image.load("sprites/cameras/utils/Border.png").convert_alpha()

		# Camera room buttons and labels

		self.room_button_unselected, self.room_button_selected = pygame.image.load("sprites/cameras/Labels/13.png").convert(), pygame.image.load("sprites/cameras/Labels/14.png").convert()

		self.room_buttons_labels = []
		for i in range(12):
			self.room_buttons_labels.append(
				pygame.image.load(f"sprites/cameras/Labels/{i+1}.png").convert_alpha()
			)

		# -- Party Room 1 --
		self.party_room_1_cameras = []
		for i in range(4):
			self.party_room_1_cameras.append(
				pygame.image.load(f"sprites/cameras/locations/PartyRoom1/{i}.png").convert()
			)

		self.party_room_1_label = pygame.image.load(f"sprites/cameras/locations/PartyRoom1/label.png").convert_alpha()

		# -- Party Room 2 --
		self.party_room_2_cameras = []
		for i in range(5):
			self.party_room_2_cameras.append(
				pygame.image.load(f"sprites/cameras/locations/PartyRoom2/{i}.png").convert()
			)

		self.party_room_2_label = pygame.image.load(f"sprites/cameras/locations/PartyRoom2/label.png").convert_alpha()

		# -- Party Room 3 --
		self.party_room_3_cameras = []
		for i in range(5):
			self.party_room_3_cameras.append(
				pygame.image.load(f"sprites/cameras/locations/PartyRoom3/{i}.png").convert()
			)

		self.party_room_3_label = pygame.image.load(f"sprites/cameras/locations/PartyRoom3/label.png").convert_alpha()

		# -- Party Room 4 --
		self.party_room_4_cameras = []
		for i in range(7):
			self.party_room_4_cameras.append(
				pygame.image.load(f"sprites/cameras/locations/PartyRoom4/{i}.png").convert()
			)

		self.party_room_4_label = pygame.image.load(f"sprites/cameras/locations/PartyRoom4/label.png").convert_alpha()

		# -- Prize Corner --
		self.prize_corner_cameras = []
		for i in range(6):
			self.prize_corner_cameras.append(
				pygame.image.load(f"sprites/cameras/locations/PrizeCorner/{i}.png").convert()
			)

		self.prize_corner_label = pygame.image.load(f"sprites/cameras/locations/PrizeCorner/label.png").convert_alpha()

		# -- Right Air Vent --
		self.right_air_vent_cameras = []
		for i in range(5):
			self.right_air_vent_cameras.append(
				pygame.image.load(f"sprites/cameras/locations/RightAirVent/{i}.png").convert()
			)

		self.right_air_vent_label = pygame.image.load(f"sprites/cameras/locations/RightAirVent/label.png").convert_alpha()

		# -- Left Air Vent --
		self.left_air_vent_cameras = []
		for i in range(6):
			self.left_air_vent_cameras.append(
				pygame.image.load(f"sprites/cameras/locations/LeftAirVent/{i}.png").convert()
			)

		self.left_air_vent_label = pygame.image.load(f"sprites/cameras/locations/LeftAirVent/label.png").convert_alpha()

		# -- Game Area --
		self.game_area_cameras = []
		for i in range(6):
			self.game_area_cameras.append(
				pygame.image.load(f"sprites/cameras/locations/GameArea/{i}.png").convert()
			)

		self.game_area_label = pygame.image.load(f"sprites/cameras/locations/GameArea/label.png").convert_alpha()

		# -- KidsCove --
		self.kids_cove_cameras = []
		for i in range(3):
			self.kids_cove_cameras.append(
				pygame.image.load(f"sprites/cameras/locations/KidsCove/{i}.png").convert()
			)

		self.kids_cove_label = pygame.image.load(f"sprites/cameras/locations/KidsCove/label.png").convert_alpha()

		# -- Parts n Service --
		self.partsnservice_cameras = []
		for i in range(7):
			self.partsnservice_cameras.append(
				pygame.image.load(f"sprites/cameras/locations/PartsnService/{i}.png").convert()
			)

		self.parts_n_service_label = pygame.image.load(f"sprites/cameras/locations/PartsnService/label.png").convert_alpha()

		# Show Stage
		self.show_stage_cameras = []
		for i in range(7):
			self.show_stage_cameras.append(
				pygame.image.load(f"sprites/cameras/locations/ShowStage/{i}.png").convert()
			)

		self.show_stage_label = pygame.image.load(f"sprites/cameras/locations/ShowStage/label.png").convert_alpha()

		# Main Hall
		self.main_hall_cameras = []
		for i in range(6):
			self.main_hall_cameras.append(
				pygame.image.load(f"sprites/cameras/locations/MainHall/{i}.png").convert()
			)

		self.main_hall_label = pygame.image.load(f"sprites/cameras/locations/MainHall/label.png").convert_alpha()


		# -- Static
		self.static_1 = []
		for i in range(6):
			self.static_1.append(
				pygame.image.load(f"sprites/cameras/static/{i+1}.png").convert()
			)

		self.static_2 = []
		for i in range(4):
			self.static_2.append(
				pygame.image.load(f"sprites/cameras/static/{i+10}.png").convert_alpha()
			)

		self.music_box_button_off = pygame.image.load(f"sprites/cameras/Labels/16.png").convert()
		self.music_box_button_on = pygame.image.load(f"sprites/cameras/Labels/17.png").convert()
		self.music_box_label = pygame.image.load(f"sprites/cameras/Labels/15.png").convert_alpha()

		# Music box timer sprites
		self.music_box_timer_sprites = []
		for i in range(21):
			self.music_box_timer_sprites.append(
				pygame.image.load(f"sprites/cameras/music_box_timer/{i+1}.png").convert_alpha()
			)

		# -- Bunny in office --
		self.office_bunny = pygame.image.load(f"sprites/office/inside/3.png").convert_alpha()
		self.office_bunny = pygame.transform.scale(self.office_bunny, (self.office_bunny.get_width() * 0.87, self.office_bunny.get_height() * 0.87))

		# Battery
		self.battery_stages = []
		for i in range(5):
			self.battery_stages.append(
				pygame.image.load(f"sprites/battery/{i}.png").convert_alpha()
			)
		self.flashlight_label = pygame.image.load(f"sprites/battery/label.png").convert_alpha()

		# -- Jumpscares Animation -- 
		# Puppet jumpscare animation
		self.puppet_screamer_animation = []
		for i in range(15):
			self.puppet_screamer_animation.append(
				pygame.image.load(f"sprites/jumpscares/puppet/{i+1}.png").convert_alpha()
			)

		# Toy bunny jumpscare animation
		self.toy_bunny_screamer_animation = []
		for i in range(13):
			self.toy_bunny_screamer_animation.append(
				pygame.image.load(f"sprites/jumpscares/toy_bonnie/{i+1}.png").convert_alpha()
			)

		# Toy chica jumpscare animation
		self.toy_chica_screamer_animation = []
		for i in range(13):
			self.toy_chica_screamer_animation.append(
				pygame.image.load(f"sprites/jumpscares/toy_chica/{i+1}.png").convert_alpha()
			)

		# Get crops from cropped images
		import_images.cropped_images(self)
		
				
	def audios(self):
		self.error_sound = pygame.mixer.Sound("sounds/error.wav")

		self.buzzlight = pygame.mixer.Sound("sounds/buzzlight.wav")

		self.mask_on_sound = pygame.mixer.Sound("sounds/mask_on.wav")
		self.mask_off_sound = pygame.mixer.Sound("sounds/mask_off.wav") 

		self.camera_sound_1 = pygame.mixer.Sound("sounds/blip3.wav")
		self.camera_sound_2 = pygame.mixer.Sound("sounds/computer_digital.wav")

		self.background_music = pygame.mixer.music.load("sounds/In_The_Depths.wav")

		self.fan_sound = pygame.mixer.Sound("sounds/fansound.wav")

		self.music_box = pygame.mixer.Sound("sounds/Music_Box_Melody_Playful.wav")

		self.charge = pygame.mixer.Sound("sounds/windup2.wav")

		self.mask_breathing = pygame.mixer.Sound("sounds/deepbreaths.wav")

		self.times_out = pygame.mixer.Sound("sounds/jackinthebox.wav")

		self.stare = pygame.mixer.Sound("sounds/stare.wav")

	def fonts(self):
		self.Arial = "fonts/arial.ttf"

		# get font types
		self.font_types()

	def font_types(self):
		self.Arial60 = pygame.font.Font(self.Arial, 60)
		self.Arial30 = pygame.font.Font(self.Arial, 30)