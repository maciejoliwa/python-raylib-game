import typing
import enum
from .game_component import GameComponent
from .room_component import RoomComponent
from pyray import *


class FloorLevel(enum.IntEnum):

    BASE = 0

class FloorComponent(GameComponent):

    _roomsCount: int
    _rooms: typing.List[RoomComponent]

    def __init__(self, level: typing.Union[FloorLevel, int]) -> None:
        match level:
            case FloorLevel.BASE:
                self._roomsCount = 10
    
    def _generate_rooms() -> typing.List[RoomComponent]:
        pass

    def update(self) -> typing.NoReturn:
        pass

    def render(self) -> typing.NoReturn:
        pass
    