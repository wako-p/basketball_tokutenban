from unittest import TestCase
from unittest.mock import MagicMock

from basketball_tokutenban.application.add_home_score.add_home_score_request import AddHomeScoreRequest
from basketball_tokutenban.application.add_home_score.add_home_score_usecase import AddHomeScoreUseCase
from basketball_tokutenban.domain.game_time_setting import GameTimeSetting
from basketball_tokutenban.domain.game import Game
from basketball_tokutenban.domain.i_game_repository import IGameRepository


class TestExecute(TestCase):

    def test_ホームの得点が加算された試合を保存できる(self) -> None:
        # given:
        game_repository_mock = MagicMock(spec_set=IGameRepository)
        setting = GameTimeSetting.setup(10, 2, 20)
        game = Game.setup(setting)
        game_repository_mock.read.return_value = game

        request = AddHomeScoreRequest(3)
        usecase = AddHomeScoreUseCase(game_repository_mock)

        # when:
        usecase.execute(request)

        # then:
        # IGameRepository.save()にGameが渡されている
        captured_game: Game = game_repository_mock.save.call_args.args[0]
        self.assertEqual(3, captured_game.home.score)
        self.assertEqual(0, captured_game.guest.score)
