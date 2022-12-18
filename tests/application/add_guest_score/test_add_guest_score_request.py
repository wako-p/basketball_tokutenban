from unittest import TestCase

from basketball_tokutenban.application.add_guest_score.add_guest_score_request import AddGuestScoreRequest


class TestNew(TestCase):

    def test_引数にゲストの得点を指定して生成できる(self) -> None:
        # when:
        request = AddGuestScoreRequest(3)

        # then:
        self.assertEqual(3, request.points)
