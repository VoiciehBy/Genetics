from enum import Enum as enum

state = enum("state", ["Playing", "Paused"])


class game:
    currentState = state.Paused

    @staticmethod
    def start_game():
        if(game.currentState == state.Paused):
            game.currentState = state.Playing

    @staticmethod
    def pause_game():
        if(game.currentState == state.Playing):
            game.currentState = state.Paused
    
    @staticmethod
    def getCurrentState() -> str:
        if(game.currentState == state.Playing):
            return "Playing"
        elif(game.currentState == state.Paused):
            return "Paused"
        else:
            return "NoState"
