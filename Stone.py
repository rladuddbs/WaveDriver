from pico2d import load_image

from WaveDriver import monitor_width


class Stone:
    def __init__(self):
        self.image = load_image('stone.png')

    def draw(self):
        self.image.clip_draw(0, 0, 300, 300, monitor_width / 2, 800, 200, 200)
