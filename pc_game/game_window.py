import tkinter as tk

from LeleEasyTkinter.easy_auto_window import EasyWindow

from pc_game.grade import Grade
from pc_game.music import Music
from pc_game.score import Score
from pc_game.seplit_line import SeplitLine


class GameWindow:
    def __init__(self):
        self.window = None
        self.grade = Grade()
        self.score = Score()
        self.balls = []
        self.seplit_line = SeplitLine()
        self.music = Music()
        self.buttons = []
        self.game_chars = []

    def _create_grade(self, ):
        # TODO : Complete method content
        pass

    def _create_score(self, ):
        # TODO : Complete method content
        pass

    def _create_game_char(self, ):
        # TODO : Complete method content
        pass

    def _create_ball(self, ):
        # TODO : Complete method content
        pass

    def _create_red_line(self, ):
        # TODO : Complete method content
        pass

    def _creat_button(self, ):
        # TODO : Complete method content
        pass

    def _play_music(self, ):
        # TODO : Complete method content
        pass

    def game_start(self):
        self.window = tk.Tk()
        EasyWindow(self.window, "PcGame window", False, False).auto_position()
        self.window.mainloop()
