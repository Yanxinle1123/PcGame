import tkinter as tk

from LeleEasyTkinter.easy_auto_window import EasyWindow

from pc_game.grade import Grade
from pc_game.music import Music
from pc_game.score import Score
from pc_game.seplit_line import SeplitLine


class GameWindow:
    def __init__(self):
        self._window = None
        self._grade = Grade()
        self._score = Score()
        self._balls = []
        self._seplit_line = SeplitLine()
        self._music = Music()
        self._buttons = []
        self._game_chars = []

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

    def get_tk_window(self):
        return self._window

    def game_start(self):
        self._window = tk.Tk()
        easy_window = EasyWindow(self._window, window_title="PcGame window", adjust_x=False,
                                 adjust_y=False)
        easy_window.auto_position()
        tk.Canvas(self._window, width=easy_window.get_window_width(), height=easy_window.get_window_height()).pack()
        self._window.mainloop()
