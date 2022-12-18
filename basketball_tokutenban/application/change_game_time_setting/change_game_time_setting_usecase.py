from basketball_tokutenban.application.change_game_time_setting.change_game_time_setting_request import ChangeGameTimeSettingRequest
from basketball_tokutenban.application.change_game_time_setting.change_game_time_setting_response import ChangeGameTimeSettingResponse
from basketball_tokutenban.domain.i_game_time_setting_repository import IGameTimeSettingRepository


class ChangeGameTimeSettingUseCase:
    """ 試合時間の設定を変更するユースケース
    """

    def __init__(self, setting_repository: IGameTimeSettingRepository) -> None:
        self.__setting_repository = setting_repository

    def execute(self, request: ChangeGameTimeSettingRequest) -> ChangeGameTimeSettingResponse:
        try:
            setting = self.__setting_repository.read()

            setting.change_quarter(request.quarter)
            setting.change_interval(request.interval)
            setting.change_halftime(request.halftime)

            self.__setting_repository.save(setting)

            response = ChangeGameTimeSettingResponse.success(
                setting.quarter,
                setting.interval,
                setting.halftime
            )
            return response

        except Exception as ex:
            response = ChangeGameTimeSettingResponse.failure(str(ex))
            return response
