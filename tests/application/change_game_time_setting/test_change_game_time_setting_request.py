from unittest import TestCase

from basketball_tokutenban.application.change_game_time_setting.change_game_time_setting_request import ChangeGameTimeSettingRequest


class TestNew(TestCase):

    def test_引数にQuarterの時間などを指定して生成できる(self) -> None:
        # when:
        request = ChangeGameTimeSettingRequest(10, 2, 15)

        # then:
        self.assertEqual(10, request.quarter)
        self.assertEqual(2, request.interval)
        self.assertEqual(15, request.halftime)
