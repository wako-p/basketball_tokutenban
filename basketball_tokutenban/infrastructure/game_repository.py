from basketball_tokutenban.domain.game_flow import GameFlow
from basketball_tokutenban.domain.game import Game
from basketball_tokutenban.domain.i_game_repository import IGameRepository
from basketball_tokutenban.domain.phase import Phase
from basketball_tokutenban.domain.status import Status
from basketball_tokutenban.domain.team import Team


class GameRepository(IGameRepository):
    """ 試合を取得/保存するためのリポジトリ
    """

    def read(self) -> Game:
        # ココでDB/ファイル/RAMなどから取得したプリミティブなデータを
        # ドメインオブジェクトに変換(詰め替え)して返す

        # とりあえず、テキトーな値で試合を再構築する
        status = Status.reconstruct(0)

        phases: list[Phase] = []
        phases.append(Phase.reconstruct("Quarter1", 10))
        phases.append(Phase.reconstruct("Interval", 2))
        phases.append(Phase.reconstruct("Quarter2", 10))
        phases.append(Phase.reconstruct("HalfTime", 20))
        phases.append(Phase.reconstruct("Quarter3", 10))
        phases.append(Phase.reconstruct("Interval", 2))
        phases.append(Phase.reconstruct("Quarter4", 10))
        flow = GameFlow.reconstruct(phases, 2)

        home = Team.reconstruct(3, 0)
        guest = Team.reconstruct(6, 1)

        return Game.reconstruct(status, flow, home, guest)

    def save(self, game: Game) -> None:
        # ココでドメインオブジェクトからプリミティブなデータに変換して
        # DB/ファイル/RAMなどに保存する
        pass
