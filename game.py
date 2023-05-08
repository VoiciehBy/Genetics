from enum import Enum


class state(Enum):
    PLAYING = "Playing",
    PAUSED = "Paused"


class game:
    currentState = state.PAUSED

    @staticmethod
    def start_game():
        if(game.currentState == state.PAUSED):
            game.currentState = state.PLAYING

    @staticmethod
    def pause_game():
        if(game.currentState == state.PLAYING):
            game.currentState = state.PAUSED

    @staticmethod
    def isGamePaused():
        return game.currentState == state.PAUSED

    @staticmethod
    def getCurrentState() -> str:
        if(game.currentState == state.PLAYING):
            return "Playing"
        elif(game.currentState == state.PAUSED):
            return "Paused"
        else:
            return "NoState"
