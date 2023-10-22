from pico2d import *

class Boat:
    def __init__(self):
        self.image = load_image('boat_animation.png')
        self.frame = 0

    def draw(self):
        self.image.clip_draw(400 * self.frame, 0, 400, 400, 600, 400, 200, 200)

    def update(self):
        self.frame = (self.frame + 1) % 3

open_canvas(1200, 800)
boat = Boat()

while True:
    clear_canvas()
    boat.update()
    boat.draw()
    delay(0.1)
    update_canvas()


close_canvas()
