from unittest import TestCase

from basketball_tokutenban.domain.phase import Phase


class TestQuarter1(TestCase):

    def test_引数に指定した時間のQuarter1を生成できる(self) -> None:
        # when:
        phase = Phase.quarter1(10)

        # then:
        self.assertEqual("Quarter1", phase.name)
        self.assertEqual(10, phase.time)


class TestQuarter2(TestCase):

    def test_引数に指定した時間のQuarter2を生成できる(self) -> None:
        # when:
        phase = Phase.quarter2(10)

        # then:
        self.assertEqual("Quarter2", phase.name)
        self.assertEqual(10, phase.time)


class TestQuarter3(TestCase):

    def test_引数に指定した時間のQuarter3を生成できる(self) -> None:
        # when:
        phase = Phase.quarter3(10)

        # then:
        self.assertEqual("Quarter3", phase.name)
        self.assertEqual(10, phase.time)


class TestQuarter4(TestCase):

    def test_引数に指定した時間のQuarter4を生成できる(self) -> None:
        # when:
        phase = Phase.quarter4(10)

        # then:
        self.assertEqual("Quarter4", phase.name)
        self.assertEqual(10, phase.time)


class TestInterval(TestCase):

    def test_引数に指定した時間のIntervalを生成できる(self) -> None:
        # when:
        phase = Phase.interval(2)

        # then:
        self.assertEqual("Interval", phase.name)
        self.assertEqual(2, phase.time)


class TestHalfTime(TestCase):

    def test_引数に指定した時間のHalfTimeを生成できる(self) -> None:
        # when:
        phase = Phase.halftime(15)

        # then:
        self.assertEqual("HalfTime", phase.name)
        self.assertEqual(15, phase.time)


class TestReconstruct(TestCase):

    def test_引数にフェーズ名と時間を指定して再構築することができる(self) -> None:
        # when:
        phase = Phase.reconstruct("Quarter1", 10)

        # then:
        self.assertEqual("Quarter1", phase.name)
        self.assertEqual(10, phase.time)
