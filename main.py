import numpy as np
from visualizations.animation import Animation
from state_manager.mountain_car import MountainCar

mc = MountainCar()
# TODO: init Animation with positions per episode from agent
anim = Animation(mc.pos, np.array([-0.4, -0.41, -0.405]))

if __name__ == "__main__":
    anim.plot_curve()