from pico2d import *
from tkinter import *

import GameWorld

from boat import Boat
from stone import Stone
from sea import Sea

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

def create_world():
    global boat
    global stone
    global sea

    sea = Sea()
    GameWorld.add_object(sea)

    boat = Boat()
    GameWorld.add_object(boat)

    stone = Stone()
    GameWorld.add_object(stone)



def render_world():
    clear_canvas()
    GameWorld.render()
    update_canvas()

create_world()

while True:
    handle_events()
    GameWorld.update()
    render_world()
    delay(0.1)
