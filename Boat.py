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
        self.boat_x, self.boat_y = monitor_width / 2, 200
        self.dir = 1
        self.V = 0
        self.angle = 0
    def draw(self):
        if self.mx >= monitor_width / 2:
            self.image.clip_composite_draw(400 * self.frame, 0, 400, 400, -self.angle, ' ', self.boat_x, self.boat_y, 200, 200)
            self.dir = 1
        else:
            self.image.clip_composite_draw(400 * self.frame, 0, 400, 400, -self.angle, 'h', self.boat_x, self.boat_y, 200, 200)
            self.dir = -1

        self.boat_x += self.V / 10000

    def GetClickImpo(self, click, mx, my):
        self.click = click
        self.mx, self.my = mx, my

    def GetMousePos(self, mx, my):
        self.mx, self.my = mx, my

    def move(self):
        pass

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

    def GetBoatImpo(self, V, angle):
        self.V = V
        self.angle = angle
        pass



