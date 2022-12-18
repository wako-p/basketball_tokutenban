from enum import Enum


class Status(Enum):
    """ ステータス
    """
    DEAD = (0),
    LIVE = (1),

    @property
    def value(self) -> int:
        return self.__value

    def __init__(self, value: int) -> None:
        self.__value = value

    @classmethod
    def reconstruct(cls, value: int) -> "Status":
        """ インフラ層から再構築するためのファクトリメソッド
            ※インフラ層でのみ使用可
        """
        for status in cls._member_map_.values():
            if status.value == value:
                return status  # type: ignore

        raise ValueError(f"引数に指定した値({value})は未定義です。")
