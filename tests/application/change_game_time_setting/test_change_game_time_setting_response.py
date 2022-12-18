from unittest import TestCase

from basketball_tokutenban.application.change_game_time_setting.change_game_time_setting_response import ChangeGameTimeSettingResponse


class TestSuccess(TestCase):

    def test_引数にQuarterの時間などを指定して生成できる(self) -> None:
        # when:
        response = ChangeGameTimeSettingResponse.success(8, 2, 20)

        # then:
        self.assertEqual(8, response.quarter)
        self.assertEqual(2, response.interval)
        self.assertEqual(20, response.halftime)
        self.assertEqual("", response.error)


class TestFailure(TestCase):

    def test_引数にエラーメッセージを指定して生成できる(self) -> None:
        # when:
        response = ChangeGameTimeSettingResponse.failure("Failed to change game time settings.")

        # then:
        self.assertEqual(None, response.quarter)
        self.assertEqual(None, response.interval)
        self.assertEqual(None, response.halftime)
        self.assertEqual("Failed to change game time settings.", response.error)
