import typing

from telegram import Game
from .game_component import GameComponent
from pyray import *


# I use it in case that the item does not have any texture yet
_FALLBACK_TEXTURE_COLOUR = RED

class ItemComponent(GameComponent):

    _x: int
    _y: int
    _texture: Texture2D

    def set_coords(self, new_x: int, new_y: int) -> typing.NoReturn:
        self._x = new_x
        self._y = new_y

    def __init__(self, texture_file_path: str) -> None:
        # Lets draw current game items outside of player's view, until
        # We know where the item room is
        self._x = -64
        self._y = -64

        if texture_file_path is not None:
            self._texture = load_texture(texture_file_path)
        else:
            self._texture = None


    def render(self) -> typing.NoReturn:
        if self._texture is not None:
            draw_texture(self._texture, self._x, self._y, RAYWHITE)
        else:
            draw_rectangle(self._x, self._y, 64, 64, _FALLBACK_TEXTURE_COLOUR)