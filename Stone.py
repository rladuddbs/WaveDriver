import random

from pico2d import load_image
from tkinter import *
import time

import GameWorld
import sea

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()
class Stone:
    image = None

    def __init__(self):
        if Stone.image == None:
            Stone.image = load_image('stone.png')
        self.x, self.y = random.randint(200, monitor_width - 200), monitor_height + 200
        self.V = 0
        self.start_time = time.time()

    def draw(self):
        self.image.clip_draw(0, 0, 300, 300, self.x, self.y - 300, 200, 200)

    def update(self):
        self.y += self.V / 10000
        pass
    def GetVelocity(self, V):
        self.V = V
        pass

    def create(self):

        pass