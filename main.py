import typing
from pyray import *
from components import PlayerComponent, FloorComponent, FloorLevel, ItemComponent

def main() -> typing.NoReturn:
    width = 1720
    height = 1020

    init_window(width, height, "Epic Cube")
    set_target_fps(60)

    player = PlayerComponent(int((width/2)), int((height/2)))

    # CAMERA SETUP
    camera = Camera2D()
    camera.target = Vector2(player._x, player._y)
    camera.offset = Vector2(width/2, height/2)
    camera.rotation = 0
    camera.zoom = 1

    floor_01 = FloorComponent(level=FloorLevel.BASE)

    it = ItemComponent(None)

    while not window_should_close():
        # UPDATE EVERYTHING
        floor_01.update(player=player)
        it.update(player=player, floor=floor_01)
        player.update()

        camera.target = Vector2(player._x+48, player._y+48)

        # DRAWING
        begin_drawing()
        clear_background(RAYWHITE)
       
        begin_mode_2d(camera)

        # Render components
        floor_01.render()
        it.render()
        player.render()
        

        end_mode_2d()

        end_drawing()

    close_window()

if __name__ == '__main__':
    main()
