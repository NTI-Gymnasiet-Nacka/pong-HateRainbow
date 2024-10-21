from time import sleep
from turtle import Screen

from matplotlib.pyplot import delaxes
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


def main() -> None:
    screen = Screen()
    screen.title("Pong Game")
    screen.bgcolor("white")
    screen.setup(width=1000, height=600)
    screen.tracer(0.5, delay=0.01)

    max_points = 5  # Set the maximum points to win the game
    left_paddle = Paddle(position=(-400, 0), color="black")
    right_paddle = Paddle(position=(400, 0), color="black")
    ball = Ball(color="blue", speed=0.5)
    scoreboard = Scoreboard(color="blue", max_points=max_points)

    screen.listen()
    screen.onkeypress(left_paddle.move_up, "w")
    screen.onkeypress(left_paddle.move_down, "s")
    screen.onkeypress(right_paddle.move_up, "Up")
    screen.onkeypress(right_paddle.move_down, "Down")

    game_is_on = True
    while game_is_on:
        screen.update()
        ball.move()

        # Check if the ball touches the top or bottom of the screen
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Check if the ball goes out of bounds on the right side
        if ball.xcor() > 500:
            ball.reset_position()
            scoreboard.left_point()
            if scoreboard.check_winner():
                game_is_on = False

        # Check if the ball goes out of bounds on the left side
        if ball.xcor() < -500:
            ball.reset_position()
            scoreboard.right_point()
            if scoreboard.check_winner():
                game_is_on = False

        # Check for collision with the paddles
        if (ball.xcor() > 360 and ball.xcor() < 370) and \
                (ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50):
            ball.bounce_x()

        if (ball.xcor() < -360 and ball.xcor() > -370) and \
                (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50):
            ball.bounce_x()

    screen.exitonclick()


if __name__ == "__main__":
    main()
