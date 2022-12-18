from typing import Optional


class GameModel:
    """ 試合のモデル
    """

    def __init__(
        self,
        status: Optional[str],
        phase_name: Optional[str],
        phase_time: Optional[int],
        home_score: Optional[int],
        home_foul: Optional[int],
        guest_score: Optional[int],
        guest_foul: Optional[int],
        error: str
    ) -> None:
        self.status = status
        self.phase_name = phase_name
        self.phase_time = phase_time
        self.home_score = home_score
        self.home_foul = home_foul
        self.guest_score = guest_score
        self.guest_foul = guest_foul
        self.error = error
