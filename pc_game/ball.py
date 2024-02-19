from comm.comm_draw import ball_first, contains_digit
from comm.common import rgb_to_hex


class PcBall:
    def __init__(self, canvas, red_line_x1, red_line_y1, grade_map, target_x=None, target_y=None, pixel=None,
                 sleep_ms=None, text=False):
        self._canvas = canvas
        self._red_line_x1 = red_line_x1
        self._red_line_y1 = red_line_y1
        self._grade_map = grade_map
        self._ball_x1 = self._red_line_x1 // 2
        self._ball_y1 = self._red_line_y1 - 45
        self._ball_x1 = self._ball_x1 - 30 / 2
        self._ball = None
        self._target_x = target_x
        self._target_y = target_y
        self._ball_color = self._grade_map["ball_color"]
        self._pixel = pixel
        self._sleep_ms = sleep_ms
        self._text = text

    def draw_ball(self):
        self._ball = ball_first(self._canvas, self._grade_map["ball_color"], self._ball_x1, self._ball_y1)

    def _get_color(self):
        return self._grade_map["ball_color"]

    def _ball_to(self):
        hex1 = self._ball_color
        num = contains_digit(hex1)
        if hex1[0] != '#' and num:
            hex1 = hex1.upper()
            hex2 = rgb_to_hex(hex1)
        else:
            hex2 = hex1

        ball_x2 = self._ball_x1 + 30
        ball_y2 = self._ball_y1 + 30
        # 画撞击的紫球
        purple_ball2 = self._canvas.create_oval(self._ball_x1, self._ball_y1, ball_x2, ball_y2, fill=hex2)

        # 计算紫球的中心坐标
        purple_center_x, purple_center_y = (self._ball_x1 + ball_x2) / 2, (self._ball_y1 + ball_y2) / 2

        # 定义移动紫球的函数
        text2 = self._text

        def move_purple_ball(purple_center_x, purple_center_y, text3=text2):
            # 计算与目标位置的剩余距离
            remaining_distance_x, remaining_distance_y = self._target_x - purple_center_x, self._target_y - purple_center_y

            # 使用线性插值算法计算移动步长
            lerp_factor = min(self._pixel / ((remaining_distance_x ** 2 + remaining_distance_y ** 2) ** 0.5), 1)
            move_dx = lerp_factor * remaining_distance_x
            move_dy = lerp_factor * remaining_distance_y

            # 移动紫球
            self._canvas.move(purple_ball2, move_dx, move_dy)

            # 更新紫球的中心坐标
            purple_center_x += move_dx
            purple_center_y += move_dy

            # 判断是否到达目标位置
            if lerp_factor == 1:
                self._canvas.delete(purple_ball2)
                if not text3:
                    return
                else:
                    self._canvas.delete(text3)
                    # 停止移动
                    return

            # 延迟一段时间后再次调用move_purple_ball()函数
            self._canvas.after(self._sleep_ms, move_purple_ball, purple_center_x, purple_center_y)

        # 调用move_purple_ball()函数，开始移动紫球
        move_purple_ball(purple_center_x, purple_center_y)

    def change_ball_color(self, color_name):
        self._ball.config(ball_color=color_name)

    def get_ball_color(self):
        return self._ball_color
