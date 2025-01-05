import turtle
import random

# Screen setup
wn = turtle.Screen()
wn.title("Arkanoid")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, -200)
ball_dx = 0.2
ball_dy = 0.2

# Create bricks
bricks = []
brick_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(-200, 200, 40):
    for j in range(200, 300, 20):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(random.choice(brick_colors))
        brick.penup()
        brick.goto(i, j)
        bricks.append(brick)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Score
score = 0

# Function to move paddle
def paddle_go_left():
    x = paddle.xcor()
    x -= 20
    if x < -350:
        x = -350
    paddle.setx(x)

def paddle_go_right():
    x = paddle.xcor()
    x += 20
    if x > 350:
        x = 350
    paddle.setx(x)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_go_left, "Left")
wn.onkeypress(paddle_go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball_dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, -200)
        ball_dx = 0.2
        ball_dy = 0.2
        score = 0
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() > 390:
        ball.setx(390)
        ball_dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball_dx *= -1

    # Paddle and ball collisions
    if (ball.xcor() < paddle.xcor() + 50 and ball.xcor() > paddle.xcor() - 50) and (ball.ycor() < paddle.ycor() + 10 and ball.ycor() > paddle.ycor() - 10):
        ball_dy *= -1

    # Brick and ball collisions
    for brick in bricks:
        if (ball.xcor() < brick.xcor() + 20 and ball.xcor() > brick.xcor() - 20) and (ball.ycor() < brick.ycor() + 10 and ball.ycor() > brick.ycor() - 10):
            ball_dy *= -1
            brick.hideturtle()
            bricks.remove(brick)
            score += 10
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    if len(bricks) == 0:
        pen.clear()
        pen.write("You Win!", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball_dx = 0
        ball_dy = 0

wn.mainloop()