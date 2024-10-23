from turtle import Turtle


class Ball(Turtle):
    def __init__(self, color: str, speed: int) -> None:
        """
        Class object that creates the ball

        Args:
            color (str): choose color of the ball
            speed (int): choose the speed that the ball goes
        """
        super().__init__()
        self.color(color)
        self.shape("circle")
        self.speed(speed)
        self.penup()
        self.dx = speed
        self.dy = -speed
        self.goto(0, 0)

    def move(self) -> None:
        """Move the ball"""
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_y(self) -> None:
        self.dy *= -1

    def bounce_x(self) -> None:
        self.dx *= -1

    def reset_position(self) -> None:
        """when the game restart so will the ball be in the first position"""
        self.goto(0, 0)
        self.bounce_x()
