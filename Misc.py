class Misc:
    class Timer:
        def __init__(self, time=0):
            self.time = time
            self.initialTime = time
            self.stop = False

        def executeTimer(self):
            if (not self.stop):
                from SimWindow import SimWindow
                self.time += SimWindow.window.delta_time()

        def stopTimer(self):
            self.stop = True

        def resumeTimer(self):
            self.stop = False

        def resetTimer(self):
            self.time = self.initialTime
