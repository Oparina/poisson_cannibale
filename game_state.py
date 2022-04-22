from enum import Enum


class GameState(Enum):
    """
    Créer les états de jeux
    """
    GAME_RUNNING = 0
    GAME_PAUSE = 1
    GAME_OVER = 2
    GAME_MENU = 3
