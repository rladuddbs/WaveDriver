from pico2d import load_image
from tkinter import *

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()


# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
MOVE_SPEED_KMPH = 20.0  # Km / Hour
MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Sea:
    def __init__(self):
        self.image = load_image('sea.png')
        self.img1_y, self.img2_y = monitor_height / 2, monitor_height

    def draw(self):
        self.image.clip_draw(0, 0, 1980, 1080, monitor_width / 2,  self.img1_y, monitor_width, monitor_height)
        self.image.clip_draw(0, 0, 1980, 1080, monitor_width / 2,  self.img2_y, monitor_width, monitor_height)
        self.img1_y -= 1
        self.img2_y -= 1
        if self.img1_y <= 0: self.img1_y = monitor_height
        if self.img2_y <= 0: self.img2_y = monitor_height

    def update(self):
        pass
