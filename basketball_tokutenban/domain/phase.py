class Phase:
    """ フェーズ
    """

    @property
    def name(self) -> str:
        """ フェーズ名
        """
        return self.__name

    @property
    def time(self) -> int:
        """ 時間
        """
        return self.__time

    def __init__(self, name: str, time: int) -> None:
        self.__name = name
        self.__time = time

    @classmethod
    def quarter1(cls, time: int) -> "Phase":
        return Phase("Quarter1", time)

    @classmethod
    def quarter2(cls, time: int) -> "Phase":
        return Phase("Quarter2", time)

    @classmethod
    def quarter3(cls, time: int) -> "Phase":
        return Phase("Quarter3", time)

    @classmethod
    def quarter4(cls, time: int) -> "Phase":
        return Phase("Quarter4", time)

    @classmethod
    def interval(cls, time: int) -> "Phase":
        return Phase("Interval", time)

    @classmethod
    def halftime(cls, time: int) -> "Phase":
        return Phase("HalfTime", time)

    @classmethod
    def reconstruct(cls, name: str, time: int) -> "Phase":
        """ インフラ層から再構築するためのファクトリメソッド
            ※インフラ層でのみ使用可
        """
        return Phase(name, time)
