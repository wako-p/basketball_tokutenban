from unittest import TestCase
from unittest.mock import MagicMock

from basketball_tokutenban.application.change_game_time_setting.change_game_time_setting_request import ChangeGameTimeSettingRequest
from basketball_tokutenban.application.change_game_time_setting.change_game_time_setting_usecase import ChangeGameTimeSettingUseCase
from basketball_tokutenban.domain.game_time_setting import GameTimeSetting
from basketball_tokutenban.domain.i_game_time_setting_repository import IGameTimeSettingRepository


class TestExecute(TestCase):

    def test_変更された試合時間の設定を保存できる(self) -> None:
        # given:
        setting_repository_mock = MagicMock(spec_set=IGameTimeSettingRepository)
        setting = GameTimeSetting.setup(10, 2, 15)
        setting_repository_mock.read.return_value = setting

        request = ChangeGameTimeSettingRequest(8, 2, 20)
        usecase = ChangeGameTimeSettingUseCase(setting_repository_mock)

        # when:
        usecase.execute(request)

        # then:
        # IGameTimeSettingRepository.save()にGameTimeSettingが渡されている
        captured_setting: GameTimeSetting = setting_repository_mock.save.call_args.args[0]
        self.assertEqual(8, captured_setting.quarter)
        self.assertEqual(2, captured_setting.interval)
        self.assertEqual(20, captured_setting.halftime)
