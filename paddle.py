from turtle import Turtle


class Paddle(Turtle):
    def __init__(
        self, position: tuple[int, int], color: str, paddle_speed: int
    ) -> None:
        """Class object that creates the paddles

        Args:
            position (tuple[int, int]): Paddle start position can be changed for preference to adjust to different screen size
            color (str): Choose the paddle color
            paddle_speed (int): Choose the speed in which the paddle goes up and down
        """
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=6, stretch_len=2)
        self.penup()
        self.paddle_speed = paddle_speed
        self.goto(position)

    def move_up(self) -> None:
        """Move the paddle up"""
        if self.ycor() < 250:
            self.sety(self.ycor() + self.paddle_speed)

    def move_down(self) -> None:
        """Move the paddle down"""
        if self.ycor() > -250:
            self.sety(self.ycor() - self.paddle_speed)
