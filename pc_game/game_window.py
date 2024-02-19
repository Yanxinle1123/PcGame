import tkinter as tk
import tkinter.font as tkfont
from tkinter import Label, Button, HORIZONTAL, Scale

import pygame
from LeleEasyTkinter.easy_auto_window import EasyWindow

from pc_game.ball import PcBall
from pc_game.button import PcButton
from pc_game.grade import PcGrade
from pc_game.music import PcMusic
from pc_game.red_line import PcRedLine
from pc_game.score import PcScore
from pc_game.seplit_line import PcSeplitLine


class PcGameWindow:
    def __init__(self):
        self._ball_speed_label_width = None
        self._ball_speed_label_x = None
        self._ball_speed = None
        self._ball_speed_label_font = None
        self._scale_self = None
        self._ball_speed_function = None
        self._ball_speed_label = None
        self._screen_width = None
        self._screen_height = None
        self._if_pause_game = None
        self._if_start_game = None
        self._is_continue = None
        self._number2 = None
        self._set_up_button = None
        self._easy_window = None
        self._red_line = None
        self._ball = None
        self._button = None
        self._canvas = None
        self._window = None
        self._grade = PcGrade()
        self._score = PcScore()
        self._balls = []
        self._seplit_line = PcSeplitLine()
        self._music = PcMusic()
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

    def start_game(self):
        #
        pass

    def close_games(self):
        #
        pass

    def pause_games(self):
        #
        pass

    def continue_game(self):
        #
        pass

    def generate_and_move(self):
        #
        pass

    def _on_close(self):
        # quit_music()
        # win.destroy()
        self._window.destroy()

    #
    def _close_game(self):
        self._on_close()

    # def set_up(self):
    #
    #     # TODO document why this method is empty
    #     pass

    def set_up(self):
        if self._button.get_set_up_button().cget('fg') != 'gray' and self._number2 % 2 == 0:
            self._button.get_set_up_button().config(fg='gray')
            self._is_continue = False
            pygame.mixer.music.unpause()

            def quit_set_up():
                if self._if_start_game and self._if_pause_game:
                    pygame.mixer.music.pause()
                    pygame.mixer.music.set_volume(volume_var)
                    self._is_continue = False
                if self._if_start_game and not self._if_pause_game:
                    self._is_continue = True
                    self.generate_and_move()
                new_window.destroy()
                self._button.get_set_up_button().config(fg='black')
                self._number2 += 1

            def on_scale_changed(value):
                # 将滑块值转换为音量（0 到 1 之间的浮点数）
                volume_var2 = float(value) / 10

                # 更新 Pygame 混音器的音量
                pygame.mixer.music.set_volume(volume_var2)

            def ball_speed_function(value):
                self._ball_speed = int(value) + 8

            def this_lower_list():
                self._grade_map = self._what_list[self._grade]
                lower_game_button.config(fg='red')
                medium_game_button.config(fg='black')
                advanced_game_button.config(fg='black')
                self._button_color = 'lower'

            def this_medium_list():
                self._what_list = self._medium_list
                self._grade_map = self._what_list[self._grade]
                lower_game_button.config(fg='black')
                medium_game_button.config(fg='red')
                advanced_game_button.config(fg='black')
                self._button_color = 'medium'

            def this_advanced_list():
                self._what_list = self._advanced_list
                self._grade_map = self._what_list[self._grade]
                lower_game_button.config(fg='black')
                medium_game_button.config(fg='black')
                advanced_game_button.config(fg='red')
                self._button_color = 'advanced'

            def button_color_function():
                if self._button_color == 'lower':
                    lower_game_button.config(fg='red')
                elif self._button_color == 'medium':
                    medium_game_button.config(fg='red')
                else:
                    advanced_game_button.config(fg='red')

            volume_var = round(pygame.mixer.music.get_volume(), 1) * 10

            new_window = tk.Toplevel(self._window)
            new_window.title("设置")
            new_window.protocol("WM_DELETE_WINDOW", quit_set_up)
            new_window.resizable(False, False)
            new_window.update_idletasks()

            new_window_height = int(self._screen_height * 0.75)
            new_window_width = int(self._screen_width * 0.3)
            new_window_x = self._screen_width // 2 - new_window_width // 2
            new_window_y = self._screen_height // 2 - new_window_height // 2
            new_window.geometry(f'{new_window_width}x{new_window_height}+{new_window_x}+{new_window_y}')

            music_label = Label(new_window, text='音乐音量', font=('Arial', 20))
            music_label_height = music_label.winfo_reqheight()
            # print(f"music_label_width={music_label_width}|music_label_height={music_label_height}")

            scale_len = int(new_window_width * 0.95)
            scale_width = 40
            scale_height = 20

            scale_music = Scale(new_window, from_=0, to=10, orient=HORIZONTAL,
                                length=scale_len, sliderlength=scale_width, width=scale_width,
                                command=on_scale_changed)
            scale_music_length = scale_music.cget("length")
            scale_music_width = scale_music.cget("width")
            # print(f"scale_music_length={scale_music_length}|scale_music_width={scale_music_width}")
            scale_music_x = new_window_width // 2 - scale_music_length // 2
            scale_music_y = music_label_height + scale_height
            scale_music.set(volume_var)
            scale_music.place(x=scale_music_x, y=scale_music_y)

            self._ball_speed_label = Label(new_window, text='球的速度', font=('Arial', 20))
            self._scale_self._ball_speed = Scale(new_window, from_=1, to=10, orient=HORIZONTAL,
                                                 length=scale_len, sliderlength=scale_width, width=scale_width,
                                                 command=ball_speed_function)
            # print(f"self._scale_self._ball_speed_length={self._scale_self._ball_speed_length}|self._scale_self._ball_speed_width={self._scale_self._ball_speed_width}")
            self._scale_self._ball_speed_x = scale_music_x
            self._scale_self._ball_speed_y = scale_music_y + scale_music_width + music_label_height + scale_height * 3
            self._scale_self._ball_speed.place(x=self._scale_self._ball_speed_x, y=self._scale_self._ball_speed_y)

            game_difficult_label = Label(new_window, text='游戏难度', font=('Arial', 20))

            lower_game_button = Button(new_window, text='低等难度', font=('Arial', 50), command=this_lower_list)
            medium_game_button = Button(new_window, text='中等难度', font=('Arial', 50), command=this_medium_list)
            advanced_game_button = Button(new_window, text='高等难度', font=('Arial', 50),
                                          command=this_advanced_list)

            lower_game_button_width = lower_game_button.winfo_reqwidth()
            medium_game_button_width = medium_game_button.winfo_reqwidth()
            advanced_game_button_width = advanced_game_button.winfo_reqwidth()
            lower_game_button_x = new_window_width // 2 - lower_game_button_width // 2
            medium_game_button_x = new_window_width // 2 - medium_game_button_width // 2
            advanced_game_button_x = new_window_width // 2 - advanced_game_button_width // 2

            # music_label_width = music_label.winfo_width()
            music_label_font = tkfont.Font(font=music_label['font'])
            music_label_width = music_label_font.measure('音乐音量 ')
            self._ball_speed_label_font = tkfont.Font(font=music_label['font'])
            self._ball_speed_label_width = self._ball_speed_label_font.measure('球的速度 ')
            that_list_label_font = tkfont.Font(font=game_difficult_label['font'])
            that_list_label_width = that_list_label_font.measure('游戏难度 ')

            quit_button = Button(new_window, text='退出设置', font=('Arial', 50), command=quit_set_up)
            quit_button_width = quit_button.winfo_reqwidth()
            quit_button_height = quit_button.winfo_reqheight()
            quit_button_x = new_window_width // 2 - quit_button_width // 2
            quit_button_y = new_window_height - (quit_button_height + quit_button_height // 2)
            quit_button.place(x=quit_button_x, y=quit_button_y)

            # 使用 Font 对象的 metrics() 方法获取 Label 的高度
            music_label_height = music_label_font.metrics("linespace")
            music_label_x = new_window_width // 2 - music_label_width // 2
            self._ball_speed_label_x = new_window_width // 2 - self._ball_speed_label_width // 2
            music_label_y = music_label_height
            that_list_label_x = new_window_width // 2 - that_list_label_width // 2
            music_label.place(x=music_label_x, y=music_label_y)
            self._ball_speed_label.place(x=self._ball_speed_label_x, y=150)
            self._scale_self._ball_speed.set(self._ball_speed - 8)
            game_difficult_label.place(x=that_list_label_x, y=280)
            lower_game_button.place(x=lower_game_button_x, y=350)
            medium_game_button.place(x=medium_game_button_x, y=450)
            advanced_game_button.place(x=advanced_game_button_x, y=550)
            button_color_function()
            self._number2 += 1

    def _create_grade(self):
        # TODO : Complete method content
        pass

    def _create_score(self):
        # TODO : Complete method content
        pass

    def _create_game_char(self):
        # TODO : Complete method content
        pass

    def _create_ball(self):
        self._ball = PcBall(self._canvas, self._red_line.get_red_line_x1(), self._red_line.get_red_line_y1(),
                            self._grade_map)
        self._ball.draw_ball()

    def _create_red_line(self):
        self._red_line = PcRedLine(self._window, self._canvas, self._easy_window.get_window_height(),
                                   self._easy_window.get_window_width())
        self._red_line.draw_red_lines()

    def _creat_button(self):
        self._button = PcButton(self._canvas, 50, "black",
                                "grey", self._easy_window.get_window_width(), self._red_line.get_red_line_y0(),
                                self.start_game, self.close_games, self.pause_games, self.continue_game,
                                self.set_up)

    def _play_music(self):
        # TODO : Complete method content
        pass

    def get_tk_window(self):
        return self._window

    def layout(self):
        self._create_red_line()
        self._create_ball()
        self._creat_button()

    def game_start(self):
        self._window = tk.Tk()

        self._easy_window = EasyWindow(self._window, window_title="PcGame window", adjust_x=False,
                                       adjust_y=False).auto_position()

        self._canvas = tk.Canvas(self._window, width=self._easy_window.get_window_width(),
                                 height=self._easy_window.get_window_height())
        self._canvas.pack()

        self.layout()

        self._window.mainloop()
