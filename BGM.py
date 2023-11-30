from pico2d import load_music


class BGM:
    def __init__(self):
        self.bgm = None
        pass

    def make_bgm(self):
        self.bgm = load_music('BGM.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()
