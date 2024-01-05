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
    speed = 8

    def __init__(self):
        print(self.speed)

    def move(self):
        pass
