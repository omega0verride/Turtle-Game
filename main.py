import turtle
import random
import time
from PIL import Image
import keyboard

# global variables
score = 0
timeLimit = 999999
startTime = time.time()

img = Image.open("background.gif")
# print(img.size)
width=img.size[0]+200
height=img.size[1]+10
print("w: ", width, " h: ", height, img.size)

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

class Heart(turtle.Turtle):
    def __init__(self, size, fill, x, y):
        super().__init__(visible=1)
        self.penup()
        self.size=size
        self.fill=fill
        self.x=x
        self.y=y
        self.goto(self.x, self.y)
        self.pensize(1)
        self.color('red', 'red')
        # if fill:
        #     self.color('red', 'red')
        # else:
        #     self.fillcolor('red')
        self.begin_fill()

        self.left(140)
        self.forward(111.65*size)

        self.func()
        self.left(120)
        self.func()

        self.forward(111.65*size)

        #self.forward(100)
        self.hideturtle()
        self.end_fill()

    def func(self):
        for i in range(200):
            self.right(1)
            self.forward(1*self.size)

class Lives(turtle.Turtle):
    def __init__(self, num_lives, x, y):
        super().__init__(shape='square', visible=0)
        self.size = 0.15
        self.space=40
        # print(x)
        self.x=x-num_lives*self.space
        self.y=y-self.size*240
        # print(x)
        self.numLives=num_lives
        self.currentNumLives=self.numLives
        self.hearts=[]
        for i in range(self.numLives):
            h=Heart(self.size, 0, self.x+self.space*i, self.y+0)
            self.hearts.append(h)

    def add(self):
        index=self.numLives-self.currentNumLives-1
        if index>-1 and index<self.numLives:
            self.hearts[index]=Heart(self.size, 0, self.x+self.space*index, self.y+0)
            self.currentNumLives+=1
    def remove(self):
        index=self.numLives-self.currentNumLives
        if index > -1 and index < self.numLives:
            self.hearts[index].clear()
            self.currentNumLives-=1


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("fox.gif")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.enableJump()

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

    def moveDown(self):
        self.backward(40)

    def jump(self, x, y):
        print("------------")
        jump_duration=0.2
        start_time=time.time()
        self.forward(40)
        screen.update()
        screen.ontimer(self.moveDown, 200)
        # while 1:
        #     if time.time()>=start_time+jump_duration:
        #         self.backward(30)
        #         print('======')
        #         break
    def enableJump(self):
        screen.onclick(self.jump)
        # screen.onkeypress(self.jump, "space")

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

class Wall(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square', visible=0)
        self.img = Image.open("background.gif")
        # print(self.img.size)
        self.position=0
        self.bgtracker=0
        self.step=30
        self.bgArray=[]

        for i in range(4):
            self.bg0=turtle.Turtle(shape='square', visible=1)
            self.bg0.shape("background.gif")
            self.bg0.penup()
            self.bgArray.append(self.bg0)

        self.leftMost=0
        self.rightMost=3

        self.bgArray[0].goto(-self.img.size[0], 0)
        self.bgArray[1].goto(0, 0)
        self.bgArray[2].goto(self.img.size[0], 0)
        self.bgArray[3].goto(self.img.size[0]*2, 0)

        self.enableMovement()



    def moveLeft(self):
        if self.bgtracker<-self.img.size[0]+200: # add 200 as a spacer on the left to avoid white bg from transition
            self.bgArray[self.rightMost].goto(self.bgArray[self.leftMost].pos()[0]-self.img.size[0], 0)

            self.leftMost=self.rightMost
            self.rightMost-=1
            if self.rightMost<0:
                self.rightMost=3
            self.bgtracker+=self.img.size[0]

        if self.position>-30:
            for bg in self.bgArray:
                bg.forward(self.step)
            self.position-=self.step
            self.bgtracker-=self.step

    def moveRight(self):
        self.position += self.step
        self.bgtracker += self.step

        if self.bgtracker>self.img.size[0]:
            self.bgArray[self.leftMost].goto(self.bgArray[self.rightMost].pos()[0]+self.img.size[0], 0)
            self.bgtracker-=self.img.size[0]
            self.rightMost=self.leftMost
            self.leftMost+=1
            if self.leftMost>3:
                self.leftMost=0

        for bg in self.bgArray:
            bg.backward(self.step)


    def enableMovement(self):
        screen.onkeypress(self.moveLeft, "a")
        screen.onkeypress(self.moveRight, "d")
        screen.onkeypress(self.moveLeft, "A")
        screen.onkeypress(self.moveRight, "D")


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
    # screen
    screen = turtle.Screen()
    screen.tracer(0, 0)  # update delay 0
    screen.setup(width, height)


    # add shapes that will be used
    screen.addshape("fox.gif")
    screen.addshape("coin.gif")
    screen.addshape("background.gif")

    screen.listen()

    bg = Wall()
    timer = Label("Timer: {}".format(timeLimit), 130, 180)
    scoreLabel = Label("Score: {}".format(score), -130, 180)
    player0 = Player()
    player0.goto(-400, -100)
    #q1 = Question()
    lives = Lives(5, width/2, height/2)
    while True:
        screen.update()
        #q1.amimate()
        screen.onkeypress(lives.remove, 'f')
        screen.onkeypress(lives.add, 'g')
        # countdown
        timeElapsed = int(time.time() - startTime)
        timer.setText("Timer: {}".format(timeLimit - timeElapsed))
        # end game when time finishes
        if timeElapsed >= timeLimit:
            GameOver()
