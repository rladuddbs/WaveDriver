import random
import time
from tkinter import Tk

from pico2d import *
import game_framework
import game_world
from boat import Boat
from sea import Sea
from speed_up import Arrow
from stone import Stone


# Game object class here
root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()


global mx, my, click
x_speed = 0
y_speed = 0
dir = 0
add_angle = 0

running = True

frame_time = 0.0
current_time = time.time()
current_my, my = 0, 0

create_stone_lenth = random.randint(200, 2000)
create_arrow_lenth = random.randint(200, 2000)


def handle_events():
    global mx, my, running, click, x_speed, y_speed, dir, add_angle, mouse_frame, current_my, frame_time, paddling

    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            current_my = my
            mx, my = event.x, monitor_height - 1 - event.y
            boat.GetMousePos(mx, my)
            if my - current_my != 0 and frame_time != 0 and my < current_my and boat.click:
                dir = boat.dir
                if y_speed > (my - current_my) / frame_time:
                    y_speed = (my - current_my) / frame_time
                    x_speed = -400 * boat.dir
                    add_angle = ((my - current_my) / (frame_time * 10) * boat.dir) / 5000


        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            boat.GetClickImpo(True, mx, my)
            mouse_frame = 1

        if event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:
            boat.GetClickImpo(False, mx, my)
            frame = 0
            mouse_frame = 0

def init():
    global boat
    global stone
    global sea
    global cursor
    global mouse_frame
    global paddling
    hide_cursor()

    sea = Sea()
    game_world.add_object(sea)

    boat = Boat()
    game_world.add_object(boat)

    cursor = load_image('paddle.png')
    mouse_frame = 0

    game_world.add_collision_pair('boat:stone', boat, None)

def finish():
    game_world.clear()
    pass


def update():
    global current_my, current_time, y_speed, x_speed, frame_time

    frame_time = time.time() - current_time
    current_time += frame_time

    if y_speed < 0: y_speed += 10
    if y_speed < -10000: y_speed = -10000

    if dir == 1:
        if x_speed < 0:
            x_speed += 1 * dir
    else:
        if x_speed * dir < 0:
            x_speed += 1 * dir


    game_world.GetVelocity(y_speed)

    boat.GetBoatImpo(x_speed, add_angle)
    create_stone(create_stone_lenth)
    create_arrow(create_arrow_lenth)
    game_world.update()

    game_world.handle_collisions()


mx = 0
def draw():
    global mx
    clear_canvas()
    game_world.render()
    if mx >= monitor_width / 2:
        cursor.clip_draw(mouse_frame * 100, 0, 100, 100, mx, my)
    else:
        cursor.clip_composite_draw(mouse_frame * 100, 0, 100, 100, 0, 'h', mx, my, 100, 100)
    update_canvas()


def create_stone(lenth):
    global create_stone_lenth
    global stone
    if abs(sea.move_stone_lenth) > lenth:
        stone = Stone()
        game_world.add_object(stone)
        game_world.add_collision_pair('boat:stone', None, stone)
        lenth = random.randint(200, 1600)
        sea.move_stone_lenth = 0
        create_stone_lenth = lenth

def create_arrow(lenth):
    global create_arrow_lenth
    global arrow
    if abs(sea.move_arrow_lenth) > lenth:
        arrow = Arrow()
        game_world.add_object(arrow)
        game_world.add_collision_pair('boat:arrow', None, arrow)
        lenth = random.randint(200, 1600)
        sea.move_arrow_lenth = 0
        create_arrow_lenth = lenth

def pause():
    pass


def resume():
    pass