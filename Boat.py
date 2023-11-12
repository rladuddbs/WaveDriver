from pico2d import *
from tkinter import *


root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()


class Boat:
    def __init__(self):
        self.image = load_image('boat_animation.png')
        self.frame = 0
        self.mx = 0
        self.my = 0
        self.click = False

    def draw(self):
        if self.mx >= monitor_width / 2:
            self.image.clip_draw(400 * self.frame, 0, 400, 400, monitor_width / 2, 200, 200, 200)
        else:
            self.image.clip_composite_draw(400 * self.frame, 0, 400, 400, 0, 'h', monitor_width / 2, 200, 200, 200)



    def GetClickImpo(self, click, mx, my):
        self.click = click
        self.mx, self.my = mx, my

    def update(self):
        if not self.click:
            self.frame = 0
        else:
            if self.my > monitor_height / 3 * 2:
                self.frame = 0
            elif monitor_height / 3 * 2 > self.my > monitor_height / 3:
                self.frame = 1
            elif monitor_height / 3 > self.my > 0:
                self.frame = 2

        print(self.click)
