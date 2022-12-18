from typing import Optional


class AddHomeScoreResponse:
    """ AddHomeScoreUseCaseのレスポンス(DTO)
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

    @classmethod
    def success(
        cls,
        status: str,
        phase_name: str,
        phase_time: int,
        home_score: int,
        home_foul: int,
        guest_score: int,
        guest_foul: int
    ) -> "AddHomeScoreResponse":
        return AddHomeScoreResponse(status, phase_name, phase_time, home_score, home_foul, guest_score, guest_foul, "")

    @classmethod
    def failure(cls, error: str) -> "AddHomeScoreResponse":
        return AddHomeScoreResponse(None, None, None, None, None, None, None, error)
