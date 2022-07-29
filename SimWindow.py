from PPlay.window import *

class SimWindow:
    window = Window(1280, 720)
    keyboard = window.get_keyboard()
    mouse = window.get_mouse()

SimWindow.window.set_title("Bus Temperature FIS Simulation")
