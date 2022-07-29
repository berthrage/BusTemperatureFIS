import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

class FuzzyController:
    def __init__(self):

        self.tempExternalRange = np.arange(-20, 70, 1)
        self.tempInternalRange = np.arange(-20, 70, 1)
        self.tempAirCondRange = np.arange(16, 70, 1)

        self.tempExternal = ctrl.Antecedent(self.tempExternalRange, 'InternalTemperature')
        self.tempInternal = ctrl.Antecedent(self.tempInternalRange, 'ExternalTemperature')
        self.tempAirCond = ctrl.Consequent(self.tempAirCondRange, 'AirConditionerTemperature', 'bisector')


        self.tempExternal['cold'] = fuzz.trimf(self.tempExternal.universe, [-100000, 7, 14])
        self.tempExternal['medium'] = fuzz.trimf(self.tempExternal.universe, [12, 20, 23])
        self.tempExternal['hot'] = fuzz.trimf(self.tempExternal.universe, [20, 30, 100000])

        self.tempInternal['cold'] = fuzz.trimf(self.tempInternal.universe, [-100000, 7, 14])
        self.tempInternal['medium'] = fuzz.trimf(self.tempInternal.universe, [12, 20, 23])
        self.tempInternal['hot'] = fuzz.trimf(self.tempInternal.universe, [20, 30, 100000])


        self.tempAirCond['cold'] = fuzz.trimf (self.tempAirCond.universe, [-100000, 16, 22])
        self.tempAirCond['hot'] = fuzz.trimf (self.tempAirCond.universe, [20, 31, 31])
        self.tempAirCond['off'] = fuzz.trimf (self.tempAirCond.universe, [32, 33, 100000])

        self.rule1 = ctrl.Rule(self.tempExternal['cold'] | self.tempInternal['cold'], self.tempAirCond['off'])
        self.rule2 = ctrl.Rule(self.tempExternal['medium'] | self.tempInternal['medium'], self.tempAirCond['hot'])
        self.rule3 = ctrl.Rule(self.tempExternal['hot'] | self.tempInternal['hot'], self.tempAirCond['cold'])

        self.tempControlSystem = ctrl.ControlSystem ([self.rule1, self.rule2, self.rule3])
        self.tempController = ctrl.ControlSystemSimulation(self.tempControlSystem)

    def viewMemberships(self):
        self.tempExternal['hot'].view()
        self.tempInternal['hot'].view()
        self.tempAirCond['hot'].view()
        plt.show()

    def viewDefuzzification(self):
        self.tempAirCond.view(sim=self.tempController)
        plt.show()

    def viewRulesGraphs(self):
        self.rule1.view()
        self.rule2.view()
        self.rule3.view()
        plt.show()

    def computeInputs(self, internalTemperature, externalTemperature):
        self.tempController.input['InternalTemperature'] = internalTemperature
        self.tempController.input['ExternalTemperature'] = externalTemperature

        self.tempController.compute()


    def output(self):
        return self.tempController.output['AirConditionerTemperature']