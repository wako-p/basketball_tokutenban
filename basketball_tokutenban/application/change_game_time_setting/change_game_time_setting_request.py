class ChangeGameTimeSettingRequest:
    """ ChangeGameTimeSettingUseCaseのリクエスト(DTO)
    """

    def __init__(self, quarter: int, interval: int, halftime: int) -> None:
        self.quarter = quarter
        self.interval = interval
        self.halftime = halftime
