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
    global sea, image, boat, boat_x, boat_y, spd, title_img, key_guide, alpha, apear, title_pos, title_acc, title_spd
    global click_sound
    sea = Sea()
    game_world.add_object(sea)

    boat = Boat()
    game_world.add_object(boat)

    boat_x, boat_y = monitor_width / 2, -100
    spd = 0.5

    title_img = load_image('title.png')
    title_pos = monitor_height / 2 + 150
    title_spd = -1
    title_acc = 0.005

    key_guide = load_image('key_guide.png')
    alpha = 1
    apear = 0.0025

    click_sound = load_wav('click.wav')
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
            click_sound.set_volume(32)
            click_sound.play()
    pass


def update():
    global boat_y, animation_start, spd, alpha, apear, title_acc, title_pos, title_spd
    if animation_start:
        boat_y += spd
        spd -= 0.0004

        title_pos += title_spd
        title_spd += title_acc
    if boat_y >= 200:
        game_framework.change_mode(play_mode)

    if not animation_start:
        if alpha >= 1:
            apear *= -1
        if alpha <= 0:
            apear *= -1
    else:
        apear = -abs(apear)

    if alpha < 0:
        alpha = 0
    alpha += apear

    key_guide.opacify(alpha)


def draw():
    global boat_x, boat_y, title_img, key_guide, title_pos
    clear_canvas()
    sea.image.clip_draw(0, 0, 1980, 1080, monitor_width / 2, monitor_height / 2, monitor_width, monitor_height)

    boat.image.clip_draw(0, 0, 400, 400, boat_x, boat_y, 200, 200)

    title_img.draw(monitor_width / 2, title_pos)
    key_guide.draw(monitor_width / 2, monitor_height / 2 - 250)
    update_canvas()
    pass

def pause():
    pass


def resume():
    pass

def Animation():
    pass