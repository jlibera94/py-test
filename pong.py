import turtle

# Screen setup
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Turns off screen updates

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B (AI)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball_dx = 0.2
ball_dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Score
score_a = 0
score_b = 0

# Function to move paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# AI movement
def ai_movement():
    if ball.ycor() < paddle_b.ycor():
        paddle_b.sety(paddle_b.ycor() - 3)
    elif ball.ycor() > paddle_b.ycor():
        paddle_b.sety(paddle_b.ycor() + 3)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

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
        ball.sety(-290)
        ball_dy *= -1

    # Scorekeeping
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball_dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball_dx *= -1

    # AI movement
    ai_movement()

wn.mainloop()