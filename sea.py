import time

from pico2d import load_image, load_music
from tkinter import *

import play_mode

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

# 보트 가로 1.8M, 보트 세로 4.35M
PIXEL_PER_METER = (100 / 3)  # 100 pixel 3 M
MOVE_SPEED_KMPH = 10.0  # Km / Hour
MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)  # m / min
MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)  # m / s
MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)


class Sea:
    def __init__(self):
        self.image = load_image('sea.png')
        self.img1_y, self.img2_y = monitor_height / 2, monitor_height
        self.V = 0
        self.move_stone_lenth = 0
        self.move_arrow_lenth = 0
        self.move_lenth = 0
    def draw(self):
        self.image.clip_draw(0, 0, 1980, 1080, monitor_width / 2,  self.img1_y, monitor_width, monitor_height)
        self.image.clip_draw(0, 0, 1980, 1080, monitor_width / 2,  self.img2_y, monitor_width, monitor_height)

    def update(self):
        self.img1_y += self.V / 10000
        self.img2_y += self.V / 10000
        if self.img1_y <= 0: self.img1_y = monitor_height
        if self.img2_y <= 0: self.img2_y = monitor_height
        self.move_stone_lenth += self.V / 10000
        self.move_arrow_lenth += self.V / 10000
        self.move_lenth -= self.V / 100000

    def GetVelocity(self, V):
        self.V = V
        pass

