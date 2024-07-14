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
		# Add toy freddy 
		self.animatrionic_offices.append(
			pygame.image.load(f"sprites/office/inside/4.png").convert()
			)

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
		for i in range(4):
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
		self.camera_record_sprite = pygame.image.load("sprites/cameras/utils/1.png").convert_alpha()
		self.camera_signal_interrupted = pygame.image.load("sprites/cameras/utils/2.png").convert_alpha()
		# Camera room buttons and labels

		self.room_button_unselected, self.room_button_selected = pygame.image.load("sprites/cameras/Labels/13.png").convert(), pygame.image.load("sprites/cameras/Labels/14.png").convert()
		self.clicknhold = pygame.image.load(f"sprites/cameras/labels/18.png").convert_alpha()

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

		# -- Golden Freddy in office --
		self.office_golden_freddy = pygame.image.load(f"sprites/office/inside/6.png").convert_alpha()

		# Battery
		self.battery_stages = []
		for i in range(5):
			self.battery_stages.append(
				pygame.image.load(f"sprites/battery/{i}.png").convert_alpha()
			)
		self.flashlight_label = pygame.image.load(f"sprites/battery/label.png").convert_alpha()

		# Mangle cameras position
		self.mangle_cameras = []
		for i in range(4):
			self.mangle_cameras.append(
				pygame.image.load(f"sprites/cameras/mangle/{i}.png").convert_alpha()
			)

		# Mangle in office
		self.office_mangle = pygame.image.load(f"sprites/office/inside/7.png").convert_alpha()

		# Baloon boy in office
		self.office_baloon_boy = pygame.image.load(f"sprites/office/inside/5.png").convert_alpha()
		
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

		# Toy freddy jumpscare animation
		self.toy_freddy_screamer_animation = []
		for i in range(12):
			self.toy_freddy_screamer_animation.append(
				pygame.image.load(f"sprites/jumpscares/toy_freddy/{i+1}.png").convert_alpha()
			)

		# Withered freddy jumpscare animation
		self.withered_freddy_screamer_animation = []
		for i in range(13):
			self.withered_freddy_screamer_animation.append(
				pygame.image.load(f"sprites/jumpscares/withered_freddy/{i+1}.png").convert_alpha()
			)
		for i in range(3):
			self.withered_freddy_screamer_animation.append(
				pygame.image.load(f"sprites/jumpscares/withered_freddy/{i+7}.png").convert_alpha()
			)


		# Withered bonnie jumpscare animation
		self.withered_bonnie_screamer_animation = []
		for i in range(16):
			self.withered_bonnie_screamer_animation.append(
				pygame.image.load(f"sprites/jumpscares/withered_bonnie/{i+1}.png").convert_alpha()
			)

		# Withered chica jumpscare animation
		self.withered_chica_screamer_animation = []
		for i in range(12):
			self.withered_chica_screamer_animation.append(
				pygame.image.load(f"sprites/jumpscares/withered_chica/{i+1}.png").convert_alpha()
			)

		# Foxy jumpscare animation
		self.foxy_screamer_animation = []
		for i in range(14):
			self.foxy_screamer_animation.append(
				pygame.image.load(f"sprites/jumpscares/withered_foxy/{i+1}.png").convert_alpha()
			)

		# Mangle jumpscare animation
		self.mangle_screamer_animation = []
		for i in range(16):
			self.mangle_screamer_animation.append(
				pygame.image.load(f"sprites/jumpscares/mangle/{i+1}.png").convert_alpha()
			)

		# Golden Freddy jumpscare animation
		self.golden_freddy_animation = []
		for i in range(13):
			self.golden_freddy_animation.append(
				pygame.image.load(f"sprites/jumpscares/withered_golden_freddy/{i+1}.png").convert_alpha()
			)
		
		# -- MENU UTILITIES -- 
		self.background_menu = []
		for i in range(4):
			self.background_menu.append(
				pygame.image.load(f"sprites/menu/misc/{i}.png").convert()
			)

		# Labels
		self.fnaf_title = pygame.image.load("sprites/menu/logos/2.png").convert()
		self.fnaf_title.set_colorkey((0, 0, 0))
		
		self.scott_credits = pygame.image.load("sprites/menu/logos/1.png").convert()
		self.scott_credits.set_colorkey((0, 0, 0))
		self.sel_scott_credits = pygame.image.load("sprites/menu/logos/10.png").convert()
		self.sel_scott_credits.set_colorkey((0, 0, 0))

		self.option_selected = pygame.image.load("sprites/menu/logos/3.png").convert()
		self.option_selected.set_colorkey((0, 0, 0))
		self.new_game_option = pygame.image.load("sprites/menu/logos/5.png").convert()
		self.new_game_option.set_colorkey((0, 0, 0))
		self.continue_option = pygame.image.load("sprites/menu/logos/6.png").convert()
		self.continue_option.set_colorkey((0, 0, 0))
		self.night_six_option = pygame.image.load("sprites/menu/nights/12.png").convert()
		self.night_six_option.set_colorkey((0, 0, 0))
		self.custom_night_option = pygame.image.load("sprites/menu/nights/13.png").convert()
		self.custom_night_option.set_colorkey((0, 0, 0))
		self.star = pygame.image.load("sprites/menu/misc/4.png").convert_alpha()
		self.delete_data_label = pygame.image.load("sprites/menu/logos/7.png").convert()
		self.delete_data_label.set_colorkey((0, 0, 0))
		self.version = pygame.image.load("sprites/menu/logos/9.png").convert_alpha()

		self.newspaper = pygame.image.load("sprites/menu/paychecks/1.png").convert()
		self.loading_icon = pygame.image.load("sprites/menu/logos/0.png").convert()

		self.night_five_paycheck = pygame.image.load("sprites/menu/paychecks/2.png").convert()
		self.night_six_paycheck = pygame.image.load("sprites/menu/paychecks/3.png").convert()
		self.night_seven_paycheck = pygame.image.load("sprites/menu/paychecks/4.png").convert()

		self.nights_12am = []
		for i in range(7):
			self.nights_12am.append(
				pygame.image.load(f"sprites/menu/nights/{i+1}.png").convert_alpha()
			)
		
		# Confetti
		self.blue_conf = []
		for i in range(0, 5):
			self.blue_conf.append(
				pygame.image.load(f"sprites/menu/sprinkles/{i}.png").convert_alpha()
			)

		self.green_conf = []
		for i in range(10, 15):
			self.green_conf.append(
				pygame.image.load(f"sprites/menu/sprinkles/{i}.png").convert_alpha()
			)

		self.yellow_conf = []
		for i in range(20, 25):
			self.yellow_conf.append(
				pygame.image.load(f"sprites/menu/sprinkles/{i}.png").convert_alpha()
			)

		self.pink_conf = []
		for i in range(30, 35):
			self.pink_conf.append(
				pygame.image.load(f"sprites/menu/sprinkles/{i}.png").convert_alpha()
			)
		
		# Numbers 
		self.numbers = []
		for i in range(10):
			self.numbers.append(
				pygame.image.load(f"sprites/numbers/1rst/medium/{i}.png").convert_alpha()
			)

		self.numbers_small = []
		for i in range(10):
			self.numbers_small.append(
				pygame.image.load(f"sprites/numbers/1rst/small/{i}.png").convert_alpha()
			)

		self.numbers_big = []
		for i in range(10):
			img = pygame.image.load(f"sprites/numbers/1rst/big/{i}.png").convert()
			img.set_colorkey((0, 0, 0))
			self.numbers_big.append(img)

		
		self.numbers2 = []
		for i in range(10):
			self.numbers2.append(
				pygame.image.load(f"sprites/numbers/2nd/medium/{i}.png").convert_alpha()
			)

		self.numbers2_small = []
		for i in range(10):
			self.numbers2_small.append(
				pygame.image.load(f"sprites/numbers/2nd/small/{i}.png").convert_alpha()
			)

		self.night_label = pygame.image.load(f"sprites/clock/20.png").convert_alpha()
		self.am_label = pygame.image.load(f"sprites/clock/2.png").convert_alpha()

		# 5 am to 6 am animation
		self.five_animation = []
		for i in range(3, 8):
			self.five_animation.append(
				pygame.image.load(f"sprites/clock/{i}.png").convert_alpha()
			)

		self.six_animation = []
		for i in range(8, 14):
			self.six_animation.append(
				pygame.image.load(f"sprites/clock/{i}.png").convert_alpha()
			)

		self.big_am = pygame.image.load(f"sprites/clock/1.png").convert_alpha()

		# Telephone mute
		self.telephone_mute = pygame.image.load(f"sprites/office/utils/20.png").convert_alpha()

		self.lost_screen = pygame.image.load(f"sprites/menu/nights/10.png").convert()
		self.game_over = pygame.image.load(f"sprites/menu/nights/11.png").convert_alpha()
		
		self.static_stripes = []
		for i in range(5):
			self.static_stripes.append(
				pygame.image.load(f"sprites/cameras/static/s2/{i+1}.png").convert_alpha()
			)
		
		self.warn_big = []
		for i in range(24,26):
			self.warn_big.append(
				pygame.image.load(f"sprites/office/utils/{i}.png").convert_alpha()
			)

		self.warn_small = []
		for i in range(30,32):
			self.warn_small.append(
				pygame.image.load(f"sprites/office/utils/{i}.png").convert_alpha()
			)

		self.night_label_2 = pygame.image.load("sprites/menu/logos/8.png").convert_alpha()

		# CUSTOM NIGHT
		# Animatrionics icons and labels
		self.animatrionic_icons = []
		for i in range(10):
			self.animatrionic_icons.append(
				pygame.image.load(f"sprites/custom_night/icons/{i+1}.png").convert()
			)

		self.animatrionic_labels = []
		for i in range(10):
			self.animatrionic_labels.append(
				pygame.image.load(f"sprites/custom_night/names/{i+1}.png").convert()
			)

		self.custom_night_title = pygame.image.load(f"sprites/custom_night/labels/1.png").convert()
		self.arrow_right = pygame.image.load(f"sprites/custom_night/labels/2.png").convert()
		self.arrow_left = pygame.image.load(f"sprites/custom_night/labels/3.png").convert()
		self.ready_button = pygame.image.load(f"sprites/custom_night/labels/4.png").convert()

		self.arrow_right2 = pygame.image.load(f"sprites/custom_night/labels/5.png").convert()
		self.arrow_left2 = pygame.image.load(f"sprites/custom_night/labels/6.png").convert()

		self.custom_night_level_info = pygame.image.load(f"sprites/custom_night/labels/7.png").convert()

		# Modes
		self.modes_labels = []
		for i in range(10):
			self.modes_labels.append(
				pygame.image.load(f"sprites/custom_night/modes/{i+1}.png").convert()
			)

		# Rewards
		self.custom_night_rewards = []
		for i in range(9):
			self.custom_night_rewards.append(
				pygame.image.load(f"sprites/custom_night/rewards/{i}.png").convert_alpha()
			)

		# -- CUTSCENES --
		self.cutscene_chica = []
		for i in range(10, 13):
			self.cutscene_chica.append(
				pygame.image.load(f"sprites/cutscenes/{i}.png").convert_alpha()
			)

		self.cutscene_bonnie = []
		for i in range(20, 23):
			self.cutscene_bonnie.append(
				pygame.image.load(f"sprites/cutscenes/{i}.png").convert_alpha()
			)

		self.cutscene_freddy = pygame.image.load(f"sprites/cutscenes/30.png").convert_alpha()

		self.cutscene_puppet = pygame.image.load(f"sprites/cutscenes/40.png").convert_alpha()

		self.cutscene_background = pygame.image.load(f"sprites/cutscenes/1.png").convert()
		self.cutscene_black = pygame.image.load(f"sprites/cutscenes/0.png").convert()
		self.cutscene_mask = pygame.image.load(f"sprites/cutscenes/2.png").convert_alpha()
		self.err_img = pygame.image.load(f"sprites/cutscenes/3.png").convert()
		self.its_me = pygame.image.load(f"sprites/cutscenes/4.png").convert()
		
		# Minigames

		# Give gifts, Give life
		self.puppet_minigame = pygame.image.load("sprites/minigames/GG_GL/4.png").convert_alpha()

		self.soul = pygame.image.load("sprites/minigames/GG_GL/7.png").convert()
		self.soul.set_colorkey((0, 0, 0))

		self.gift = pygame.image.load("sprites/minigames/GG_GL/6.png").convert_alpha()

		self.give_gifts = pygame.image.load("sprites/minigames/GG_GL/10.png").convert_alpha()

		self.give_life = pygame.image.load("sprites/minigames/GG_GL/11.png").convert_alpha()

		self.chica_mask = pygame.image.load("sprites/minigames/GG_GL/0.png").convert_alpha()

		self.fred_mask = pygame.image.load("sprites/minigames/GG_GL/1.png").convert_alpha()

		self.bonnie_mask = pygame.image.load("sprites/minigames/GG_GL/2.png").convert_alpha()

		self.foxy_mask = pygame.image.load("sprites/minigames/GG_GL/3.png").convert_alpha()

		# SAVE THEM

		self.freddy_walking = []
		for i in range(6):
			self.freddy_walking.append(
				pygame.image.load(f"sprites/minigames/SAVE THEM/{i}.png").convert_alpha()
			)

		
		self.table = pygame.image.load(f"sprites/minigames/SAVE THEM/10.png").convert()
		self.table.set_colorkey((0, 0, 0))

		self.floor1 = pygame.image.load(f"sprites/minigames/SAVE THEM/14.png").convert()
		self.floor2 = pygame.image.load(f"sprites/minigames/SAVE THEM/15.png").convert()

		
		self.sad_soul = pygame.image.load(f"sprites/minigames/SAVE THEM/27.png").convert()
		self.sad_soul.set_colorkey((0, 0, 0))

		self.suit_gr_1 = pygame.image.load(f"sprites/minigames/SAVE THEM/23.png").convert()
		self.suit_gr_1.set_colorkey((0, 0, 0))

		self.suit_gr_2 = pygame.image.load(f"sprites/minigames/SAVE THEM/24.png").convert()
		self.suit_gr_2.set_colorkey((0, 0, 0))

		self.suit1 = pygame.image.load(f"sprites/minigames/SAVE THEM/20.png").convert()
		self.suit1.set_colorkey((0, 0, 0))

		self.suit2 = pygame.image.load(f"sprites/minigames/SAVE THEM/21.png").convert()
		self.suit2.set_colorkey((0, 0, 0))

		self.suit3 = pygame.image.load(f"sprites/minigames/SAVE THEM/22.png").convert()
		self.suit3.set_colorkey((0, 0, 0))

		self.dust = pygame.image.load(f"sprites/minigames/SAVE THEM/13.png").convert()
		self.dust.set_colorkey((0, 0, 0))

		self.blood = pygame.image.load(f"sprites/minigames/SAVE THEM/31.png").convert()
		self.blood.set_colorkey((0, 0, 0))

		self.bigGift = pygame.image.load(f"sprites/minigames/SAVE THEM/30.png").convert()
		self.bigGift.set_colorkey((0, 0, 0))

		self.endo_anim = []
		for i in range(2):
			img = pygame.image.load(f"sprites/minigames/SAVE THEM/{25 + i}.png").convert()
			img.set_colorkey((0, 0, 0))
			self.endo_anim.append(img)

		self.dust.set_colorkey((0, 0, 0))

		self.sceneary = pygame.image.load(f"sprites/minigames/SAVE THEM/12.png").convert()
		self.sceneary.set_colorkey((0, 0, 0))

		self.desk_min = pygame.image.load(f"sprites/minigames/SAVE THEM/11.png").convert()
		self.desk_min.set_colorkey((0, 0, 0))

		# Get crops from cropped images
		import_images.cropped_images(self)
		
				
	def audios(self):
		self.error_sound = pygame.mixer.Sound("sounds/error.wav")

		self.buzzlight = pygame.mixer.Sound("sounds/buzzlight.wav")

		self.mask_on_sound = pygame.mixer.Sound("sounds/mask_on.wav")
		self.mask_off_sound = pygame.mixer.Sound("sounds/mask_off.wav") 

		self.blip1 = pygame.mixer.Sound("sounds/blip3.wav")
		self.camera_sound_1 = pygame.mixer.Sound("sounds/cam_in.wav")
		self.camera_sound_2 = pygame.mixer.Sound("sounds/cam_out.wav")

		self.background_music = "sounds/In_The_Depths.wav"
		
		self.background_music_menu = "sounds/The_Sand_Temple_Loop_G.wav"

		self.fan_sound = pygame.mixer.Sound("sounds/fansound.wav")

		self.music_box = pygame.mixer.Sound("sounds/Music_Box_Melody_Playful.wav")

		self.charge = pygame.mixer.Sound("sounds/windup2.wav")

		self.mask_breathing = pygame.mixer.Sound("sounds/deepbreaths.wav")

		self.times_out = pygame.mixer.Sound("sounds/jackinthebox.wav")

		self.stare = pygame.mixer.Sound("sounds/stare.wav")

		self.boop = pygame.mixer.Sound("sounds/PartyFavorraspyPart_AC01__3.wav")

		self.xScream1 = pygame.mixer.Sound("sounds/Xscream2.wav")

		self.mangle_noise = pygame.mixer.Sound("sounds/elec_garble.wav")

		self.baloon_laugh = pygame.mixer.Sound("sounds/echo3.wav")

		self.scary_ambiance = pygame.mixer.Sound("sounds/ScaryAmbiance.wav")

		self.clock_chimes = pygame.mixer.Sound("sounds/Clocks_Chimes.wav")

		self.joy_sound = pygame.mixer.Sound("sounds/yay.wav")

		self.menu_static_1 = pygame.mixer.Sound("sounds/static2_1.wav")

		self.menu_static_2 = pygame.mixer.Sound("sounds/static2_2.wav")

		self.game_lost_static = pygame.mixer.Sound("sounds/gameOver.wav")

		self.music_box2 = pygame.mixer.Sound("sounds/musicbox2.wav")

		self.coin_sound = pygame.mixer.Sound("sounds/coin.wav")

		self.cake_sound = pygame.mixer.Sound("sounds/cake2.wav")


		self.vents_sounds = pygame.mixer.Sound("sounds/ventwalk1.wav")

		self.walk_sounds = []
		for i in range(5):
			self.walk_sounds.append(
				pygame.mixer.Sound(f"sounds/walk{i+1}.wav")
			)
		for i in range(3):
			self.walk_sounds.append(
				pygame.mixer.Sound(f"sounds/metalwalk{i+1}.wav")
			)

		self.metal_run_sound = pygame.mixer.Sound(f"sounds/metalrun.wav")

		self.baloon_noises = []
		for i in range(3):
			self.baloon_noises.append(
				pygame.mixer.Sound(f"sounds/echo{i+1}.wav")
				
			)


		self.telephone_audios = []
		for i in range(6):
			self.telephone_audios.append(
				f"sounds/call{i+1}b.wav"
			)

		# -- Cutscene --
		self.move_sound = pygame.mixer.Sound(f"sounds/machineturn2.wav")
		self.cutscene_ambient = pygame.mixer.Sound(f"sounds/Scary_Space_B.wav")
		self.ambiance_2 = pygame.mixer.Sound(f"sounds/ambience2.wav")
		self.robot_err = pygame.mixer.Sound("sounds/Robot.wav")
		self.static_end = pygame.mixer.Sound("sounds/staticend2.wav")
		self.pop = pygame.mixer.Sound("sounds/pop.wav")

		# -- Minigames --
		self.sv_tm_audio = [
			pygame.mixer.Sound(f"sounds/S2.wav"),
			pygame.mixer.Sound(f"sounds/A2.wav"),
			pygame.mixer.Sound(f"sounds/V2.wav"),
			pygame.mixer.Sound(f"sounds/E2.wav"),
			pygame.mixer.Sound(f"sounds/T2.wav"),
			pygame.mixer.Sound(f"sounds/H2.wav"),
			pygame.mixer.Sound(f"sounds/E2.wav"),
			pygame.mixer.Sound(f"sounds/M2.wav")
		]


	def fonts(self):
		self.ocr_font = pygame.font.Font("fonts/1.TTF")