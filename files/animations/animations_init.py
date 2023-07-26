from files.animations.sprites_animation import SpritesAnimation
from files.animations.darkness_effect import DarknessAnimation
from files.animations.static_stripe_animation import StaticStripesAnimation

class animations_init:
    def __init__(self, App):
        self.monitor = SpritesAnimation(sprites=App.assets.camera_sprites, position=(0, 0))

        self.mask = SpritesAnimation(sprites=App.assets.mask_sprites[0:9], position=(0, 0), frame_wait=1)

        self.desk = SpritesAnimation(sprites=App.assets.desk_animation, position=(0, 0), frame_wait=4, isLoop=True)

        self.static_anim_1 = SpritesAnimation(sprites=App.assets.static_1, position=(0, 0), alpha=255, isLoop=True)

        self.static_anim_2 = SpritesAnimation(sprites=App.assets.static_2, position=(0, 0), frame_wait=3)

        self.darkness = DarknessAnimation(App=App, position=(0,0), frame_wait=3, fading_time=15000)

        self.darkness_reversed = DarknessAnimation(App=App, position=(0,0), frame_wait=0, fading_time=15000, time_until_fade=0, reversed_=True)

        self.static_stripes_animation = StaticStripesAnimation(App=App)

        self.static_stripes_animation2 = StaticStripesAnimation(App=App, time_to_appear=5000, speed_frame=2, random_sprites_range=(2, 4), alpha=20)

        self.static_stripes_animation3 = StaticStripesAnimation(App=App, time_to_appear=3700, speed_frame=5, random_sprites_range=(3, 4), alpha=10)

        self.static_stripes_animation4 = StaticStripesAnimation(App=App, time_to_appear=3700, speed_frame=6, random_sprites_range=(4, 4), alpha=40)

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