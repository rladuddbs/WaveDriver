from pico2d import load_image, get_events, clear_canvas, update_canvas, load_music
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE

import game_framework
import game_world
import play_mode
from sea import Sea

from tkinter import *

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

def init():
    global sea, image
    sea = Sea()
    game_world.add_object(sea)
    pass


def finish():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(play_mode)
    pass


def update():
    pass


def draw():
    clear_canvas()
    sea.image.clip_draw(0, 0, 1980, 1080, monitor_width / 2, monitor_height / 2, monitor_width, monitor_height)
    update_canvas()
    pass

def pause():
    pass


def resume():
    pass