from pico2d import load_image
from tkinter import *

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()
class Sea:
    def __init__(self):
        self.image = load_image('sea.png')

    def draw(self):
        self.image.draw(monitor_width / 2, monitor_height / 2)

    def update(self):
        pass
