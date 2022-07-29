from SimWindow import *
from multiprocessing import Process
import threading
import multiprocessing
import time

class Input:

    mouseButtonPressed = {
        1: False, #LEFTCLICK
        2: False, #MIDDLECLICK
        3: False, #RIGHTCLICK
        #4: False, #SCROLLUP
        #5: False #SCROLLDOWN
    }

    keyPressed = {
        "ESC": False,
        "UP": False,
        "DOWN": False,
        "SPACE": False,
        "w": False,
        "s": False,
        "a": False,
        "d": False,
        "e": False,
        "i": False,
        "j": False,
        "k": False,
        "l": False,
    }

    @staticmethod
    def getMouseButtonDown(mouseButton):

        if(SimWindow.mouse.is_button_pressed(mouseButton) and not Input.mouseButtonPressed[mouseButton]):
            Input.mouseButtonPressed[mouseButton] = True
            #thread2 = threading.Thread(target=Input.checkMouseClick, args=(mouseButton,))
            #thread2.daemon = True
            #thread2.start()
            return True

        return False

    @staticmethod
    def getKeyDown(keyButton):
        if (SimWindow.keyboard.key_pressed(keyButton) and not Input.keyPressed[keyButton]):
            Input.keyPressed[keyButton] = True
            #thread3 = threading.Thread(target=Input.checkKeyPress, args=(keyButton,))
            #thread3.daemon = True
            #thread3.start()
            return True

        return False

    @staticmethod
    def checkMouseClick(mouseButton):
        while True:
            if(not SimWindow.mouse.is_button_pressed(mouseButton)):
                Input.mouseButtonPressed[mouseButton] = False
                break

    @staticmethod
    def checkKeyPress(keyButton):
        while True:
            if(not SimWindow.keyboard.key_pressed(keyButton)):
                Input.keyPressed[keyButton] = False
                break

    @staticmethod
    def checkMouseClickNonThread(mouseButton):
        if (not SimWindow.mouse.is_button_pressed(mouseButton)):
            Input.mouseButtonPressed[mouseButton] = False

    @staticmethod
    def checkKeyPressNonThread(keyButton):
        if (not SimWindow.keyboard.key_pressed(keyButton)):
            Input.keyPressed[keyButton] = False

    @staticmethod
    def inputHandler():
        for mouseButton in Input.mouseButtonPressed:
            Input.checkMouseClickNonThread(mouseButton)

        for keyButton in Input.keyPressed:
            Input.checkKeyPressNonThread(keyButton)