from basketball_tokutenban.domain.game_flow import GameFlow
from basketball_tokutenban.domain.game_time_setting import GameTimeSetting
from basketball_tokutenban.domain.phase import Phase
from basketball_tokutenban.domain.status import Status
from basketball_tokutenban.domain.team import Team


class Game:
    """ 試合
    """

    @property
    def status(self) -> Status:
        """ ステータス
        """
        return self.__status

    @property
    def phase(self) -> Phase:
        """ フェーズ
        """
        return self.__flow.current

    @property
    def home(self) -> Team:
        """ ホーム
        """
        return self.__home

    @property
    def guest(self) -> Team:
        """ ゲスト
        """
        return self.__guest

    def __init__(self, status: Status, flow: GameFlow, home: Team, guest: Team) -> None:
        self.__status = status
        self.__flow = flow
        self.__home = home
        self.__guest = guest

    @classmethod
    def setup(cls, game_time_setting: GameTimeSetting) -> "Game":
        """ 試合をセッティングする
        """
        return Game(Status.DEAD, GameFlow.create(game_time_setting), Team.create(), Team.create())

    @classmethod
    def reconstruct(cls, status: Status, flow: GameFlow, home: Team, guest: Team) -> "Game":
        """ インフラ層から再構築するためのファクトリメソッド
            ※インフラ層でのみ使用可
        """
        return Game(status, flow, home, guest)

    def start(self) -> None:
        """ 試合をスタートする
        """
        self.__status = Status.LIVE

    def stop(self) -> None:
        """ 試合をストップする
        """
        self.__status = Status.DEAD

    def next_phase(self) -> None:
        """ 試合のフェーズを次に進める
        """
        self.__flow.next()

    def reset(self) -> None:
        """ 試合をリセットする
        """
        self.__status = Status.DEAD
        self.__flow.reset()
        self.__home.reset()
        self.__guest.reset()
