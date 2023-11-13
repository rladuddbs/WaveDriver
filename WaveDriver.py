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
V = 1
accel = 10000
click = False
def handle_events():
    global mx, my, running, click, V, accel

    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            mx, my = event.x, monitor_height - 1 - event.y
            boat.GetMousePos(mx, my)

            if my - current_my != 0 and frame_time != 0 and my < current_my and boat.click:
                if V > (my - current_my) / frame_time:
                    V = (my - current_my) / frame_time

            print(V)


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

    if V < -10000: V = -10000
    if V < 0:
        V += 20

    sea.GetVelocity(V)






