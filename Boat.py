from pico2d import *
from tkinter import *
import time

import play_mode

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()



class Boat:

    def __init__(self):
        self.image = load_image('boat_animation.png')
        self.frame = 0
        self.mx = 0
        self.my = 0
        self.click = False
        self.boat_x, self.boat_y = monitor_width / 2, 200
        self.dir = 1
        self.V = 0
        self.angle = 0
        self.Durability = 3
        self.paddling = load_wav('paddle_sound.wav')
        self.last_frame = 0
        self.broken_sound = load_wav('wounded .wav')
        self.invincibility = False
        self.alpha = 1
        self.frame_time = 0
        self.alpha_interval = 0.5  # 알파값 변경 간격
        self.alpha_duration = 2.0  # 알파값 유지 시간
        self.last_time = time.time()
    def draw(self):
        if self.mx >= monitor_width / 2:
            self.image.clip_composite_draw(400 * self.frame, 0, 400, 400, -self.angle, ' ', self.boat_x, self.boat_y, 200, 200)
            self.dir = 1
        else:
            self.image.clip_composite_draw(400 * self.frame, 0, 400, 400, -self.angle, 'h', self.boat_x, self.boat_y, 200, 200)
            self.dir = -1

        self.boat_x += self.V / 2000
        draw_rectangle(*self.get_bb())

    def GetClickImpo(self, click, mx, my):
        self.click = click
        self.mx, self.my = mx, my

    def GetMousePos(self, mx, my):
        self.mx, self.my = mx, my

    def move(self):
        pass

    def update(self):
        if not self.click:
            self.frame = 0
        else:
            if self.my > monitor_height / 3 * 2:
                self.frame = 0
                self.last_frame = self.frame
            elif monitor_height / 3 * 2 > self.my > monitor_height / 3:
                self.frame = 1
            elif monitor_height / 3 > self.my > 0:
                self.frame = 2

            if self.frame == 2 and self.last_frame == 0:
                self.paddling.set_volume(60)
                self.paddling.play()
                self.last_frame = 2

        if self.invincibility:
            current_time = time.time()
            self.frame_time += current_time - self.last_time
            self.last_time = current_time

            if self.frame_time >= self.alpha_duration:
                self.invincibility = False
                self.alpha = 0.5
                self.frame_time = 0

            if self.frame_time <= self.alpha_duration:
                if self.frame_time % self.alpha_interval <= self.alpha_interval / 2:
                    self.alpha = 1
                else:
                    self.alpha = 0.5

        self.image.opacify(self.alpha)


    def GetBoatImpo(self, V, add_angle):
        self.V = V
        if -0.5 < self.angle < 0.5:
            save_angle = self.angle
            self.angle += add_angle / 500
            if -0.5 > self.angle or self.angle > 0.5:
                self.angle = save_angle



    def GetVelocity(self, V):
        pass

    def get_bb(self):
        return self.boat_x - 30, self.boat_y - 70, self.boat_x + 30, self.boat_y + 75

    def handle_collision(self, group, other):
        if group == 'boat:stone':
            self.Durability -= 1
            self.broken_sound.set_volume(40)
            self.broken_sound.play()
            self.invincibility = True
            self.last_time = time.time()
            self.frame_time = 0
            play_mode.y_speed = play_mode.y_speed / 2

        if group == 'boat:arrow':
            self.Durability -= 1
            self.broken_sound.set_volume(40)
            self.broken_sound.play()
            self.invincibility = True
            self.last_time = time.time()
            self.frame_time = 0
            play_mode.y_speed = play_mode.y_speed * 2
