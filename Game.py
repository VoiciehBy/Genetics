from enum import Enum


class State(Enum):
    PLAYING = "Playing",
    PAUSED = "Paused"


class Game:
    currentState = State.PAUSED

    @staticmethod
    def start_game():
        if(Game.currentState == State.PAUSED):
            Game.currentState = State.PLAYING

    @staticmethod
    def pause_game():
        if(Game.currentState == State.PLAYING):
            Game.currentState = State.PAUSED

    @staticmethod
    def is_game_paused():
        return Game.currentState == State.PAUSED

    @staticmethod
    def get_current_state() -> str:
        if(Game.currentState == State.PLAYING):
            return "Playing"
        elif(Game.currentState == State.PAUSED):
            return "Paused"
        else:
            return "NoState"
