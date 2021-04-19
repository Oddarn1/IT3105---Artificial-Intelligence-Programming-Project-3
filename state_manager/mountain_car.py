import random
import numpy as np

class MountainCar():

    def __init__(self):
        self.legal_actions = [-1, 0, 1]
        self.pos = random.uniform(-0.6, -0.4)
        self.velocity = 0

    def update_state(self, move):
        if move not in self.legal_actions:
            raise Exception("Illegal move")
        self.velocity += 0.001 * move - 0.0025 * np.cos(3*self.pos)
        if self.velocity > 0.07:
            self.velocity = 0.07
        elif self.velocity < - 0.07:
            self.velocity = - 0.07
        self.pos += self.velocity
        if self.pos < - 1.2:
            self.pos = - 1.2
        elif self.pos > 0.6:
            self.pos = 0.6
    