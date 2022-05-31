import sys

def main():
    args = sys.argv[1:]
    component_name = args[0]
    class_name = "".join([s.capitalize() for s in component_name.split('_')])

    template =  f"""import typing
from .game_component import GameComponent
from pyray import *

class {class_name}(GameComponent):

    def update(self) -> typing.NoReturn:
        pass

    def render(self) -> typing.NoReturn:
        pass
    """

    with open(f'components/{component_name}.py', 'w+') as COMPONENT_FILE:
        COMPONENT_FILE.write(template)

    print(f"Generated {component_name}.py file!")


if __name__ == '__main__':
    main()