from pico2d import *
from tkinter import *
import time

import boat
import play_mode

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

class Heart:
    def __init__(self, x):
        self.image = load_image('heart.png')
        self.x = x
        self.last_time = time.time()

    def draw(self):
        self.image.clip_draw(0, 0, 30, 30, 150 * (self.x + 1) - (self.x * 50), monitor_height - 150, 150, 150)
        pass

    def update(self):

        pass

    def GetVelocity(self, V):
        pass


