from basketball_tokutenban.domain.phase import Phase
from basketball_tokutenban.domain.game_time_setting import GameTimeSetting


class GameFlow:
    """ 試合のフロー
    """

    __phases: list[Phase]

    @property
    def current(self) -> Phase:
        """ 現在のフェーズ
        """
        return self.__phases[self.__index]

    def __init__(self, phases: list[Phase], index: int) -> None:
        self.__phases = phases
        self.__index = index

    @classmethod
    def create(cls, game_time_setting: GameTimeSetting) -> "GameFlow":
        """ 試合のフローを試合時間の設定を考慮して生成する
        """
        phases: list[Phase] = []
        phases.append(Phase.quarter1(game_time_setting.quarter))
        phases.append(Phase.interval(game_time_setting.interval))
        phases.append(Phase.quarter2(game_time_setting.quarter))
        phases.append(Phase.halftime(game_time_setting.halftime))
        phases.append(Phase.quarter3(game_time_setting.quarter))
        phases.append(Phase.interval(game_time_setting.interval))
        phases.append(Phase.quarter4(game_time_setting.quarter))

        return GameFlow(phases, 0)

    @classmethod
    def reconstruct(cls, phases: list[Phase], index: int) -> "GameFlow":
        """ インフラ層から再構築するためのファクトリメソッド
            ※インフラ層でのみ使用可
        """
        return GameFlow(phases, index)

    def next(self) -> None:
        """ 次のフェーズに遷移する
        """
        # 最後のフェーズにいる場合は何もしない
        if (self.is_last_phase()):
            return

        self.__index += 1

    def is_last_phase(self) -> bool:
        return self.__index == (len(self.__phases) - 1)

    def reset(self) -> None:
        """ 試合のフローをリセットする
        """
        self.__index = 0

    def unsafe_trasitions(self, index: int) -> Phase:
        """ テストコード用
            ※プロダクトコードでは使用禁止
        """
        return self.__phases[index]
