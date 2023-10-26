from pico2d import load_image

from tkinter import *

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

class Boat:
    def __init__(self):
        self.image = load_image('boat_animation.png')
        self.frame = 0

    def draw(self):
        self.image.clip_draw(400 * self.frame, 0, 400, 400, monitor_width / 2, 200, 200, 200)

    def update(self):
        self.frame = (self.frame + 1) % 3
