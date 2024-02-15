from comm.comm_draw import ball_first


class PcBall:
    def __init__(self, canvas, red_line_x1, red_line_y1, grade_map):
        self._canvas = canvas
        self._red_line_x1 = red_line_x1
        self._red_line_y1 = red_line_y1
        self._grade_map = grade_map
        self._ball_x1 = self._red_line_x1 // 2
        self._ball_y1 = self._red_line_y1 - 45
        self._ball_x1 = self._ball_x1 - 30 / 2
        self._ball = None

    def _draw_ball(self):
        self._ball = ball_first(self._canvas, self._grade_map["ball_color"], self._ball_x1, self._ball_y1)

    def _get_color(self, ):
        # TODO : Complete method content
        pass

    def _ball_to(self, ):
        # TODO : Complete method content
        pass

    def _change_ball_color(self, color_name):
        # TODO : Complete method content
        pass

    def get_ball_color(self, ):
        # TODO : Complete method content
        pass
