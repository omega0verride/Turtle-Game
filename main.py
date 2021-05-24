import turtle
import random
import time

# global variables
score = 0
timeLimit = 999999
startTime = time.time()

# screen
screen = turtle.Screen()
screen.tracer(0)  # update delay 0

# add shapes that will be used
screen.addshape("fox.gif")
screen.addshape("coin.gif")


class Label(turtle.Turtle):
    def __init__(self, text="Default Text", x=0, y=0, textcolor="black", align="center",
                 font=("Courier", 15, "normal")):
        super().__init__()
        self.text = text
        self.x = x
        self.y = y
        self.textcolor = textcolor
        self.align = align
        self.font = font
        self.color(textcolor)
        self.hideturtle()
        self.penup()
        self.goto(self.x, self.y)
        self.write(text, align=self.align, font=self.font)

    def setText(self, text):
        self.clear()
        self.write(text, align=self.align, font=self.font)


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("fox.gif")
        self.penup()
        self.speed(0)
        self.setheading(90)

    def moveRight(self):
        (x, y) = self.pos()
        if x < 400:
            self.setx(x + 30)

    def moveLeft(self):
        (x, y) = self.pos()
        if x > -400:
            self.setx(x - 30)

    def moveUp(self):
        if self.ycor() < 400:
            self.forward(30)

    def moveDown(self):
        if self.ycor() > -400:
            self.backward(25)

    def enableMovement(self):
        screen.onkeypress(self.moveUp, "w")
        screen.onkeypress(self.moveLeft, "a")
        screen.onkeypress(self.moveDown, "s")
        screen.onkeypress(self.moveRight, "d")
        screen.onkeypress(self.moveUp, "W")
        screen.onkeypress(self.moveLeft, "A")
        screen.onkeypress(self.moveDown, "S")
        screen.onkeypress(self.moveRight, "D")

    def disableMovement(self):
        screen.onkeypress(self.emptyKeypressHandler, "w")
        screen.onkeypress(self.emptyKeypressHandler, "a")
        screen.onkeypress(self.emptyKeypressHandler, "s")
        screen.onkeypress(self.emptyKeypressHandler, "d")
        screen.onkeypress(self.emptyKeypressHandler, "W")
        screen.onkeypress(self.emptyKeypressHandler, "A")
        screen.onkeypress(self.emptyKeypressHandler, "S")
        screen.onkeypress(self.emptyKeypressHandler, "D")

    def emptyKeypressHandler(self):
        pass


class Coin(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='circle', visible=False)
        self.shape("coin.gif")
        self.color('red')
        self.penup()
        self.showturtle()







#   Questions: ----------------------------------------------------------------------------------------------------------
class Question(turtle.Turtle):
    def __init__(self):
        turtle.Screen.__init__()

        question = Label(
            "How can the Fox get all the coins?\n[1]Using an if statement?\n[2]Using 10 nested if statements?\n[3]Using a for loop until 10",
            0, -180)

        self.time0 = time.time()
        self.i = 0
        self.ans1_ = 0

        self.ans = Label("", 0, -300, "green")
        self.ans2_w = Label("", 0, -320, "green")

        screen.onkeypress(self.ans1, "1")
        screen.onkeypress(self.ans2, "2")
        screen.onkeypress(self.ans3, "3")
        screen.onkeypress(self.ans4, "4")

        self.coins = []
        for i in range(0, 10):
            coin = Coin()
            x = 42 + i * 30
            y = 0
            coin.goto(x, y)
            self. coins.append(coin)

    def amimate(self):
      global score
      for c in self.coins:
        if player0.distance(c) < 30:
          c.clear()
          c.ht()
          self.coins.remove(c)
          score = score + 10
          scoreLabel.setText("Score: {}".format(score))

      if self.ans1_ and self.i < 10:
        if time.time() - self.time0 >= 1:
          self.time0 = time.time()
          player0.moveRight()
          self.ans2_w.setText("\ti = {}".format(self.i + 1))
          self.i = self.i + 1
          print(self.i)



    def ans1(self):
      self.ans.write("Correct! +10 points\n", align="center", font=("Courier", 15, "normal"))
      self.ans1_w = turtle.Turtle()
      self.ans1_w.hideturtle()
      self.ans1_w.penup()
      self.ans1_w.color('green')
      self.ans1_w.goto(0, -320)
      self.ans1_w.write("for (i=1; i<=10; i=i+1)\n", align="center", font=("Courier", 15, "normal"))
      global time0
      time0 = time.time()
      self.ans1_ = 1

    def ans2(self):
      self.wrong_ans(self)

    def ans3(self):
      self.wrong_ans(self)

    def ans4(self):
      self.wrong_ans()

    def wrong_ans(self):
      print("Add wrong answer handler")
# ---------------------------------------------------------------------------------------------------------------------


def GameOver():
    # add game over view
    exit()


if __name__ == "__main__":
    screen.listen()

    timer = Label("Timer: {}".format(timeLimit), 130, 180)
    scoreLabel = Label("Score: {}".format(score), -130, 180)
    player0 = Player()
    player0.enableMovement()

    q1 = Question()

    while True:
        screen.update()

        q1.amimate()

        # countdown
        timeElapsed = int(time.time() - startTime)
        timer.setText("Timer: {}".format(timeLimit - timeElapsed))
        # end game when time finishes
        if timeElapsed >= timeLimit:
            GameOver()
