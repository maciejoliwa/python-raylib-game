import typing
import random
import enum
from .game_component import GameComponent
from pyray import *


RoomType = typing.Dict[str, typing.Any]
_ROOM_SIZE = 1024

class FloorLevel(enum.IntEnum):

    BASE = 0

class FloorComponent(GameComponent):

    _roomsCount: int
    _rooms: typing.List[RoomType]

    def __init__(self, level: typing.Union[FloorLevel, int]) -> None:
        match level:
            case FloorLevel.BASE:
                self._floorColour = GRAY
                self._roomsCount = 10
        
        self._rooms = self._generate_rooms()
    
    def _generate_room(self, current_rooms: typing.List[RoomType], i: int) -> RoomType:
        curr_x = 0
        curr_y = 0

        for index, room in enumerate(current_rooms):
            if index == i:
                break

            curr_x += _ROOM_SIZE + 256

        return { "x": curr_x, "y": curr_y, "visited": False, "item_room": False }

    def _generate_rooms(self) -> typing.List[RoomType]:
        rooms = []
        for i in range(self._roomsCount):
            room = self._generate_room(rooms, i)

            rooms.append(room)

        index_to_update = random.choice(range(0, len(rooms)))  # We pick the funny treasure room
        rooms[index_to_update]["item_room"] = True
        return rooms

    def update(self, **kwargs) -> typing.NoReturn:
        player = kwargs["player"]
        
        for room in self._rooms:
            pl_rect = Rectangle(player._x, player._y, 96, 96)
            room_rect = Rectangle(room["x"], room["y"], _ROOM_SIZE, _ROOM_SIZE)

            if check_collision_recs(pl_rect, room_rect):
                room["visited"] = True

    def render(self) -> typing.NoReturn:
        for index, room in enumerate(self._rooms):
            if room["visited"]:
                draw_rectangle(room["x"], room["y"], _ROOM_SIZE, _ROOM_SIZE, DARKGRAY)
            if room["item_room"]:
                draw_rectangle(room["x"], room["y"], _ROOM_SIZE, _ROOM_SIZE, YELLOW)
            else:
                draw_rectangle(room["x"], room["y"], _ROOM_SIZE, _ROOM_SIZE, self._floorColour)
             
            if index < len(self._rooms) - 1:
                draw_rectangle(room["x"] + _ROOM_SIZE, room["y"] + (int(_ROOM_SIZE/2) - 100), 256, 200, RED)
