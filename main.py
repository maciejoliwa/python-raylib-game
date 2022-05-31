import typing
from pyray import *
from components import PlayerComponent

def main() -> typing.NoReturn:

    monitor = get_current_monitor()
    monitor_width = get_monitor_width(monitor)
    monitor_height = get_monitor_height(monitor)

    init_window(monitor_width, monitor_height, "Epic Cube")
    set_target_fps(60)
    
    player = PlayerComponent(100, 100)

    while not window_should_close():
        player.update()

        # DRAWING
        begin_drawing()
        clear_background(RAYWHITE)
        draw_text("EPIC CUBE", 200, 200, 69, RED)
        
        # Render components
        player.render()
        
        end_drawing()

    close_window()

if __name__ == '__main__':
    main()