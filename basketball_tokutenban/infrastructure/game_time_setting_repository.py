from basketball_tokutenban.domain.game_time_setting import GameTimeSetting
from basketball_tokutenban.domain.i_game_time_setting_repository import IGameTimeSettingRepository


class GameTimeSettingRepository(IGameTimeSettingRepository):
    """ 試合時間の設定を取得/保存するためのリポジトリ
    """

    def read(self) -> GameTimeSetting:
        # ココでDB/ファイル/RAMなどから取得したプリミティブなデータを
        # ドメインオブジェクトに変換(詰め替え)して返す

        # とりあえず、テキトーな値で試合時間の設定を再構築する
        return GameTimeSetting.reconstruct(10, 2, 20)

    def save(self, setting: GameTimeSetting) -> None:
        # ココでドメインオブジェクトからプリミティブなデータに変換して
        # DB/ファイル/RAMなどに保存する
        pass
