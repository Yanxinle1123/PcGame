from tkinter import Button


class PcButton:
    def __init__(self, canvas):
        self._canvas = canvas

        self._start_button = None
        self._start_width = None
        self._start_height = None

        self._close_button = None
        self._close_width = None
        self._close_height = None

        self._paused_button = None
        self._paused_width = None
        self._paused_height = None

        self._continue_button = None
        self._continue_width = None
        self._continue_height = None

        self._set_up_button = None
        self._set_up_width = None
        self._set_up_height = None

    def _draw_button(self):
        self._start_button = Button(self._canvas, text='开始', font=("Arial", button_text_size), fg='black',
                                    command=start_game)
        self._start_width = self._start_button.winfo_reqwidth()
        self._start_height = self._start_button.winfo_reqheight()

        close_button = Button(canvas, text='退出', font=("Arial", button_text_size), command=close_game)
        close_width = close_button.winfo_reqwidth()
        close_height = close_button.winfo_reqheight()

        pause_button = Button(canvas, text='暂停', font=("Arial", button_text_size), fg=pause_button_text_color,
                              command=pause_game)
        pause_width = pause_button.winfo_reqwidth()
        pause_height = pause_button.winfo_reqheight()

        continue_button = Button(canvas, text='继续', font=("Arial", button_text_size), fg=continue_button_text_color,
                                 command=continue_game)
        continue_width = continue_button.winfo_reqwidth()
        continue_height = continue_button.winfo_reqheight()

        set_up_button = Button(canvas, text='设置', font=("Arial", button_text_size), command=set_up)
        set_up_width = continue_button.winfo_reqwidth()
        set_up_height = continue_button.winfo_reqheight()

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
