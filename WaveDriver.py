from pico2d import *
from tkinter import *
import time
import GameWorld
import game_framework

from boat import Boat
from stone import Stone
from sea import Sea


root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

open_canvas(monitor_width, monitor_height)

global mx, my, click
x_speed = 0
y_speed = 0
dir = 0
angle = 0
def handle_events():
    global mx, my, running, click, x_speed, y_speed, dir

    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            mx, my = event.x, monitor_height - 1 - event.y
            boat.GetMousePos(mx, my)
            if my - current_my != 0 and frame_time != 0 and my < current_my and boat.click:
                dir = boat.dir

                if y_speed > (my - current_my) / frame_time:
                    y_speed = (my - current_my) / frame_time
                    x_speed = (my - current_my) / (frame_time * 10) * boat.dir


        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()
            running = False

        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            boat.GetClickImpo(True, mx, my)


        if event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:
            boat.GetClickImpo(False, mx, my)
            frame = 0



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

frame_time = 0.0
current_time = time.time()
current_my, my = 0, 0

while running:
    handle_events()
    current_my = my
    GameWorld.update()
    render_world()
    frame_time = time.time() - current_time
    current_time += frame_time

    if y_speed < 0: y_speed += 10
    if y_speed < -10000: y_speed = -10000

    #if -1000 > x_speed or x_speed > 1000: x_speed = -1000 * dir
    if dir == 1:
        if x_speed < 0:
            x_speed += 1 * dir
    else:
        if x_speed * dir < 0:
            x_speed += 1 * dir


    sea.GetVelocity(y_speed)
    boat.GetVelocity(x_speed)

    print(abs(x_speed * dir))






