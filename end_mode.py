from pico2d import load_image, get_events, clear_canvas, update_canvas, load_music, load_wav
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
    global click_sound, close_sound
    sea = Sea()
    game_world.add_object(sea)


    click_sound = load_wav('click.wav')
    close_sound = load_wav('close_click')
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
            close_sound.set_volume(32)
            close_sound.play()
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            animation_start = True
            click_sound.set_volume(32)
            click_sound.play()
    pass


def update():
    pass


def draw():
    pass

def pause():
    pass


def resume():
    pass

def Animation():
    pass