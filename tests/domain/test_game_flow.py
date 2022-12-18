from unittest import TestCase

from basketball_tokutenban.domain.game_flow import GameFlow
from basketball_tokutenban.domain.game_time_setting import GameTimeSetting


class TestCreate(TestCase):

    def test_生成された直後の現在のフェーズがQuarter1になっている(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)

        # when:
        game_flow = GameFlow.create(game_time_setting)

        # then:
        self.assertEqual("Quarter1", game_flow.current.name)

    def test_Quarter1から4が試合時間の設定通りになっている(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)

        # when:
        game_flow = GameFlow.create(game_time_setting)

        # then:
        self.assertEqual(10, game_flow.unsafe_trasitions(0).time)
        self.assertEqual(10, game_flow.unsafe_trasitions(2).time)
        self.assertEqual(10, game_flow.unsafe_trasitions(4).time)
        self.assertEqual(10, game_flow.unsafe_trasitions(6).time)

    def test_Intervalが試合時間の設定通りになっている(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)

        # when:
        game_flow = GameFlow.create(game_time_setting)

        # then:
        self.assertEqual(2, game_flow.unsafe_trasitions(1).time)
        self.assertEqual(2, game_flow.unsafe_trasitions(5).time)

    def test_HalfTimelが試合時間の設定通りになっている(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)

        # when:
        game_flow = GameFlow.create(game_time_setting)

        # then:
        self.assertEqual(15, game_flow.unsafe_trasitions(3).time)


class TestNext(TestCase):

    def test_Quarter1からIntervalに遷移できる(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game_flow = GameFlow.create(game_time_setting)

        # when:
        game_flow.next()

        # then:
        self.assertEqual("Interval", game_flow.current.name)

    def test_IntervalからQuarter2に遷移できる(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game_flow = GameFlow.create(game_time_setting)
        game_flow.next()

        # when:
        game_flow.next()

        # then:
        self.assertEqual("Quarter2", game_flow.current.name)

    def test_Quarter2からHalfTimeに遷移できる(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game_flow = GameFlow.create(game_time_setting)
        game_flow.next()
        game_flow.next()

        # when:
        game_flow.next()

        # then:
        self.assertEqual("HalfTime", game_flow.current.name)

    def test_HalfTimeからQuarter3に遷移できる(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game_flow = GameFlow.create(game_time_setting)
        game_flow.next()
        game_flow.next()
        game_flow.next()

        # when:
        game_flow.next()

        # then:
        self.assertEqual("Quarter3", game_flow.current.name)

    def test_Quarter3からIntervalに遷移できる(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game_flow = GameFlow.create(game_time_setting)
        game_flow.next()
        game_flow.next()
        game_flow.next()
        game_flow.next()

        # when:
        game_flow.next()

        # then:
        self.assertEqual("Interval", game_flow.current.name)

    def test_IntervalからQuarter4に遷移できる(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game_flow = GameFlow.create(game_time_setting)
        game_flow.next()
        game_flow.next()
        game_flow.next()
        game_flow.next()
        game_flow.next()

        # when:
        game_flow.next()

        # then:
        self.assertEqual("Quarter4", game_flow.current.name)

    def test_Quarter4の状態からはどこにも遷移できない(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game_flow = GameFlow.create(game_time_setting)
        game_flow.next()
        game_flow.next()
        game_flow.next()
        game_flow.next()
        game_flow.next()
        game_flow.next()

        # when:
        game_flow.next()

        # then:
        self.assertEqual("Quarter4", game_flow.current.name)


class TestReset(TestCase):

    def test_最初のフェーズに戻ることができる(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game_flow = GameFlow.create(game_time_setting)
        game_flow.next()
        game_flow.next()
        game_flow.next()
        game_flow.next()
        game_flow.next()
        game_flow.next()

        # when:
        game_flow.reset()

        # then:
        self.assertEqual("Quarter1", game_flow.current.name)
