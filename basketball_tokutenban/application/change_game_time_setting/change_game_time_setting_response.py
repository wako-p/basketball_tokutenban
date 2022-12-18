from typing import Optional


class ChangeGameTimeSettingResponse:
    """ ChangeGameTimeSettingUseCaseのレスポンス(DTO)
    """

    def __init__(self, quarter: Optional[int], interval: Optional[int], halftime: Optional[int], error: str) -> None:
        self.quarter = quarter
        self.interval = interval
        self.halftime = halftime
        self.error = error

    @classmethod
    def success(cls, quarter: int, interval: int, halftime: int) -> "ChangeGameTimeSettingResponse":
        return ChangeGameTimeSettingResponse(quarter, interval, halftime, "")

    @classmethod
    def failure(cls, error: str) -> "ChangeGameTimeSettingResponse":
        return ChangeGameTimeSettingResponse(None, None, None, error)
