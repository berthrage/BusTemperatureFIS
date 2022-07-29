from SimWindow import SimWindow
from PPlay.sprite import *
from PPlay.rect import *

class Bus:
    def __init__(self):
        self.busSprite = Sprite("sprites/aircondOff.png")
        self.intTempSprite = Sprite("sprites/intTemperaturecold.png")
        self.busSprite.set_position(360, 415)
        self.intTempRect = Rect(self.busSprite.x + 20, self.busSprite.y - 23, 509, 25)
        self.intTempRectColor = [0, 0, 0]
        self.intTempSprite.set_position(self.busSprite.x + 20, self.busSprite.y - 23)
        self.currentBusX = self.busSprite.x
        self.currentBusY = self.busSprite.y
        self.currentIntTempX = self.intTempSprite.x
        self.currentIntTempY = self.intTempSprite.y

    def drawBus(self):
        self.busSprite.draw()
        #self.intTempSprite.draw()
        SimWindow.window.draw_rect(self.intTempRectColor, self.intTempRect.rect, 0, 10)

    def changeBusSprite(self, busSprite):
        self.busSprite = busSprite
        self.busSprite.set_position(self.currentBusX, self.currentBusY)

    def changeIntTempColor(self, color):
        self.intTempRectColor = color

    def changeIntTempSprite(self, intTempSprite):
        self.intTempSprite = intTempSprite
        self.intTempSprite.set_position(self.currentIntTempX, self.currentIntTempY)