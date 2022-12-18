from basketball_tokutenban.application.change_game_time_setting.change_game_time_setting_request import ChangeGameTimeSettingRequest
from basketball_tokutenban.application.change_game_time_setting.change_game_time_setting_usecase import ChangeGameTimeSettingUseCase
from basketball_tokutenban.presentation.console.model.game_time_setting_model import GameTimeSettingModel


class GameTimeSettingConrtoller:
    """ 試合時間の設定のコントローラー
    """

    def __init__(
        self,
        change_game_time_setting_usecaase: ChangeGameTimeSettingUseCase
    ) -> None:
        self.__change_game_time_setting_usecaase = change_game_time_setting_usecaase

    def change_game_time_setting(self, quarter: int, interval: int, halftime: int) -> GameTimeSettingModel:
        """ 試合時間の設定を変更する
        """
        request = ChangeGameTimeSettingRequest(quarter, interval, halftime)
        response = self.__change_game_time_setting_usecaase.execute(request)

        model = GameTimeSettingModel(
            response.quarter,
            response.interval,
            response.halftime,
            response.error
        )
        return model
