from pico2d import *
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

class Stone:
    def __init__(self):
        self.image = load_image('stone.png')

    def draw(self):
        self.image.clip_draw(0, 0, 300, 300, monitor_width / 2, 800, 200, 200)


open_canvas(monitor_width, monitor_height)
boat = Boat()
stone = Stone()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, monitor_height - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()


while True:
    clear_canvas()
    handle_events()
    boat.update()
    boat.draw()
    stone.draw()
    delay(0.1)
    update_canvas()



