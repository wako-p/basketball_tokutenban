from unittest import TestCase

from basketball_tokutenban.domain.game_time_setting import GameTimeSetting


class TestSetup(TestCase):

    def test_引数にクォータなどの時間を指定して生成できる(self) -> None:
        # when:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)

        # then:
        self.assertEqual(10, game_time_setting.quarter)
        self.assertEqual(2, game_time_setting.interval)
        self.assertEqual(15, game_time_setting.halftime)


class TestChangeQuarter(TestCase):

    def test_Quarterの時間を変更できる(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)

        # when:
        game_time_setting.change_quarter(8)

        # then:
        self.assertEqual(8, game_time_setting.quarter)


class TestChangeInterval(TestCase):

    def test_Intervalの時間を変更できる(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)

        # when:
        game_time_setting.change_interval(4)

        # then:
        self.assertEqual(4, game_time_setting.interval)


class TestChangehalfTime(TestCase):

    def test_HalfTimeの時間を変更できる(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)

        # when:
        game_time_setting.change_halftime(20)

        # then:
        self.assertEqual(20, game_time_setting.halftime)
