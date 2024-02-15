from tkinter import Button


class PcButton:
    def __init__(self, canvas, button_text_size, continue_button_text_color, pause_button_text_color, window_width,
                 red_line_y0, start_command=None, close_command=None, paused_command=None, continue_command=None,
                 set_up_command=None, ):
        self._red_line_y0 = red_line_y0
        self._window_width = window_width
        self._canvas = canvas
        self._button_text_size = button_text_size

        self._start_button = None
        self._start_width = None
        self._start_height = None
        self._start_command = start_command

        self._close_button = None
        self._close_width = None
        self._close_height = None
        self._close_command = close_command

        self._paused_button = None
        self._paused_width = None
        self._paused_height = None
        self._paused_command = paused_command
        self._pause_button_text_color = pause_button_text_color

        self._continue_button = None
        self._continue_width = None
        self._continue_height = None
        self._continue_command = continue_command
        self._continue_button_text_color = continue_button_text_color

        self._set_up_button = None
        self._set_up_width = None
        self._set_up_height = None
        self._set_up_command = set_up_command

    def _draw_button(self):
        self._start_button = Button(self._canvas, text='开始', font=("Arial", self._button_text_size), fg='black',
                                    command=self._start_command)
        self._start_width = self._start_button.winfo_reqwidth()
        self._start_height = self._start_button.winfo_reqheight()

        self._close_button = Button(self._canvas, text='退出', font=("Arial", self._button_text_size),
                                    command=self._close_command)
        self._close_width = self._close_button.winfo_reqwidth()
        self._close_height = self._close_button.winfo_reqheight()

        self._pause_button = Button(self._canvas, text='暂停', font=("Arial", self._button_text_size),
                                    fg=self._pause_button_text_color,
                                    command=self._paused_command)
        self._pause_width = self._pause_button.winfo_reqwidth()
        self._pause_height = self._pause_button.winfo_reqheight()

        self._continue_button = Button(self._canvas, text='继续', font=("Arial", self._button_text_size),
                                       fg=self._continue_button_text_color,
                                       command=self._continue_command)
        self._continue_width = self._continue_button.winfo_reqwidth()
        self._continue_height = self._continue_button.winfo_reqheight()

        self._set_up_button = Button(self._canvas, text='设置', font=("Arial", self._button_text_size),
                                     command=self._set_up_command)
        self._set_up_width = self._continue_button.winfo_reqwidth()
        self._set_up_height = self._continue_button.winfo_reqheight()

        button_width_gap = 40
        button_height_gap = 22
        start_x = (self._window_width - self._start_width - button_width_gap - self._close_width - button_width_gap
                   - self._pause_width - button_width_gap - self._continue_width - button_width_gap - self._set_up_width) // 2
        start_y = self._red_line_y0 + button_height_gap

        close_x = start_x + self._start_width + button_width_gap
        close_y = start_y

        pause_x = close_x + self._close_width + button_width_gap
        pause_y = start_y

        continue_x = pause_x + self._pause_width + button_width_gap
        continue_y = start_y

        set_up_x = continue_x + self._continue_width + button_width_gap
        set_up_y = start_y

        self._start_button.place(x=start_x, y=start_y)
        self._close_button.place(x=close_x, y=close_y)
        self._pause_button.place(x=pause_x, y=pause_y)
        self._continue_button.place(x=continue_x, y=continue_y)
        self._set_up_button.place(x=set_up_x, y=set_up_y)

    def _get_x(self, ):
        # TODO : Complete method content
        pass

    def _get_y(self, ):
        # TODO : Complete method content
        pass

    def _make_font(self, fong_name, font_size):
        # TODO : Complete method content
        pass

    def _make_label(self, ):
        # TODO : Complete method content
        pass

    def _place(self, ):
        # TODO : Complete method content
        pass

    def _command(self, ):
        # TODO : Complete method content
        pass
