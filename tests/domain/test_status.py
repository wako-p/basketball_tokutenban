from unittest import TestCase
from parameterized import parameterized, param

from basketball_tokutenban.domain.status import Status


class TestEnum(TestCase):

    def test_DEADを取得できる(self) -> None:
        # when:
        status = Status.DEAD

        # then:
        self.assertEqual("DEAD", status.name)
        self.assertEqual(0, status.value)

    def test_LIVEを取得できる(self) -> None:
        # when:
        status = Status.LIVE

        # then:
        self.assertEqual("LIVE", status.name)
        self.assertEqual(1, status.value)


class TestReconstruct(TestCase):

    @parameterized.expand([
        param(0, 0),
        param(1, 1),
    ])
    def test_引数に0または1を指定すると再構築できる(self, value: int, expected: int) -> None:
        # when:
        status = Status.reconstruct(value)

        # then:
        self.assertEqual(expected, status.value)

    @parameterized.expand([
        param(-1),
        param(2),
        param(3),
    ])
    def test_引数に0または1以外を指定すると例外がスローされる(self, value: int) -> None:
        # when/then:
        with self.assertRaises(ValueError):
            Status.reconstruct(value)
