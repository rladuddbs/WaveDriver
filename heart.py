from pico2d import *
from tkinter import *
import time

import boat
import game_world
import play_mode

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

class Heart:
    def __init__(self, x):
        self.image = load_image('heart.png')
        self.x = x
        self.last_time = time.time()
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 30, 0, 30, 30, 150 * (self.x + 1) - (self.x * 50), monitor_height - 150, 150, 150)
        pass

    def update(self):
        if self.x == play_mode.boat.Durability:
            if time.time() - self.last_time > 0.1:
                self.frame = self.frame + 1
                self.last_time = time.time()
        if self.frame == 4:
            game_world.remove_object(self)
        pass

    def GetVelocity(self, V):
        pass


