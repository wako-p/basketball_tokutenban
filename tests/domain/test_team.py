from unittest import TestCase
from parameterized import parameterized, param

from basketball_tokutenban.domain.team import Team


class TestCreate(TestCase):

    def test_生成された直後の得点とファール数は0になっている(self) -> None:
        # when:
        team = Team.create()

        # then:
        self.assertEqual(0, team.score)
        self.assertEqual(0, team.foul)


class TestReconstruct(TestCase):

    def test_引数に得点とファール数を指定して再構築できる(self) -> None:
        # when:
        team = Team.reconstruct(3, 1)

        # then:
        self.assertEqual(3, team.score)
        self.assertEqual(1, team.foul)


class TestAddPoints(TestCase):

    @parameterized.expand([
        param(points=1, expected=1),
        param(points=2, expected=2),
        param(points=3, expected=3),
    ])
    def test_得点を1から3点加算することができる(self, points: int, expected: int) -> None:
        # given:
        team = Team.create()

        # when:
        team.add_score(points)

        # then:
        self.assertEqual(expected, team.score)

    @parameterized.expand([
        param(points=-1),
        param(points=0),
        param(points=4),
        param(points=5),
    ])
    def test_引数に1から3点以外を指定すると例外がスローされる(self, points: int) -> None:
        # given:
        team = Team.create()

        # when/then:
        with self.assertRaises(Exception):
            team.add_score(points)


class TestCountFoul(TestCase):

    def test_ファール数をカウントすることができる(self) -> None:
        # given:
        team = Team.create()

        # when:
        team.count_foul()
        team.count_foul()
        team.count_foul()

        # then:
        self.assertEqual(3, team.foul)


class TestReset(TestCase):

    def test_得点とファール数をリセットできる(self) -> None:
        # given:
        team = Team.create()
        team.add_score(1)
        team.add_score(2)
        team.add_score(3)
        team.count_foul()

        # when:
        team.reset()

        # then:
        self.assertEqual(0, team.score)
        self.assertEqual(0, team.foul)
