from abc import ABC
from abc import abstractmethod

from basketball_tokutenban.domain.game import Game


class IGameRepository(ABC):
    """ 試合を取得/保存するためのリポジトリのインタフェース
    """

    @abstractmethod
    def read(self) -> Game:
        pass

    @abstractmethod
    def save(self, game: Game) -> None:
        pass
