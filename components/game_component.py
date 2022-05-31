import typing
import abc

class GameComponent(abc.ABC):

    @abc.abstractmethod
    def update(self) -> typing.NoReturn:
        pass

    @abc.abstractmethod
    def render(self) -> typing.NoReturn:
        pass
