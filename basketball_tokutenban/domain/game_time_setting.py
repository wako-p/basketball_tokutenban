class GameTimeSetting:
    """ 試合時間の設定
    """

    @property
    def quarter(self) -> int:
        """ クォーターの時間[分]
        """
        return self.__quarter

    @property
    def interval(self) -> int:
        """ インターバルの時間[分]
        """
        return self.__interval

    @property
    def halftime(self) -> int:
        """ ハーフタイムの時間[分]
        """
        return self.__halftime

    def __init__(self, quarter: int, interval: int, halftime: int) -> None:
        self.__quarter = quarter
        self.__interval = interval
        self.__halftime = halftime

    @classmethod
    def setup(cls, quarter: int, interval: int, halftime: int) -> "GameTimeSetting":
        return GameTimeSetting(quarter, interval, halftime)

    @classmethod
    def reconstruct(cls, quarter: int, interval: int, halftime: int) -> "GameTimeSetting":
        """ インフラ層から再構築するためのファクトリメソッド
            ※インフラ層でのみ使用可
        """
        return GameTimeSetting(quarter, interval, halftime)

    def change_quarter(self, quarter: int) -> None:
        self.__quarter = quarter

    def change_interval(self, interval: int) -> None:
        self.__interval = interval

    def change_halftime(self, halftime: int) -> None:
        self.__halftime = halftime
