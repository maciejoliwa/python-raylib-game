import typing

from .game_component import GameComponent
from pyray import *


# I use it in case that the item does not have any texture yet
_FALLBACK_TEXTURE_COLOUR = RED

class ItemComponent(GameComponent):

    _x: int
    _y: int
    _texture: Texture2D
    taken: bool = False

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


    def update(self, **kwargs) -> typing.NoReturn:
        player = kwargs["player"]  # We need a reference to player in order to check for collisions
        floor = kwargs["floor"]  # We need a reference to the floor in order to get data about the item rooom

        if self._x == -64 and self._y == -64 and not self.taken:
            for room in floor._rooms:
                if room["item_room"]:
                    self._x = room["x"]
                    self._y = room["y"]

        player_rec = Rectangle(player._x, player._y, 96, 96)
        item_rec = Rectangle(self._x, self._y, 64, 64)

        if check_collision_recs(player_rec, item_rec):
            self.taken = True
            self._x = -64
            self._y = -64

    def render(self) -> typing.NoReturn:
        if self._texture is not None:
            draw_texture(self._texture, self._x, self._y, RAYWHITE)
        else:
            draw_rectangle(self._x, self._y, 64, 64, _FALLBACK_TEXTURE_COLOUR)
