from unittest import TestCase

from basketball_tokutenban.domain.game_time_setting import GameTimeSetting
from basketball_tokutenban.domain.game import Game
from basketball_tokutenban.domain.status import Status


class TestSetup(TestCase):

    def test_試合をセットアップするとフェーズがQuarter1で生成される(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)

        # when:
        game = Game.setup(game_time_setting)

        # then:
        self.assertEqual("Quarter1", game.phase.name)

    def test_試合をセットアップするとステータスがDeadで生成される(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)

        # when:
        game = Game.setup(game_time_setting)

        # then:
        self.assertEqual(Status.DEAD, game.status)

    def test_試合をセットアップするとホームの得点とファール数が0で生成される(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)

        # when:
        game = Game.setup(game_time_setting)

        # then:
        self.assertEqual(0, game.home.score)
        self.assertEqual(0, game.home.foul)

    def test_試合をセットアップするとゲストの得点とファール数が0で生成される(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)

        # when:
        game = Game.setup(game_time_setting)

        # then:
        self.assertEqual(0, game.guest.score)
        self.assertEqual(0, game.guest.foul)


class TestStart(TestCase):

    def test_試合をスタートするとステータスがLiveになる(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game = Game.setup(game_time_setting)

        # when:
        game.start()

        # then:
        self.assertEqual(Status.LIVE, game.status)


class TestStop(TestCase):

    def test_試合をストップするとステータスがDeadになる(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game = Game.setup(game_time_setting)
        game.start()

        # when:
        game.stop()

        # then:
        self.assertEqual(Status.DEAD, game.status)


class TestNextPhase(TestCase):

    def test_試合をQuarter1からIntervalに進めることができる(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game = Game.setup(game_time_setting)

        # when:
        game.next_phase()

        # then:
        self.assertEqual("Interval", game.phase.name)
        self.assertEqual(2, game.phase.time)

    def test_試合をIntervalからQuarter2に進めることができる(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game = Game.setup(game_time_setting)
        game.next_phase()

        # when:
        game.next_phase()

        # then:
        self.assertEqual("Quarter2", game.phase.name)
        self.assertEqual(10, game.phase.time)

    def test_試合をQuarter2からHalfTimeに進めることができる(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game = Game.setup(game_time_setting)
        game.next_phase()
        game.next_phase()

        # when:
        game.next_phase()

        # then:
        self.assertEqual("HalfTime", game.phase.name)
        self.assertEqual(15, game.phase.time)

    def test_試合をHalfTimeからQuarter3に進めることができる(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game = Game.setup(game_time_setting)
        game.next_phase()
        game.next_phase()
        game.next_phase()

        # when:
        game.next_phase()

        # then:
        self.assertEqual("Quarter3", game.phase.name)
        self.assertEqual(10, game.phase.time)

    def test_試合をQuarter3からIntervalに進めることができる(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game = Game.setup(game_time_setting)
        game.next_phase()
        game.next_phase()
        game.next_phase()
        game.next_phase()

        # when:
        game.next_phase()

        # then:
        self.assertEqual("Interval", game.phase.name)
        self.assertEqual(2, game.phase.time)

    def test_試合をIntervalからQuarter4に進めることができる(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game = Game.setup(game_time_setting)
        game.next_phase()
        game.next_phase()
        game.next_phase()
        game.next_phase()
        game.next_phase()

        # when:
        game.next_phase()

        # then:
        self.assertEqual("Quarter4", game.phase.name)
        self.assertEqual(10, game.phase.time)


class TestReset(TestCase):

    def test_試合をリセットするとステータスがDEADになっている(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game = Game.setup(game_time_setting)
        game.start()

        # when:
        game.reset()

        # then:
        self.assertEqual(Status.DEAD, game.status)

    def test_試合をリセットするとQuarter1に戻っている(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game = Game.setup(game_time_setting)
        game.next_phase()
        game.next_phase()
        game.next_phase()

        # when:
        game.reset()

        # then:
        self.assertEqual("Quarter1", game.phase.name)

    def test_試合をリセットするとホームの得点とファール数が0になっている(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game = Game.setup(game_time_setting)
        game.home.add_score(1)
        game.home.add_score(2)
        game.home.add_score(3)
        game.home.count_foul()

        # when:
        game.reset()

        # then:
        self.assertEqual(0, game.home.score)
        self.assertEqual(0, game.home.foul)

    def test_試合をリセットするとゲストの得点とファール数が0になっている(self) -> None:
        # given:
        game_time_setting = GameTimeSetting.setup(10, 2, 15)
        game = Game.setup(game_time_setting)
        game.guest.add_score(1)
        game.guest.add_score(2)
        game.guest.add_score(3)
        game.guest.count_foul()

        # when:
        game.reset()

        # then:
        self.assertEqual(0, game.guest.score)
        self.assertEqual(0, game.guest.foul)
