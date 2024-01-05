""" hurdle

    ハードルのモジュール
"""
# ハードル画像を取得するために使用
from image_dict import IMAGE_DICT
# 座標を表現するために使用
from point import Point
# ゲーム画面の幅と高さに依存する定数を定義するために使用
from game_settings import WIDTH, HEIGHT

class Hurdle:
    # ハードルの移動速度
    speed = 8

    def __init__(self, image_key):
        self.image = IMAGE_DICT[image_key]
        self.left_top_point = Point(WIDTH, HEIGHT*3/7 + IMAGE_DICT['run1'].get_height() - self.image.get_height())  
        # 画像の幅
        self.width = self.image.get_width()
        # 画像の高さ
        self.height = self.image.get_height()
        # 画像の右下の座標。衝突判定に使用する。
        self.right_bottom_point = Point(
            self.left_top_point.x + self.width, self.left_top_point.y + self.height)

    def move(self):
        # ハードルのxの座標をspeed分動かす。
        self.left_top_point.x -= self.speed
        # 衝突検知のためのハードル画像の右下座標を更新する
        self.right_bottom_point.x = self.left_top_point.x + self.width
