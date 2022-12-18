from unittest import TestCase

from basketball_tokutenban.application.start_game.start_game_response import StartGameResponse


class TestSuccess(TestCase):

    def test_引数にステータスなどを指定して生成できる(self) -> None:
        # when:
        response = StartGameResponse.success("Live", "Quarter1", 10, 0, 0, 0, 0)

        # then:
        self.assertEqual("Live", response.status)
        self.assertEqual("Quarter1", response.phase_name)
        self.assertEqual(10, response.phase_time)
        self.assertEqual(0, response.home_score)
        self.assertEqual(0, response.home_foul)
        self.assertEqual(0, response.guest_score)
        self.assertEqual(0, response.guest_foul)
        self.assertEqual("", response.error)


class TestFailure(TestCase):

    def test_引数にエラーメッセージを指定して生成できる(self) -> None:
        # when:
        response = StartGameResponse.failure("Failed to add the Home team's points.")

        # then:
        self.assertEqual(None, response.status)
        self.assertEqual(None, response.phase_name)
        self.assertEqual(None, response.phase_time)
        self.assertEqual(None, response.home_score)
        self.assertEqual(None, response.home_foul)
        self.assertEqual(None, response.guest_score)
        self.assertEqual(None, response.guest_foul)
        self.assertEqual("Failed to add the Home team's points.", response.error)
