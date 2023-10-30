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


def handle_events():
    global mx, my, running

    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            mx, my = event.x, monitor_height - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()
            running = False


def create_world():
    global boat
    global stone
    global sea
    global cursor

    sea = Sea()
    GameWorld.add_object(sea)

    boat = Boat()
    GameWorld.add_object(boat)

    stone = Stone()
    GameWorld.add_object(stone)

    cursor = load_image('paddle.png')


def render_world():
    clear_canvas()
    GameWorld.render()
    cursor.draw(mx, my)
    update_canvas()


hide_cursor()
create_world()
running = True

while running:
    handle_events()
    GameWorld.update()
    render_world()
    delay(0.1)
