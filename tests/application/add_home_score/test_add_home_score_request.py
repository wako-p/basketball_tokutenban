from unittest import TestCase

from basketball_tokutenban.application.add_home_score.add_home_score_request import AddHomeScoreRequest


class TestNew(TestCase):

    def test_引数にホームの得点を指定して生成できる(self) -> None:
        # when:
        request = AddHomeScoreRequest(3)

        # then:
        self.assertEqual(3, request.points)
