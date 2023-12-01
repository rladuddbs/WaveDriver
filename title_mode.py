from pico2d import load_image, get_events, clear_canvas, update_canvas, load_music
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE

import game_framework
import game_world
import play_mode
from boat import Boat
from sea import Sea

from tkinter import *

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

def init():
    global sea, image, boat, boat_x, boat_y, spd
    sea = Sea()
    game_world.add_object(sea)

    boat = Boat()
    game_world.add_object(boat)

    boat_x, boat_y = monitor_width / 2, -100
    spd = 0.5
    pass


def finish():
    pass

animation_start = False

def handle_events():
    global animation_start
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            animation_start = True
    pass


def update():
    global boat_y, animation_start, spd
    if animation_start:
        boat_y += spd
        spd -= 0.0004
    if boat_y >= 200:
        game_framework.change_mode(play_mode)
    pass


def draw():
    global boat_x, boat_y
    clear_canvas()
    sea.image.clip_draw(0, 0, 1980, 1080, monitor_width / 2, monitor_height / 2, monitor_width, monitor_height)

    boat.image.clip_draw(0, 0, 400, 400, boat_x, boat_y, 200, 200)
    update_canvas()
    print(boat_y)
    pass

def pause():
    pass


def resume():
    pass

def Animation():
    pass