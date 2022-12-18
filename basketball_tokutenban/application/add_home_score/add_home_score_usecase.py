from basketball_tokutenban.application.add_home_score.add_home_score_request import AddHomeScoreRequest
from basketball_tokutenban.application.add_home_score.add_home_score_response import AddHomeScoreResponse
from basketball_tokutenban.domain.i_game_repository import IGameRepository


class AddHomeScoreUseCase:
    """ ホームの得点を加算するユースケース
    """

    def __init__(self, game_repository: IGameRepository) -> None:
        self.__game_repository = game_repository

    def execute(self, request: AddHomeScoreRequest) -> AddHomeScoreResponse:
        try:
            game = self.__game_repository.read()
            game.home.add_score(request.points)
            self.__game_repository.save(game)

            response = AddHomeScoreResponse.success(
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
            response = AddHomeScoreResponse.failure(str(ex))
            return response
