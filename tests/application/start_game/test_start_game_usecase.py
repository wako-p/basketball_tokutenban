from unittest import TestCase
from unittest.mock import MagicMock

from basketball_tokutenban.application.start_game.start_game_request import StartGameRequest
from basketball_tokutenban.application.start_game.start_game_usecase import StartGameUseCase
from basketball_tokutenban.domain.game_time_setting import GameTimeSetting
from basketball_tokutenban.domain.game import Game
from basketball_tokutenban.domain.i_game_repository import IGameRepository
from basketball_tokutenban.domain.i_game_time_setting_repository import IGameTimeSettingRepository


class TestExecute(TestCase):

    def test_ステータスがLiveの試合を保存できる(self) -> None:
        # given:
        game_time_setting_repository_mock = MagicMock(sepc_set=IGameTimeSettingRepository)
        setting = GameTimeSetting.setup(10, 2, 20)
        game_time_setting_repository_mock.read.return_value = setting

        game_repository_mock = MagicMock(spec_set=IGameRepository)

        request = StartGameRequest()
        usecase = StartGameUseCase(game_time_setting_repository_mock, game_repository_mock)

        # when:
        usecase.execute(request)

        # then:
        # IGameRepository.save()にGameが渡されている
        captured_game: Game = game_repository_mock.save.call_args.args[0]
        self.assertEqual("LIVE", captured_game.status.name)
