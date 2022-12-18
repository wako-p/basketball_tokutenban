class Team:
    """ チーム
    """

    @property
    def score(self) -> int:
        """ 得点
        """
        return self.__score

    @property
    def foul(self) -> int:
        """ ファール数
        """
        return self.__foul

    def __init__(self, score: int, foul: int) -> None:
        self.__score = score
        self.__foul = foul

    @classmethod
    def create(cls) -> "Team":
        return Team(0, 0)

    @classmethod
    def reconstruct(cls, score: int, foul: int) -> "Team":
        """ インフラ層で再構築するためのファクトリメソッド
            ※インフラ層でのみ使用可
        """
        return Team(score, foul)

    def add_score(self, points: int) -> None:
        """ 得点を加算する
        """
        if (not (1 <= points and points <= 3)):
            raise Exception("得点は1～3点の範囲内で指定する必要があります。")

        self.__score += points

    def count_foul(self) -> None:
        """ ファール数をカウントする
        """
        self.__foul += 1

    def reset(self) -> None:
        """ 得点とファール数をリセットする
        """
        self.__score = 0
        self.__foul = 0
