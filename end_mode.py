from pico2d import load_image, get_events, clear_canvas, update_canvas, load_music, load_wav, load_font
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
    global click_sound, close_sound, sea, main, exit, font
    sea = Sea()
    game_world.add_object(sea)

    click_sound = load_wav('click.wav')
    close_sound = load_wav('close_click.wav')
    main = load_image('main.png')
    exit = load_image('exit.png')

    font = load_font('esamanru Bold.ttf', 100)

def finish():
    pass


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
    global title_pos, sea, main, exit, font
    clear_canvas()
    sea.image.clip_draw(0, 0, 1980, 1080, monitor_width / 2, monitor_height / 2, monitor_width, monitor_height)

    main.draw(monitor_width / 2 - 350, monitor_height / 2 - 250)
    exit.draw(monitor_width / 2 + 350, monitor_height / 2 - 250)
    font.draw(monitor_width / 2 - 275, monitor_height / 2 + 100, f'score : {int(play_mode.sea.move_lenth)} M', (0, 0, 0))

    update_canvas()
    pass

def pause():
    pass

def resume():
    pass

def Animation():
    pass