from SimWindow import SimWindow
from PPlay.sprite import *

class Background:
    def __init__(self, setPosX, setPosY):
        self.sprite = Sprite("sprites/background.png")
        self.sprite.set_position(setPosX, setPosY)
        self.speed = 0

class Backgrounds:
    def __init__(self):
        self.bg1 = Background(0, 0)
        self.bg2 = Background(1280, 0)
        self.scrollingSpeed = 200

    def drawBackgrounds(self):
        self.bg1.sprite.draw()
        self.bg2.sprite.draw()

    def moveBackgrounds(self):
        self.speed = self.scrollingSpeed * SimWindow.window.delta_time()
        self.bg1.sprite.x -= self.speed
        self.bg2.sprite.x -= self.speed
        #print(SimWindow.window.delta_time())

        if(self.bg1.sprite.x < -SimWindow.window.width):
            self.bg1.sprite.x = 1280

        if (self.bg2.sprite.x < -SimWindow.window.width):
            self.bg2.sprite.x = 1280
