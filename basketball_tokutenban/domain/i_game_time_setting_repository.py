from abc import ABC
from abc import abstractmethod

from basketball_tokutenban.domain.game_time_setting import GameTimeSetting


class IGameTimeSettingRepository(ABC):
    """ 試合時間の設定を取得/保存するためのリポジトリのインタフェース
    """

    @abstractmethod
    def read(self) -> GameTimeSetting:
        pass

    @abstractmethod
    def save(self, setting: GameTimeSetting) -> None:
        pass
