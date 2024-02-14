from pc_game.config import Config
from pc_game.game_ui import GameUI
from pc_game.key_press import KeyPress
from pc_game.settings_window import SettingsWindow


class Game:
    def __init__(self):
        # TODO define the parameters : 
        self.config = Config()
        # TODO define the parameters : 
        self.game_ui = GameUI()
        # TODO define the parameters : 
        self.settings_window = SettingsWindow()
        # TODO define the parameters : 
        self.key_press = KeyPress()
        self._config_game = None
        self._key_press = None

    def _create_game_ui(self, ):
        # TODO : Complete method content
        pass

    def _create_config_window(self, ):
        # TODO : Complete method content
        pass

    def lost_game(self, ):
        # TODO : Complete method content
        pass

    def winning_the_game(self, ):
        # TODO : Complete method content
        pass

    def restart_game(self, ):
        # TODO : Complete method content
        pass

    def close_game(self, ):
        # TODO : Complete method content
        pass

    def start_game(self, ):
        # TODO : Complete method content
        pass

    def continue_game(self, ):
        # TODO : Complete method content
        pass

    def pause_game(self, ):
        # TODO : Complete method content
        pass
