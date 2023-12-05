import random

from pico2d import load_image, draw_rectangle
from tkinter import *
import time

import game_world
import sea

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()
class Stone:
    image = None

    def __init__(self):
        if Stone.image == None:
            Stone.image = load_image('stone.png')
        self.x, self.y = random.randint(50, monitor_width - 50), monitor_height + 200
        self.V = 0
        self.start_time = time.time()

    def draw(self):
        self.image.clip_draw(0, 0, 300, 300, self.x, self.y, 200, 200)
        # draw_rectangle(*self.get_bb())

    def update(self):
        self.y += self.V / 10000
        self.delete()
        pass
    def GetVelocity(self, V):
        self.V = V
        pass

    def get_bb(self):
        return self.x - 35, self.y - 30, self.x + 35, self.y + 30

    def handle_collision(self, group, other):
        if group == 'boat:stone':
            game_world.remove_object(self)

    def delete(self):
        if self.y < -100:
            game_world.remove_object(self)
        pass
