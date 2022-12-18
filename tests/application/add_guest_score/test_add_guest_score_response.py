from unittest import TestCase

from basketball_tokutenban.application.add_guest_score.add_guest_score_response import AddGuestScoreResponse


class TestSuccess(TestCase):

    def test_引数にステータスなどを指定して生成できる(self) -> None:
        # when:
        response = AddGuestScoreResponse.success("Live", "Quarter1", 10, 6, 0, 3, 0)

        # then:
        self.assertEqual("Live", response.status)
        self.assertEqual("Quarter1", response.phase_name)
        self.assertEqual(10, response.phase_time)
        self.assertEqual(6, response.home_score)
        self.assertEqual(0, response.home_foul)
        self.assertEqual(3, response.guest_score)
        self.assertEqual(0, response.guest_foul)
        self.assertEqual("", response.error)


class TestFailure(TestCase):

    def test_引数にエラーメッセージを指定して生成できる(self) -> None:
        # when:
        response = AddGuestScoreResponse.failure("Failed to add the Guest points.")

        # then:
        self.assertEqual(None, response.status)
        self.assertEqual(None, response.phase_name)
        self.assertEqual(None, response.phase_time)
        self.assertEqual(None, response.home_score)
        self.assertEqual(None, response.home_foul)
        self.assertEqual(None, response.guest_score)
        self.assertEqual(None, response.guest_foul)
        self.assertEqual("Failed to add the Guest points.", response.error)
