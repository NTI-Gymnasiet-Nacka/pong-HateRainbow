from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

MAX_POINTS: int = 1  # Set the maximum points to win the game
LEFT_PLAYER_NAME: str = "left player"
RIGHT_PLAYER_NAME: str = "right player"
PADDLE_SPEED: int = 20
BALL_SPEED = 5


def main() -> None:
    screen = Screen()
    screen.title("Pong Game")
    screen.bgcolor("white")
    screen.setup(width=1000, height=600)
    screen.tracer()

    left_paddle = Paddle(position=(-400, 0), color="black", paddle_speed=PADDLE_SPEED)

    right_paddle = Paddle(position=(400, 0), color="black", paddle_speed=PADDLE_SPEED)

    ball = Ball(color="blue", speed=BALL_SPEED)

    scoreboard = Scoreboard(
        color="blue",
        max_points=MAX_POINTS,
        left_player_name=LEFT_PLAYER_NAME,
        right_player_name=RIGHT_PLAYER_NAME,
    )

    screen.listen()
    screen.onkeypress(left_paddle.move_up, "w")
    screen.onkeypress(left_paddle.move_down, "s")
    screen.onkeypress(right_paddle.move_up, "Up")
    screen.onkeypress(right_paddle.move_down, "Down")

    game_is_on: bool = True

    while game_is_on:  # while loop to check if the game will continue
        screen.update()
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            # Check if the ball touches the top or bottom of the screen if so it will bounce
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

        # Check for collision with the paddles (hitbox)
        if (ball.xcor() > 360 and ball.xcor() < 370) and (
            ball.ycor() < right_paddle.ycor() + 70
            and ball.ycor() > right_paddle.ycor() - 70
        ):
            ball.bounce_x()

        if (ball.xcor() < -360 and ball.xcor() > -370) and (
            ball.ycor() < left_paddle.ycor() + 70
            and ball.ycor() > left_paddle.ycor() - 70
        ):
            ball.bounce_x()

    screen.exitonclick()


if __name__ == "__main__":
    main()
