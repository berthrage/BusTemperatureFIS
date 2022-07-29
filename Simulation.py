import random
import dataclasses

from Background import Backgrounds
from Bus import Bus
from Fonts import Fonts
from FuzzyController import FuzzyController
from Input import Input
from Misc import Misc
from SimWindow import SimWindow
from PPlay.sprite import *


class Simulation:
    def __init__(self):
        self.windowColor = [255, 255, 255]
        self.textColor = [0, 0, 0]
        self.fuzzController = FuzzyController()
        self.externalTemperature = 16
        self.internalTemperature = 24
        self.externalTemperatureSetting = 'medium'
        self.internalTemperatureSetting = 'cold'
        self.foundTemperatures = False
        self.setTemperaturesTimer = Misc.Timer()
        self.buttonsBorderRadius = 10
        self.viewRules = False
        self.backgrounds = Backgrounds()
        self.bus = Bus()
        self.outputAirCondTemp = 0
        self.aircondState = "OFF"
        self.pause = False

        @dataclasses.dataclass
        class Button:
            rect: None
            borderWidth: int
            textColor: list[int]
            selected: False

        self.buttons = {
            'viewFunctions': Button(SimWindow.window.typeRect(), 2, self.textColor, False),
            'viewRules': Button(SimWindow.window.typeRect(), 2, self.textColor, False),
            'viewRulesGraphs': Button(SimWindow.window.typeRect(), 2, self.textColor, False),
            'viewDefuzzification': Button(SimWindow.window.typeRect(), 2, self.textColor, False),
            'externalCold': Button(SimWindow.window.typeRect(), 2, self.textColor, False),
            'externalMedium': Button(SimWindow.window.typeRect(), 2, self.textColor, False),
            'externalHot': Button(SimWindow.window.typeRect(), 2, self.textColor, False),
            'internalCold': Button(SimWindow.window.typeRect(), 2, self.textColor, False),
            'internalMedium': Button(SimWindow.window.typeRect(), 2, self.textColor, False),
            'internalHot': Button(SimWindow.window.typeRect(), 2, self.textColor, False),
        }

    def executeSimulation(self):
        while True:
            Input.inputHandler()
            self.setBackgroundColorTemperature()


            self.getTemperaturesInRange()
            self.backgrounds.drawBackgrounds()
            if(not self.pause):
                self.backgrounds.moveBackgrounds()

            self.bus.drawBus()
            self.changeBusSpritesTemperatures()

            self.fuzzController.computeInputs(self.externalTemperature, self.internalTemperature)
            self.outputAirCondTemp = self.fuzzController.output()

            self.renderHUD()
            self.controlHUD()

            SimWindow.window.update()

            if (Input.getKeyDown("ESC")):
                break

    def getTemperaturesInRange(self):
        self.setTemperaturesTimer.resumeTimer()
        self.setTemperaturesTimer.executeTimer()

        if (self.setTemperaturesTimer.time > 2):
            if (self.externalTemperatureSetting == 'cold'):
                self.externalTemperature = random.randrange(0, 14)
            elif (self.externalTemperatureSetting == 'medium'):
                self.externalTemperature = random.randrange(12, 23)
            elif (self.externalTemperatureSetting == 'hot'):
                self.externalTemperature = random.randrange(20, 40)

            if (self.internalTemperatureSetting == 'cold'):
                self.internalTemperature = random.randrange(0, 14)
            elif (self.internalTemperatureSetting == 'medium'):
                self.internalTemperature = random.randrange(12, 23)
            elif (self.internalTemperatureSetting == 'hot'):
                self.internalTemperature = random.randrange(20, 40)

            self.setTemperaturesTimer.stopTimer()
            self.setTemperaturesTimer.resetTimer()

    def renderHUD(self):
        SimWindow.window.draw_rect(self.textColor, self.buttons['viewFunctions'].rect, self.buttons['viewFunctions'].borderWidth,
                                   self.buttonsBorderRadius)
        self.buttons['viewFunctions'].rect = SimWindow.window.draw_text(f"View functions", 1000, 50, 30, self.buttons['viewFunctions'].textColor,
                                                                        Fonts.connection3,
                                                                        True, False, False)

        SimWindow.window.draw_rect(self.textColor, self.buttons['viewRules'].rect, self.buttons['viewRules'].borderWidth,
                                   self.buttonsBorderRadius)
        self.buttons['viewRules'].rect = SimWindow.window.draw_text(f"View rules", 1078, 90, 30, self.buttons['viewRules'].textColor,
                                                                        Fonts.connection3,
                                                                        True, False, False)

        SimWindow.window.draw_rect(self.textColor, self.buttons['viewRulesGraphs'].rect, self.buttons['viewRulesGraphs'].borderWidth,
                                   self.buttonsBorderRadius)
        self.buttons['viewRulesGraphs'].rect = SimWindow.window.draw_text(f"View rules graphs", 950, 130, 30, self.buttons[
            'viewRulesGraphs'].textColor,
                                                                    Fonts.connection3,
                                                                    True, False, False)

        SimWindow.window.draw_rect(self.textColor, self.buttons['viewDefuzzification'].rect, self.buttons['viewDefuzzification'].borderWidth,
                                   self.buttonsBorderRadius)
        self.buttons['viewDefuzzification'].rect = SimWindow.window.draw_text(f"View deffuzification", 905, 170, 30, self.buttons[
            'viewDefuzzification'].textColor,
                                                                        Fonts.connection3,
                                                                        True, False, False)


        SimWindow.window.draw_text(f"Set Temperatures", 10, 0, 20, self.textColor, Fonts.connection3, False,
                                   False,
                                   False)

        SimWindow.window.draw_text(f"External", 10, 20, 30, self.textColor, Fonts.connection3, False,
                                   False,
                                   False)

        SimWindow.window.draw_rect(self.textColor, self.buttons['externalCold'].rect, self.buttons['externalCold'].borderWidth,
                                   self.buttonsBorderRadius)

        self.buttons['externalCold'].rect = SimWindow.window.draw_text(f"Cold", 150, 20, 30, self.buttons['externalCold'].textColor, Fonts.connection3,
                                                                       True,
                                   False,
                                   False)

        SimWindow.window.draw_rect(self.textColor, self.buttons['externalMedium'].rect, self.buttons['externalMedium'].borderWidth,
                                   self.buttonsBorderRadius)

        self.buttons['externalMedium'].rect = SimWindow.window.draw_text(f"Medium", 230, 20, 30, self.buttons['externalMedium'].textColor,
                                                                         Fonts.connection3, True,
                                                           False,
                                                           False)


        SimWindow.window.draw_rect(self.textColor, self.buttons['externalHot'].rect, self.buttons['externalHot'].borderWidth,
                                   self.buttonsBorderRadius)

        self.buttons['externalHot'].rect = SimWindow.window.draw_text(f"Hot", 367, 20, 30, self.buttons['externalHot'].textColor, Fonts.connection3,
                                                                      True,
                                                             False,
                                                             False)


        SimWindow.window.draw_text(f"Internal", 10, 60, 30, self.textColor, Fonts.connection3, False,
                                   False,
                                   False)

        SimWindow.window.draw_rect(self.textColor, self.buttons['internalCold'].rect, self.buttons['internalCold'].borderWidth,
                                   self.buttonsBorderRadius)

        self.buttons['internalCold'].rect = SimWindow.window.draw_text(f"Cold", 150, 60, 30, self.buttons['internalCold'].textColor,
                                                                       Fonts.connection3, True,
                                                           False,
                                                           False)

        SimWindow.window.draw_rect(self.textColor, self.buttons['internalMedium'].rect, self.buttons['internalMedium'].borderWidth,
                                   self.buttonsBorderRadius)

        self.buttons['internalMedium'].rect = SimWindow.window.draw_text(f"Medium", 230, 60, 30, self.buttons['internalMedium'].textColor,
                                                                         Fonts.connection3, True,
                                                             False,
                                                             False)

        SimWindow.window.draw_rect(self.textColor, self.buttons['internalHot'].rect, self.buttons['internalHot'].borderWidth,
                                   self.buttonsBorderRadius)

        self.buttons['internalHot'].rect = SimWindow.window.draw_text(f"Hot", 367, 60, 30, self.buttons['internalHot'].textColor,
                                                                      Fonts.connection3, True,
                                                          False,
                                                          False)


        SimWindow.window.draw_text(f"External Temperature:{self.externalTemperature} C", 500, 20, 20, self.textColor, Fonts.connection3, False,
                                   False,
                                   False)

        SimWindow.window.draw_text(f"Internal Temperature:{self.internalTemperature} C", 500, self.bus.intTempRect.rect.y - 20, 20, self.textColor,
                                   Fonts.connection3,
                                   False,
                                   False,
                                   False)

        if (self.outputAirCondTemp >= 32):
            SimWindow.window.draw_text(f"Air Conditioner: OFF", 400, self.bus.busSprite.y + 200, 50, self.textColor,
                                       Fonts.connection3, False,
                                       False, False)
        else:
            SimWindow.window.draw_text(f"Air Conditioner:{self.outputAirCondTemp:.1f} C", 400, self.bus.busSprite.y + 200, 50, self.textColor,
                                       Fonts.connection3, False,
                                       False, False)


        if (self.outputAirCondTemp >= 16 and self.outputAirCondTemp <= 22):
            self.airCondState = "COLD"
        elif (self.outputAirCondTemp >= 23 and self.outputAirCondTemp <= 32):
            self.airCondState = "HOT"
        elif (self.outputAirCondTemp > 32):
            self.airCondState = "OFF"

        SimWindow.window.draw_text(self.airCondState, 520, self.bus.busSprite.y + 130, 30, self.textColor,
                                       Fonts.connection3, True,
                                       False, False)
        if (self.viewRules):
            SimWindow.window.draw_text("-if external temp is COLD or internal temp is COLD then air cond temp is OFF", 330, 230, 20, self.textColor,
                                       Fonts.connection3, True,
                                       False, False)
            SimWindow.window.draw_text("-if external temp is MEDIUM or internal temp is MEDIUM then air cond temp is HOT", 330, 250, 20,
                                       self.textColor,
                                       Fonts.connection3, True,
                                       False, False)
            SimWindow.window.draw_text("-if external temp is HOT or internal temp is HOT then air cond temp is COLD", 330, 270, 20, self.textColor,
                                       Fonts.connection3, True,
                                       False, False)

        for button in self.buttons.values():
            if (button.selected == True):
                button.borderWidth = 0
                button.textColor = [255, 255, 255]
            else:
                button.borderWidth = 2
                button.textColor = self.textColor


        if(self.externalTemperatureSetting == 'cold'):
            self.buttons['externalCold'].selected = True
        else:
            self.buttons['externalCold'].selected = False

        if (self.externalTemperatureSetting == 'medium'):
            self.buttons['externalMedium'].selected = True
        else:
            self.buttons['externalMedium'].selected = False

        if (self.externalTemperatureSetting == 'hot'):
            self.buttons['externalHot'].selected = True
        else:
            self.buttons['externalHot'].selected = False

        if (self.internalTemperatureSetting == 'cold'):
            self.buttons['internalCold'].selected = True
        else:
            self.buttons['internalCold'].selected = False

        if (self.internalTemperatureSetting == 'medium'):
            self.buttons['internalMedium'].selected = True
        else:
            self.buttons['internalMedium'].selected = False

        if (self.internalTemperatureSetting == 'hot'):
            self.buttons['internalHot'].selected = True
        else:
            self.buttons['internalHot'].selected = False


    def controlHUD(self):

        if (SimWindow.mouse.is_over_object(self.buttons['viewFunctions'].rect)):
            self.buttons['viewFunctions'].selected = True
            if (Input.getMouseButtonDown(1)):
                self.buttons['viewFunctions'].selected = True
                self.pause = True
                self.fuzzController.viewMemberships()
            else:
                self.pause = False

        elif (SimWindow.mouse.is_over_object(self.buttons['viewRulesGraphs'].rect)):
            self.buttons['viewRulesGraphs'].selected = True
            if (Input.getMouseButtonDown(1)):
                self.buttons['viewRulesGraphs'].selected = True
                self.pause = True
                self.fuzzController.viewRulesGraphs()
            else:
                self.pause = False
        elif (SimWindow.mouse.is_over_object(self.buttons['viewDefuzzification'].rect)):
            self.buttons['viewDefuzzification'].selected = True
            if (Input.getMouseButtonDown(1)):
                self.buttons['viewDefuzzification'].selected = True
                self.pause = True
                self.fuzzController.viewDefuzzification()
            else:
                self.pause = False
        else:
            self.buttons['viewFunctions'].selected = False
            self.buttons['viewRulesGraphs'].selected = False
            self.buttons['viewDefuzzification'].selected = False
            self.pause = False


        if (SimWindow.mouse.is_over_object(self.buttons['viewRules'].rect)):
            self.buttons['viewRules'].selected = True
            if (not self.viewRules and Input.getMouseButtonDown(1)):
                self.viewRules = True

            if (self.viewRules and Input.getMouseButtonDown(1)):
                self.viewRules = False
        else:
            self.buttons['viewRules'].selected = False

        if(self.viewRules):
            self.buttons['viewRules'].selected = True









        if (SimWindow.mouse.is_over_object(self.buttons['externalCold'].rect)):
            self.buttons['externalCold'].selected = True
            if (Input.getMouseButtonDown(1)):
                self.externalTemperatureSetting = 'cold'


        if (SimWindow.mouse.is_over_object(self.buttons['externalMedium'].rect)):
            self.buttons['externalMedium'].selected = True
            if (Input.getMouseButtonDown(1)):
                self.externalTemperatureSetting = 'medium'

        if (SimWindow.mouse.is_over_object(self.buttons['externalHot'].rect)):
            self.buttons['externalHot'].selected = True
            if (Input.getMouseButtonDown(1)):
                self.externalTemperatureSetting = 'hot'

        if (SimWindow.mouse.is_over_object(self.buttons['internalCold'].rect)):
            self.buttons['internalCold'].selected = True
            if (Input.getMouseButtonDown(1)):
                self.internalTemperatureSetting = 'cold'

        if (SimWindow.mouse.is_over_object(self.buttons['internalMedium'].rect)):
            self.buttons['internalMedium'].selected = True
            if (Input.getMouseButtonDown(1)):
                self.internalTemperatureSetting = 'medium'

        if (SimWindow.mouse.is_over_object(self.buttons['internalHot'].rect)):
            self.buttons['internalHot'].selected = True
            if (Input.getMouseButtonDown(1)):
                self.internalTemperatureSetting = 'hot'

    def setBackgroundColorTemperature(self):
        if(self.externalTemperatureSetting == 'cold'):
            SimWindow.window.set_background_color([250 - self.externalTemperature, 250 - self.externalTemperature, 250 - self.externalTemperature])
        elif(self.externalTemperatureSetting == 'medium'):
            SimWindow.window.set_background_color([133 - self.externalTemperature, 236 - self.externalTemperature, 252 - self.externalTemperature])
        elif (self.externalTemperatureSetting == 'hot'):
            SimWindow.window.set_background_color([250 - self.externalTemperature, 201 - self.externalTemperature, 99 - self.externalTemperature])

    def changeBusSpritesTemperatures(self):
        if(self.outputAirCondTemp >= 16 and self.outputAirCondTemp <= 22):
            self.bus.changeBusSprite(Sprite("sprites/aircondCold.png"))
        elif (self.outputAirCondTemp >= 23 and self.outputAirCondTemp <= 32):
            self.bus.changeBusSprite(Sprite("sprites/aircondHot.png"))
        elif (self.outputAirCondTemp > 32):
            self.bus.changeBusSprite(Sprite("sprites/aircondOff.png"))

        if (self.internalTemperatureSetting == 'cold'):
            self.bus.changeIntTempColor([182 - self.internalTemperature, 223 - self.internalTemperature, 247 - self.internalTemperature])
        elif (self.internalTemperatureSetting == 'medium'):
            self.bus.changeIntTempColor([231 - self.internalTemperature, 80 - self.internalTemperature, 239 - self.internalTemperature])
        elif (self.internalTemperatureSetting == 'hot'):
            self.bus.changeIntTempColor([250 - self.internalTemperature, 63 - self.internalTemperature, 50 - self.internalTemperature])
        #if(self.internalTemperatureSetting == 'cold'):

