from pico2d import *
import end_mode as start_mode
# import play_mode as start_mode
# import title_mode as start_mode

import game_framework
from tkinter import Tk

from BGM import BGM

root = Tk()

bgm = BGM()
monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

open_canvas(monitor_width, monitor_height)
bgm.make_bgm()

game_framework.run(start_mode)
close_canvas()
