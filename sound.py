import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sounds'
        self.shotgun_sound = pg.mixer.Sound(self.path + '/dsshotgn.wav')