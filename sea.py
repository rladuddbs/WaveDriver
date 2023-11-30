from pico2d import load_image, load_music
from tkinter import *

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()


PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
MOVE_SPEED_KMPH = 20.0  # Km / Hour
MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)


class Sea:
    def __init__(self):
        self.image = load_image('sea.png')
        self.img1_y, self.img2_y = monitor_height / 2, monitor_height
        self.V = 0
        self.move_lenth = 0



    def draw(self):
        self.image.clip_draw(0, 0, 1980, 1080, monitor_width / 2,  self.img1_y, monitor_width, monitor_height)
        self.image.clip_draw(0, 0, 1980, 1080, monitor_width / 2,  self.img2_y, monitor_width, monitor_height)


    def update(self):
        self.img1_y += self.V / 10000
        self.img2_y += self.V / 10000
        if self.img1_y <= 0: self.img1_y = monitor_height
        if self.img2_y <= 0: self.img2_y = monitor_height
        self.move_lenth += self.V / 10000
        pass

    def GetVelocity(self, V):
        self.V = V
        pass
