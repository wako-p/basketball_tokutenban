class AddGuestScoreRequest:
    """ AddGuestScoreUseCaseのリクエスト(DTO)
    """

    def __init__(self, points: int) -> None:
        self.points = points
