import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl


class ExampleFuzzyController:
    def __init__(self):
        self.x_qual = np.arange(0, 11, 1)
        self.x_serv = np.arange(0, 13, 1)
        self.x_tip = np.arange(0, 26, 1)

        self.qual_lo = fuzz.trimf(self.x_qual, [0, 0, 5])
        self.qual_md = fuzz.trimf(self.x_qual, [0, 5, 10])
        self.qual_hi = fuzz.trimf(self.x_qual, [5, 10, 10])
        self.serv_lo = fuzz.trimf(self.x_serv, [0, 0, 5])
        self.serv_md = fuzz.trimf(self.x_serv, [0, 5, 10])
        self.serv_hi = fuzz.trimf(self.x_serv, [5, 10, 100000])
        self.tip_lo = fuzz.trimf(self.x_tip, [0, 0, 13])
        self.tip_md = fuzz.trimf(self.x_tip, [0, 13, 25])
        self.tip_hi = fuzz.trimf(self.x_tip, [13, 25, 25])



    def generatePlot(self):
        # Visualize these universes and membership functions
        self.fig, (self.ax0, self.ax1, self.ax2) = plt.subplots (nrows=3, figsize=(8, 9))

        self.ax0.plot(self.x_qual, self.qual_lo, 'b', linewidth=1.5, label='Bad')
        self.ax0.plot(self.x_qual, self.qual_md, 'g', linewidth=1.5, label='Decent')
        self.ax0.plot(self.x_qual, self.qual_hi, 'r', linewidth=1.5, label='Great')
        self.ax0.set_title ('Food quality')
        self.ax0.legend()

        self.ax1.plot(self.x_serv, self.serv_lo, 'b', linewidth=1.5, label='Poor')
        self.ax1.plot(self.x_serv, self.serv_md, 'g', linewidth=1.5, label='Acceptable')
        self.ax1.plot(self.x_serv, self.serv_hi, 'r', linewidth=1.5, label='Amazing')
        self.ax1.set_title ('Service quality')
        self.ax1.legend()

        self.ax2.plot(self.x_tip, self.tip_lo, 'b', linewidth=1.5, label='Low')
        self.ax2.plot(self.x_tip, self.tip_md, 'g', linewidth=1.5, label='Medium')
        self.ax2.plot(self.x_tip, self.tip_hi, 'r', linewidth=1.5, label='High')
        self.ax2.set_title('Tip amount')
        self.ax2.legend ()

        # Turn off top/right axes
        for ax in (self.ax0, self.ax1, self.ax2):
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()

        plt.tight_layout()

    def showPlot(self):
        plt.show()
