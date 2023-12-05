from pico2d import load_image, get_events, clear_canvas, update_canvas, load_music, load_wav, load_font, draw_rectangle
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT, \
    SDL_MOUSEBUTTONUP

import game_framework
import game_world
import play_mode
import title_mode
from sea import Sea

from tkinter import *

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

mx, my = 0, 0

def init():
    global click_sound, close_sound, sea, main, exit, font, mx, my, mouse_frame, cursor
    sea = Sea()
    game_world.add_object(sea)

    click_sound = load_wav('click.wav')
    close_sound = load_wav('close_click.wav')
    main = load_image('main.png')
    exit = load_image('exit.png')

    font = load_font('esamanru Bold.ttf', 100)

    cursor = load_image('paddle.png')
    mouse_frame = 0

def finish():
    pass


def handle_events():
    global animation_start, mx, my, mouse_frame
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_sound.set_volume(32)
            close_sound.play()
            game_framework.quit()

        if event.type == SDL_MOUSEMOTION:
            mx, my = event.x, monitor_height - 1 - event.y

        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            mouse_frame = 1
            if monitor_width / 2 + 350 - 100 < mx < monitor_width / 2 + 350 + 100 and monitor_height / 2 - 250 - 50 < my < monitor_height / 2 - 250 + 50:
                close_sound.set_volume(32)
                close_sound.play()
                game_framework.quit()

            if monitor_width / 2 - 350 - 100 < mx < monitor_width / 2 - 350 + 100 and monitor_height / 2 - 250 - 50 < my < monitor_height / 2 - 250 + 50:
                title_mode.boat_y = -100
                title_mode.animation_start = False
                click_sound.set_volume(32)
                click_sound.play()
                game_framework.change_mode(title_mode)


        if event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:
            frame = 0
            mouse_frame = 0
    pass


def update():
    pass

def draw():
    global title_pos, sea, main, exit, font
    clear_canvas()
    sea.image.clip_draw(0, 0, 1980, 1080, monitor_width / 2, monitor_height / 2, monitor_width, monitor_height)

    main.draw(monitor_width / 2 - 350, monitor_height / 2 - 250)
    exit.draw(monitor_width / 2 + 350, monitor_height / 2 - 250)
    font.draw(monitor_width / 2 - 450, monitor_height / 2 + 100, f'score : {int(play_mode.sea.move_lenth)} M', (0, 0, 0))

    if mx >= monitor_width / 2:
        cursor.clip_draw(mouse_frame * 100, 0, 100, 100, mx, my)
    else:
        cursor.clip_composite_draw(mouse_frame * 100, 0, 100, 100, 0, 'h', mx, my, 100, 100)

    # draw_rectangle(monitor_width / 2 + 350 - 100, monitor_height / 2 - 250 - 50, monitor_width / 2 + 350 + 100, monitor_height / 2 - 250 + 50)
    # draw_rectangle(monitor_width / 2 - 350 - 100, monitor_height / 2 - 250 - 50, monitor_width / 2 - 350 + 100, monitor_height / 2 - 250 + 50)
    update_canvas()
    pass

def pause():
    pass

def resume():
    pass

def Animation():
    pass