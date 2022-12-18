from basketball_tokutenban.application.add_guest_score.add_guest_score_request import AddGuestScoreRequest
from basketball_tokutenban.application.add_guest_score.add_guest_score_response import AddGuestScoreResponse
from basketball_tokutenban.domain.i_game_repository import IGameRepository


class AddGuestScoreUseCase:
    """ ゲストの得点を加算するユースケース
    """

    def __init__(self, game_repository: IGameRepository) -> None:
        self.__game_repository = game_repository

    def execute(self, request: AddGuestScoreRequest) -> AddGuestScoreResponse:
        try:
            game = self.__game_repository.read()
            game.guest.add_score(request.points)
            self.__game_repository.save(game)

            response = AddGuestScoreResponse.success(
                game.status.name,
                game.phase.name,
                game.phase.time,
                game.home.score,
                game.home.foul,
                game.guest.score,
                game.guest.foul
            )
            return response

        except Exception as ex:
            response = AddGuestScoreResponse.failure(str(ex))
            return response
