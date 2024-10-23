from time import sleep
from tkinter import CENTER
from turtle import Turtle, bye

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
WIN_FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):
    def __init__(
        self, color: str, max_points: int, left_player_name: str, right_player_name: str
    ) -> None:
        """A class representing scoreboard

        Args:
            color (str): Color of the scoreboard
            max_points (int): how many points per game
            left_player_name (str): left paddle player name
            right_player_name (str): right paddle player name
        """
        super().__init__()
        self.color(color)
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.left_score = 0
        self.right_score = 0
        self.max_points = max_points
        self.left_player_name = left_player_name
        self.right_player_name = right_player_name
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        """update the scoreboard with new score values"""
        self.clear()
        self.write(
            f"Left Player: {self.left_score}    Right Player: {self.right_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def left_point(self) -> None:
        """add a point to the left paddle"""
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self) -> None:
        """add a point to the right paddle"""
        self.right_score += 1
        self.update_scoreboard()

    def check_winner(self) -> bool:
        """
        Check if there is a winner and end the game. \n
        then returns a bool if the game has ended or not
        """
        if self.left_score >= self.max_points:
            self.game_over(self.left_player_name)
            return True

        elif self.right_score >= self.max_points:
            self.game_over(self.right_player_name)
            return True

        return False

    def game_over(self, player: str) -> None:
        """If a player win or lose a game so will it display the winner and also a 'GAME OVER' in the screen

        Args:
            player (str): name of the player that wins
        """
        self.clear()
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER\n{player} won", align=CENTER, font=WIN_FONT)
        sleep(10)
        bye()  # Closes the application
