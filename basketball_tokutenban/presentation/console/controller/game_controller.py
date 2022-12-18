from basketball_tokutenban.application.add_guest_score.add_guest_score_request import AddGuestScoreRequest
from basketball_tokutenban.application.add_guest_score.add_guest_score_usecase import AddGuestScoreUseCase
from basketball_tokutenban.application.add_home_score.add_home_score_request import AddHomeScoreRequest
from basketball_tokutenban.application.add_home_score.add_home_score_usecase import AddHomeScoreUseCase
from basketball_tokutenban.application.start_game.start_game_request import StartGameRequest
from basketball_tokutenban.application.start_game.start_game_usecase import StartGameUseCase
from basketball_tokutenban.presentation.console.model.game_model import GameModel


class GameConrtoller:
    """ 試合のコントローラー
    """

    def __init__(
        self,
        start_game_usecase: StartGameUseCase,
        add_home_score_usecase: AddHomeScoreUseCase,
        add_guest_score_usecase: AddGuestScoreUseCase,
    ) -> None:
        self.__start_usecase = start_game_usecase
        self.__add_home_score_usecase = add_home_score_usecase
        self.__add_guest_score_usecase = add_guest_score_usecase

    def start(self) -> "GameModel":
        """ 試合をスタートする
        """
        request = StartGameRequest()
        response = self.__start_usecase.execute(request)

        model = GameModel(
            response.status,
            response.phase_name,
            response.phase_time,
            response.home_score,
            response.home_foul,
            response.guest_score,
            response.guest_foul,
            response.error
        )
        return model

    def add_home_score(self, points: int) -> GameModel:
        """ ホームの得点を加算する
        """
        request = AddHomeScoreRequest(points)
        response = self.__add_home_score_usecase.execute(request)

        model = GameModel(
            response.status,
            response.phase_name,
            response.phase_time,
            response.home_score,
            response.home_foul,
            response.guest_score,
            response.guest_foul,
            response.error
        )
        return model

    def add_quest_score(self, points: int) -> GameModel:
        """ ゲストの得点を加算する
        """
        request = AddGuestScoreRequest(points)
        response = self.__add_guest_score_usecase.execute(request)

        model = GameModel(
            response.status,
            response.phase_name,
            response.phase_time,
            response.home_score,
            response.home_foul,
            response.guest_score,
            response.guest_foul,
            response.error
        )
        return model
