import random
from files.animations.sprites_animation import SpritesAnimation
from files.animations.darkness_effect import DarknessAnimation
from files.animations.static_stripe_animation import StaticStripesAnimation
from files.animations.random_animation import RandomSpritesAnimation
from files.animations.fade_effect import FadeEffect
from files.animations.mask_animation import MaskAnimation

class animations_init:
    def __init__(self, App):
        self.monitor = SpritesAnimation(sprites=App.assets.camera_sprites, position=(0, 0), frame_wait=1)

        self.mask = SpritesAnimation(sprites=App.assets.mask_sprites[0:9], position=(0, 0), frame_wait=1)

        self.desk = SpritesAnimation(sprites=App.assets.desk_animation, position=(0, 0), frame_wait=4, isLoop=True)

        self.static_anim_1 = SpritesAnimation(sprites=App.assets.static_1, position=(0, 0), alpha=255, isLoop=True, frame_wait=3)

        self.static_anim_2 = SpritesAnimation(sprites=App.assets.static_2, position=(0, 0), frame_wait=3)

        self.darkness = DarknessAnimation(App=App, position=(0,0), frame_wait=3, fading_time=15000)

        self.fade_effect = FadeEffect(App=App, position=(0, 0))

        self.static_stripes_animation = StaticStripesAnimation(App=App, alpha=8)

        self.static_stripes_animation2 = StaticStripesAnimation(App=App, time_to_appear=5567, speed_frame=2, random_sprites_range=(2, 4), alpha=10)
        self.static_stripes_animation2.big_stripe_y_location = random.randint(100, 500)

        self.static_stripes_animation3 = StaticStripesAnimation(App=App, time_to_appear=3709, speed_frame=5, random_sprites_range=(3, 4), alpha=10)
        self.static_stripes_animation3.big_stripe_y_location = random.randint(400, 700)

        self.static_stripes_animation4 = StaticStripesAnimation(App=App, time_to_appear=4200, speed_frame=6, random_sprites_range=(4, 4), alpha=10)
        self.static_stripes_animation4.big_stripe_y_location = random.randint(100, 300)

        self.static_stripes_animation5 = StaticStripesAnimation(App=App, random_sprites_range=(3, 3)) # Used on the menu and cameras

        self.random_static_animation = RandomSpritesAnimation(App=App, sprites=App.assets.static_2, position=(0, 0), speed_frame=5)

        self.mask_animation = MaskAnimation(position=[0, 20])

        self.cutscene_mask_animation = MaskAnimation(position=[-30, -20], move=(0.06, 0.02))

        self.static_anim_2_looped = SpritesAnimation(sprites=App.assets.static_2, position=(0, 0), frame_wait=3, isLoop=True)

        # Confetti
        confs = [App.assets.blue_conf, App.assets.yellow_conf, App.assets.green_conf, App.assets.pink_conf]
        self.confs_animation = []
        for con in confs:
            for i in range(5):
                self.confs_animation.append(
                    SpritesAnimation(con, [random.randint(0, App.dimentions[0] - 40), 0], frame_wait=6, isLoop=True)
                )


        # -- Jumpscares --
        self.puppet_jump = SpritesAnimation(sprites=App.assets.puppet_screamer_animation, position=(0, 0), frame_wait=2)
        self.toy_bunny_jump = SpritesAnimation(sprites=App.assets.toy_bunny_screamer_animation, position=(0, 0), frame_wait=2)
        self.toy_chica_jump = SpritesAnimation(sprites=App.assets.toy_chica_screamer_animation, position=(0, 0), frame_wait=2)
        self.toy_freddy_jump = SpritesAnimation(sprites=App.assets.toy_freddy_screamer_animation, position=(0, 0), frame_wait=2)
        self.withered_freddy_jump = SpritesAnimation(sprites=App.assets.withered_freddy_screamer_animation, position=(0, 0), frame_wait=2)
        self.withered_bonnie_jump = SpritesAnimation(sprites=App.assets.withered_bonnie_screamer_animation, position=(0, 0), frame_wait=2)
        self.withered_chica_jump = SpritesAnimation(sprites=App.assets.withered_chica_screamer_animation, position=(0, 0), frame_wait=2)
        self.foxy_jump = SpritesAnimation(sprites=App.assets.foxy_screamer_animation, position=(0,0), frame_wait=2)
        self.mangle_jump = SpritesAnimation(sprites=App.assets.mangle_screamer_animation, position=(0,0), frame_wait=2)
        self.golden_freddy_jump = SpritesAnimation(sprites=App.assets.golden_freddy_animation, position=(0,0), frame_wait=2)