import typing
from .game_component import GameComponent
from pyray import *

class PlayerComponent(GameComponent):

    _x: int
    _y: int
    _speed = 250
    _damage = 5

    def __init__(self, init_x: int, init_y: int) -> None:
        self._x = init_x
        self._y = init_y

    def update(self) -> typing.NoReturn:
        delta = get_frame_time()

        if is_key_down(KEY_A):
            self._x -= int(self._speed * delta)

        if is_key_down(KEY_D):
            self._x += int(self._speed * delta)

        if is_key_down(KEY_S):
            self._y += int(self._speed * delta)

        if is_key_down(KEY_W):
            self._y -= int(self._speed * delta)

    def render(self) -> typing.NoReturn:
        draw_rectangle(self._x, self._y, 96, 96, GREEN)
        