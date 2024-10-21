from tkinter import CENTER
from turtle import Turtle, bye

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
WIN_FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self, color: str, max_points: int) -> None:
        super().__init__()
        self.color(color)
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.left_score = 0
        self.right_score = 0
        self.max_points = max_points  # Set the maximum points required to win
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f"Left Player: {self.left_score}    Right Player: {self.right_score}",
                   align=ALIGNMENT, font=FONT)

    def left_point(self) -> None:
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self) -> None:
        self.right_score += 1
        self.update_scoreboard()

    def check_winner(self) -> bool:
        """Check if there is a winner and end the game."""
        if self.left_score >= self.max_points:
            self.win_declaration("Left player")
            return True
        elif self.right_score >= self.max_points:
            self.win_declaration("Right player")
            return True
        return False

    def win_declaration(self, player: str) -> None:
        self.goto(0, 0)
        self.clear()
        self.write(f"The winner is {player}", align=CENTER, font=WIN_FONT)
        bye()  # Closes the application
