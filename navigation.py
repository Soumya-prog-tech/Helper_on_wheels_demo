import numpy as np

class RobotNavigator:
    def __init__(self):
        self.position = np.array([0,0])
        self.target = None

    def set_target(self, target_position):
        self.target = np.array(target_position)

    def move_towards_target(self):
        while not np.array_equal(self.position,self.target):
            step = np.sign(self.target - self.position)
            self.position += step
        print("reached the target")

navigator = RobotNavigator()
navigator.set_target([1,1]) # taking a target for example
navigator.move_towards_target()

