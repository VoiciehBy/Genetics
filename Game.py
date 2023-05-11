from enum import Enum


class State(Enum):
    PLAYING = "Playing",
    PAUSED = "Paused",
    BREEDING = "Breeding"


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
    def start_breeding_state():
        if(Game.currentState == State.PLAYING):
            Game.currentState = State.BREEDING

    @staticmethod
    def stop_breeding_state():
        if (Game.currentState == State.BREEDING):
            Game.currentState = State.PLAYING

    @staticmethod
    def is_game_paused() -> bool:
        return Game.currentState == State.PAUSED

    @staticmethod
    def is_in_breeding_state() -> bool:
        return Game.currentState == State.BREEDING

    @staticmethod
    def get_current_state() -> str:
        if(Game.currentState == State.PLAYING):
            return "Playing"
        elif(Game.currentState == State.PAUSED):
            return "Paused"
        elif(Game.currentState == State.BREEDING):
            return "Breeding"
        else:
            return "NoState"
