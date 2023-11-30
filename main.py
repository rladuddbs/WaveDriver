from pico2d import *
import play_mode as start_mode
import game_framework
from tkinter import Tk
import title_mode as start_mode


root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

open_canvas(monitor_width, monitor_height)
game_framework.run(start_mode)
close_canvas()
