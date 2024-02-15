import tkinter as tk

from LeleEasyTkinter.easy_auto_window import EasyWindow

from pc_game.ball import Ball
from pc_game.grade import Grade
from pc_game.music import Music
from pc_game.red_line import RedLine
from pc_game.score import Score
from pc_game.seplit_line import SeplitLine


class GameWindow:
    def __init__(self):
        self._ball = None
        self._canvas = None
        self._window = None
        self._grade = Grade()
        self._score = Score()
        self._balls = []
        self._seplit_line = SeplitLine()
        self._music = Music()
        self._buttons = []
        self._game_chars = []
        self._yellow = 'green'
        self._letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        self._rainbow = f'red,blue,{self._yellow}'
        self._two_color = "red,blue"
        self._button_color = 'lower'

        self._lower_list = [
            {"move_char_time_ms": 20, "other_char": 0, "gen_char_time_ms": 500,
             "ball_color": "red", "char_color": "red"},  # 第 1 关
            {"move_char_time_ms": 15, "other_char": 0, "gen_char_time_ms": 500,
             "ball_color": "red", "char_color": "red"},  # 第 2 关
            {"move_char_time_ms": 10, "other_char": 0, "gen_char_time_ms": 600,
             "ball_color": "blue", "char_color": "blue"},  # 第 3 关
            {"move_char_time_ms": 20, "other_char": 2, "gen_char_time_ms": 400,
             "ball_color": "green", "char_color": self._yellow},  # 第 4 关
            {"move_char_time_ms": 20, "other_char": 2, "gen_char_time_ms": 300,
             "ball_color": "red", "char_color": self._two_color},  # 第 5 关
            {"move_char_time_ms": 20, "other_char": 5, "gen_char_time_ms": 200,
             "ball_color": "red", "char_color": self._rainbow},  # 第 6 关
            {"move_char_time_ms": 10, "other_char": 3, "gen_char_time_ms": 200,
             "ball_color": self._yellow, "char_color": f"{self._yellow},red"},  # 第 7 关
            {"move_char_time_ms": 20, "other_char": 3, "gen_char_time_ms": 400,
             "ball_color": "blue", "char_color": self._rainbow},  # 第 8 关
            {"move_char_time_ms": 15, "other_char": 5, "gen_char_time_ms": 300,
             "ball_color": self._yellow, "char_color": self._rainbow},  # 第 9 关
            {"move_char_time_ms": 10, "other_char": 8, "gen_char_time_ms": 250,
             "ball_color": "red", "char_color": self._rainbow},  # 第 10 关
        ]

        self._medium_list = [
            {"move_char_time_ms": 15, "other_char": 2, "gen_char_time_ms": 400,
             "ball_color": "red", "char_color": "red"},  # 第 1 关
            {"move_char_time_ms": 10, "other_char": 2, "gen_char_time_ms": 500,
             "ball_color": "red", "char_color": "red"},  # 第 2 关
            {"move_char_time_ms": 10, "other_char": 2, "gen_char_time_ms": 500,
             "ball_color": "blue", "char_color": "blue"},  # 第 3 关
            {"move_char_time_ms": 15, "other_char": 2, "gen_char_time_ms": 400,
             "ball_color": "green", "char_color": self._yellow},  # 第 4 关
            {"move_char_time_ms": 15, "other_char": 2, "gen_char_time_ms": 300,
             "ball_color": "red", "char_color": self._two_color},  # 第 5 关
            {"move_char_time_ms": 15, "other_char": 5, "gen_char_time_ms": 200,
             "ball_color": "red", "char_color": self._rainbow},  # 第 6 关
            {"move_char_time_ms": 10, "other_char": 3, "gen_char_time_ms": 200,
             "ball_color": self._yellow, "char_color": f"{self._yellow},red"},  # 第 7 关
            {"move_char_time_ms": 15, "other_char": 3, "gen_char_time_ms": 400,
             "ball_color": "blue", "char_color": self._rainbow},  # 第 8 关
            {"move_char_time_ms": 10, "other_char": 5, "gen_char_time_ms": 300,
             "ball_color": self._yellow, "char_color": self._rainbow},  # 第 9 关
            {"move_char_time_ms": 10, "other_char": 8, "gen_char_time_ms": 250,
             "ball_color": "red", "char_color": self._rainbow},  # 第 10 关
        ]

        self._advanced_list = [
            {"move_char_time_ms": 15, "other_char": 5, "gen_char_time_ms": 400,
             "ball_color": "red", "char_color": "red"},  # 第 1 关
            {"move_char_time_ms": 10, "other_char": 5, "gen_char_time_ms": 500,
             "ball_color": "red", "char_color": "red"},  # 第 2 关
            {"move_char_time_ms": 10, "other_char": 5, "gen_char_time_ms": 500,
             "ball_color": "blue", "char_color": "blue"},  # 第 3 关
            {"move_char_time_ms": 15, "other_char": 7, "gen_char_time_ms": 400,
             "ball_color": "green", "char_color": self._yellow},  # 第 4 关
            {"move_char_time_ms": 15, "other_char": 7, "gen_char_time_ms": 300,
             "ball_color": "red", "char_color": self._two_color},  # 第 5 关
            {"move_char_time_ms": 15, "other_char": 10, "gen_char_time_ms": 200,
             "ball_color": "red", "char_color": self._rainbow},  # 第 6 关
            {"move_char_time_ms": 10, "other_char": 8, "gen_char_time_ms": 200,
             "ball_color": self._yellow, "char_color": f"{self._yellow},red"},  # 第 7 关
            {"move_char_time_ms": 15, "other_char": 8, "gen_char_time_ms": 400,
             "ball_color": "blue", "char_color": self._rainbow},  # 第 8 关
            {"move_char_time_ms": 10, "other_char": 10, "gen_char_time_ms": 300,
             "ball_color": self._yellow, "char_color": self._rainbow},  # 第 9 关
            {"move_char_time_ms": 10, "other_char": 8, "gen_char_time_ms": 200,
             "ball_color": "red", "char_color": self._rainbow},  # 第 10 关
        ]
        self._grade = 0
        self._what_list = self._lower_list
        self._grade_map = self._what_list[self._grade]

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
                                 adjust_y=False).auto_position()

        self._canvas = tk.Canvas(self._window, width=easy_window.get_window_width(),
                                 height=easy_window.get_window_height())
        self._canvas.pack()
        red_line = RedLine(self._window, self._canvas, easy_window.get_window_height(), easy_window.get_window_width())
        red_line.draw_red_lines()
        self._ball = Ball(self._canvas, red_line.get_red_line_x1(), red_line.get_red_line_y1(), self._grade_map)
        self._ball.draw_ball()
        self._window.mainloop()
