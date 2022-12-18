from basketball_tokutenban.application.start_game.start_game_response import StartGameResponse
from basketball_tokutenban.application.start_game.start_game_request import StartGameRequest
from basketball_tokutenban.domain.game import Game
from basketball_tokutenban.domain.i_game_repository import IGameRepository
from basketball_tokutenban.domain.i_game_time_setting_repository import IGameTimeSettingRepository


class StartGameUseCase:
    """ 試合をスタートするユースケース
    """

    def __init__(
        self,
        game_time_setting_repository: IGameTimeSettingRepository,
        game_repository: IGameRepository
    ) -> None:
        self.__game_time_setting_repository = game_time_setting_repository
        self.__game_repository = game_repository

    def execute(self, request: StartGameRequest) -> StartGameResponse:
        try:
            setting = self.__game_time_setting_repository.read()
            game = Game.setup(setting)
            game.start()

            self.__game_repository.save(game)

            response = StartGameResponse.success(
                game.status.name,
                game.phase.name,
                game.phase.time,
                game.home.score,
                game.home.foul,
                game.guest.score,
                game.guest.foul,
            )
            return response

        except Exception as ex:
            response = StartGameResponse.failure(str(ex))
            return response
