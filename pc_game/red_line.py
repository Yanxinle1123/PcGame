class RedLine:
    def __init__(self, window, canvas):
        self._window = window
        self._canvas = canvas
        self._window_height = self._window.winfo_height()
        self._window_width = self._window.winfo_width()
        self._red_line_height = 20
        self._red_line_x0 = 0
        self._red_line_y0 = self._window_height - 80
        self._red_line_x1 = self._window_width
        self._red_line_y1 = self._red_line_y0
        self._red_line = None

    def draw_red_lines(self):
        self._red_line = self._canvas.create_line(self._red_line_x0, self._red_line_y0, self._red_line_x1,
                                                  self._red_line_y1, fill='red',
                                                  width=self._red_line_height)
