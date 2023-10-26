from pico2d import *
from tkinter import *

from Boat import Boat
from Stone import Stone

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

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



