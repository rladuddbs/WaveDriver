import random

from pico2d import load_image, draw_rectangle
from tkinter import *
import time

import game_world
import sea

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()
class Arrow:
    image = None

    def __init__(self):
        if Arrow.image == None:
            Arrow.image = load_image('arrow.png')
        self.x, self.y = random.randint(600, monitor_width - 500), monitor_height + 200
        self.V = 0
        self.start_time = time.time()
        self.frame = 1

    def draw(self):
        self.image.clip_draw(self.frame * int(250 / 3), 0, int(250 / 3), 100, self.x, self.y, 100, 250)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y += self.V / 10000
        self.frame = (self.frame + 1) % 3

    def GetVelocity(self, V):
        self.V = V
        pass

    def get_bb(self):
        return self.x - 35, self.y - 30, self.x + 35, self.y + 30

    def handle_collision(self, group, other):
        pass

    def delete(self):
        if self.y < -100:
            game_world.remove_object(self)
