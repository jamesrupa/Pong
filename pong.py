import turtle
import tkinter

sc = turtle.Screen()
sc.title('Pong')
sc.bgcolor('black')
sc.setup(width=800, height=600)
sc.tracer(0)

# Score
scoreOne = 0
scoreTwo = 0


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

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def paddleOne_up():
    y = paddleOne.ycor()
    y += 30
    paddleOne.sety(y)


def paddleOne_down():
    y = paddleOne.ycor()
    y -= 30
    paddleOne.sety(y)


def paddleTwo_up():
    y = paddleTwo.ycor()
    y += 30
    paddleTwo.sety(y)


def paddleTwo_down():
    y = paddleTwo.ycor()
    y -= 30
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
    if paddleOne.ycor() > 250:
        paddleOne.sety(250)

    if paddleTwo.ycor() > 250:
        paddleTwo.sety(250)

    if paddleOne.ycor() < -250:
        paddleOne.sety(-250)

    if paddleTwo.ycor() < -250:
        paddleTwo.sety(-250)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 350:
        scoreOne += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreOne, scoreTwo), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        scoreTwo += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreOne, scoreTwo), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1


    # Collisions
    if ball.xcor() < -340 and ball.ycor() < paddleOne.ycor() + 50 and ball.ycor() > paddleOne.ycor() - 50:
            ball.dx *= -1

    if ball.xcor() > 340 and ball.ycor() < paddleTwo.ycor() + 50 and ball.ycor() > paddleTwo.ycor() - 50:
        ball.dx *= -1

