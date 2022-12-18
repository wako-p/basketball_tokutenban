from typing import Optional


class GameTimeSettingModel:
    """ 試合時間の設定のモデル
    """

    def __init__(
        self,
        quarter: Optional[int],
        interval: Optional[int],
        halftime: Optional[int],
        error: str
    ) -> None:
        self.quarter = quarter
        self.interval = interval
        self.halftime = halftime
        self.error = error
