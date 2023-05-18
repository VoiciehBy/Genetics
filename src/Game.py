from enum import Enum


class State(Enum):
    PLAYING = "Playing",
    PAUSED = "Paused",
    BREEDING = "Breeding",
    END = "End"


class Game:
    currentState = State.PAUSED
    result = False
    breedingCounter = 0

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
            Game.breedingCounter += 1

    @staticmethod
    def stop_breeding_state():
        if (Game.currentState == State.BREEDING):
            Game.currentState = State.PLAYING

    @staticmethod
    def end_game(was_ai_victorious=False):
        if (Game.currentState in [State.PLAYING, State.BREEDING]):
            Game.currentState = State.END
            Game.result = was_ai_victorious

    @staticmethod
    def is_game_paused() -> bool:
        return Game.currentState == State.PAUSED

    @staticmethod
    def is_game_not_paused() -> bool:
        return Game.currentState != State.PAUSED

    @staticmethod
    def is_game_playing() -> bool:
        return Game.currentState == State.PLAYING

    @staticmethod
    def is_in_breeding_state() -> bool:
        return Game.currentState == State.BREEDING

    @staticmethod
    def is_it_the_end() -> bool:
        return Game.currentState == State.END

    @staticmethod
    def get_current_state() -> str:
        if(Game.currentState == State.PLAYING):
            return "Playing"
        elif(Game.currentState == State.PAUSED):
            return "Paused"
        elif(Game.currentState == State.BREEDING):
            return "Breeding"
        elif (Game.currentState == State.END):
            return "End"
        else:
            return "NoState"
