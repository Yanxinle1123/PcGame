from tkinter import Button


class PcButton:
    def __init__(self, canvas, button_text_size, continue_button_text_color, pause_button_text_color):
        self._canvas = canvas
        self._button_text_size = button_text_size

        self._start_button = None
        self._start_width = None
        self._start_height = None
        self._start_command = None

        self._close_button = None
        self._close_width = None
        self._close_height = None
        self._close_command = None

        self._paused_button = None
        self._paused_width = None
        self._paused_height = None
        self._paused_command = None
        self._pause_button_text_color = pause_button_text_color

        self._continue_button = None
        self._continue_width = None
        self._continue_height = None
        self._continue_command = None
        self._continue_button_text_color = continue_button_text_color

        self._set_up_button = None
        self._set_up_width = None
        self._set_up_height = None
        self._set_up_command = None

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
