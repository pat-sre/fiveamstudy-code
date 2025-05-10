from abc import ABC, abstractmethod

class Stepper:
    def walk_distance(self):
        raise NotImplemented
    
class StepperMetric(Stepper):
    def walk(self, m):
        pass

class StepperImperial(Stepper):
    def convert_m_to_feet(self, m):
        return 3.281 * m
    
    def walk(self, m):
        print(f"walked {self.convert_m_to_feet(m)} feet")

si = StepperImperial()
si.walk(10)