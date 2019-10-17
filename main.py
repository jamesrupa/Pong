import turtle

sc = turtle.Screen()
sc.title('Pong')
sc.bgcolor('black')
sc.setup(width=800, height=600)
sc.tracer(0)

# Paddle 1
paddleOne = turtle.Turtle()
paddleOne.speed(0)
paddleOne.shape('square')
paddleOne.shapesize(stretch_wid=5, stretch_len=1)
paddleOne.color('white')
paddleOne.penup()
paddleOne.goto(-350, 0)


# Paddle 2
paddleTwo = turtle.Turtle()
paddleTwo.speed(0)
paddleTwo.shape('square')
paddleTwo.shapesize(stretch_wid=5, stretch_len=1)
paddleTwo.color('white')
paddleTwo.penup()
paddleTwo.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1


# Functions
def paddleOne_up():
    y = paddleOne.ycor()
    y += 20
    paddleOne.sety(y)


def paddleOne_down():
    y = paddleOne.ycor()
    y -= 20
    paddleOne.sety(y)


def paddleTwo_up():
    y = paddleTwo.ycor()
    y += 20
    paddleTwo.sety(y)


def paddleTwo_down():
    y = paddleTwo.ycor()
    y -= 20
    paddleTwo.sety(y)


sc.listen()
sc.onkeypress(paddleOne_up, 'w')
sc.onkeypress(paddleOne_down, 's')
sc.onkeypress(paddleTwo_up, 'Up')
sc.onkeypress(paddleTwo_down, 'Down')


# Game loop
while True:
    sc.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1


    # Collisions
    if ball.xcor() < -340 and ball.ycor() < paddleOne.ycor() + 50 and ball.ycor() > paddleOne.ycor() - 50:
            ball.dx *= -1

    if ball.xcor() > 340 and ball.ycor() < paddleTwo.ycor() + 50 and ball.ycor() > paddleTwo.ycor() - 50:
        ball.dx *= -1

