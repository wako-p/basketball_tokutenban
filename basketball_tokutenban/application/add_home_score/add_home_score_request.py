class AddHomeScoreRequest:
    """ AddHomeScoreUseCaseのリクエスト(DTO)
    """

    def __init__(self, points: int) -> None:
        self.points = points
