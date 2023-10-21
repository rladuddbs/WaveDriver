from pico2d import *

class Boat:
    def __init__(self):
        self.image = load_image('boat.png')

    def draw(self):
        self.image.clip_draw(0, 0, 500, 500, 600, 200, 150, 150)

    def update(self):
        pass

open_canvas(1200, 800)
boat = Boat()

while True:
    clear_canvas()
    boat.draw()
    update_canvas()

close_canvas()
