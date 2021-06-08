import turtle
import time
from PIL import Image
import os
import getpass


db_dir=os.path.join("C:/Users/", getpass.getuser(), "AppData/Local/PythonGame")
db_filename='database.json'
db_file=os.path.join(db_dir, db_filename)

# global variables
score = 0
timeLimit = 999999
startTime = time.time()

img = Image.open("background.gif")
# print(img.size)
width = img.size[0] + 200
height = img.size[1] + 10
print("w: ", width, " h: ", height, img.size)

def emptyKeypressHandler():
    pass
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
        self.size = size
        self.fill = fill
        self.x = x
        self.y = y
        self.goto(self.x, self.y)
        self.pensize(1)
        self.color('red', 'red')
        if fill:
            self.color('red', 'red')
        else:
            self.fillcolor('red')
        self.begin_fill()

        self.left(140)
        self.forward(111.65 * size)

        self.func()
        self.left(120)
        self.func()

        self.forward(111.65 * size)

        # self.forward(100)
        self.hideturtle()
        self.end_fill()

    def func(self):
        for i in range(200):
            self.right(1)
            self.forward(1 * self.size)


class Lives(turtle.Turtle):
    def __init__(self, num_lives, x, y):
        super().__init__(shape='square', visible=0)
        self.size = 0.15
        self.space = 40
        # print(x)
        self.x = x - num_lives * self.space
        self.y = y - self.size * 240
        # print(x)
        self.numLives = num_lives
        self.currentNumLives = self.numLives
        self.hearts = []
        for i in range(self.numLives):
            h = Heart(self.size, 0, self.x + self.space * i, self.y + 0)
            self.hearts.append(h)

    def add(self):
        index = self.numLives - self.currentNumLives - 1
        if index > -1 and index < self.numLives:
            self.hearts[index] = Heart(self.size, 0, self.x + self.space * index, self.y + 0)
            self.currentNumLives += 1

    def remove(self):
        index = self.numLives - self.currentNumLives
        if index > -1 and index < self.numLives:
            self.hearts[index].clear()
            self.currentNumLives -= 1

    def animateRemove(self):
        for i in range(5):
            screen.ontimer(self.remove, i*200+300)
            screen.ontimer(self.add, i*200+350)
        screen.ontimer(self.remove, 5*200+400)

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
        self.backward(100)

    def jump(self, x, y):
        print("------------")
        jump_duration = 0.2
        start_time = time.time()
        self.forward(100)
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
        screen.onkeypress(emptyKeypressHandler, "w")
        screen.onkeypress(emptyKeypressHandler, "a")
        screen.onkeypress(emptyKeypressHandler, "s")
        screen.onkeypress(emptyKeypressHandler, "d")
        screen.onkeypress(emptyKeypressHandler, "W")
        screen.onkeypress(emptyKeypressHandler, "A")
        screen.onkeypress(emptyKeypressHandler, "S")
        screen.onkeypress(emptyKeypressHandler, "D")



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
        self.position = 0
        self.bgtracker = 0
        self.step = 10
        self.bgArray = []

        for i in range(4):
            self.bg0 = turtle.Turtle(shape='square', visible=1)
            self.bg0.shape("background.gif")
            self.bg0.penup()
            self.bgArray.append(self.bg0)

        self.leftMost = 0
        self.rightMost = 3

        self.bgArray[0].goto(-self.img.size[0], 0)
        self.bgArray[1].goto(0, 0)
        self.bgArray[2].goto(self.img.size[0], 0)
        self.bgArray[3].goto(self.img.size[0] * 2, 0)

        self.enableMovement()

    def moveLeft(self):
        if self.bgtracker < -self.img.size[
            0] + 200:  # add 200 as a spacer on the left to avoid white bg from transition
            self.bgArray[self.rightMost].goto(self.bgArray[self.leftMost].pos()[0] - self.img.size[0], 0)

            self.leftMost = self.rightMost
            self.rightMost -= 1
            if self.rightMost < 0:
                self.rightMost = 3
            self.bgtracker += self.img.size[0]

        if self.position > -30:
            if t!=None:
                for o in t.objects:
                    o.forward(self.step)
            for bg in self.bgArray:
                bg.forward(self.step)
            self.position -= self.step
            self.bgtracker -= self.step

    def moveRight(self, step=None):
        if step==None:
            step=self.step
        self.position += step
        self.bgtracker += step

        if self.bgtracker > self.img.size[0]:
            self.bgArray[self.leftMost].goto(self.bgArray[self.rightMost].pos()[0] + self.img.size[0], 0)
            self.bgtracker -= self.img.size[0]
            self.rightMost = self.leftMost
            self.leftMost += 1
            if self.leftMost > 3:
                self.leftMost = 0

        for bg in self.bgArray:
            bg.backward(step)
        if t != None:
            for o in t.objects:
                o.backward(step)

    def emptyFunc(self):
        print("Movement is disabled")

    def enableMovement(self):
        screen.onkeypress(self.moveLeft, "a")
        screen.onkeypress(self.moveRight, "d")
        screen.onkeypress(self.moveLeft, "A")
        screen.onkeypress(self.moveRight, "D")

    def disableMovement(self):
        screen.onkeypress(self.emptyFunc, "a")
        screen.onkeypress(self.emptyFunc, "d")
        screen.onkeypress(self.emptyFunc, "A")
        screen.onkeypress(self.emptyFunc, "D")


#   Questions: ----------------------------------------------------------------------------------------------------------
class Question0(turtle.Turtle):
    def __init__(self, bg):
        bg.disableMovement()
        turtle.Screen.__init__()

        self.question = Label(
            "How can the Fox get all the coins?\n[1]Using an if statement?\n[2]Using 10 nested if statements?\n[3]Using a for loop until 10",
            0, 60)

        self.wrongAnsLabel=Label("", 0, 25, "red")

        self.coins=t.objects
        self.time0 = time.time()
        self.i = 0
        self.ans1_ = 0

        self.ans2_w = Label("", -20, 70, "green")
        self.enable_answers()

    def enable_answers(self):
        screen.onkeypress(self.ans1, "1")
        screen.onkeypress(self.ans2, "2")
        screen.onkeypress(self.ans3, "3")
        screen.onkeypress(self.ans4, "4")

    def disale_answers(self):
        screen.onkeypress(emptyKeypressHandler, "1")
        screen.onkeypress(emptyKeypressHandler, "2")
        screen.onkeypress(emptyKeypressHandler, "3")
        screen.onkeypress(emptyKeypressHandler, "4")

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
                # player0.moveRight()
                bg.moveRight(30)
                self.ans2_w.setText("\ti = {}".format(self.i+1))
                self.i = self.i + 1
                print(self.i)

    def ans1(self):
        self.disale_answers()
        self.question.color('green')
        self.question.goto(0,100)
        self.question.setText("Correct! +10 points\nfor i in range(1, 10):")
        global time0
        time0 = time.time()
        self.ans1_ = 1
        self.end_question()

    def ans2(self):
        self.wrong_ans()
    def ans3(self):
        self.wrong_ans()
    def ans4(self):
        self.wrong_ans()

    def wrong_ans(self):
        lives.animateRemove()
        self.wrongAnsLabel.setText("Wrong Answer!")
        screen.ontimer(self.wrongAnsLabel.clear, 1000)
        self.end_question()
    def end_question(self):
        pass
    def __del__(self):
        print(0)


# ---------------------------------------------------------------------------------------------------------------------
class QuestionTrigger(turtle.Turtle):
    def __init__(self, pos):
        self.objects = []
        pos=0
        for i in range(0, 10):
            coin = Coin()
            x = pos + i * 30
            y = -100
            coin.goto(x, y)
            self.objects.append(coin)

class QuestionObject(turtle.Turtle):
    def __init__(self, shape):
        super().__init__(visible=False)
        self.shape(shape)
        self.penup()
        self.goto(0, -100)
        self.showturtle()
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
    screen.addshape("stoplight@0.25x.gif")

    screen.listen()

    bg = Wall()
    timer = Label("Timer: {}".format(timeLimit), 130, 180)
    scoreLabel = Label("Score: {}".format(score), -width/2+60, height/2-30, textcolor='orange')
    # stoplight=QuestionObject('stoplight@0.25x.gif')

    lives = Lives(5, width / 2, height / 2)


    run_qustion = 1

    triggers=[QuestionTrigger, None]

    trigger_index = 0
    t=triggers[0](width/2)


    player0 = Player()
    player0.goto(-400, -100)
    while True:
        screen.update()

        print(bg.position)
        if t!=None:
            try:
                if bg.position>t.objects[0].pos()[0]+width-220:
                     if run_qustion:
                         print(0000)
                         run_qustion = 0
                         q1 = Question0(bg)

                     q1.amimate()
            except:
                q1.question.clear()
                q1.ans2_w.clear()
                trigger_index += 1
                t = triggers[trigger_index]
                bg.enableMovement()
                bg.position=0
        # if bgddd.position > 100:


        screen.onkeypress(lives.remove, 'f')
        screen.onkeypress(lives.add, 'g')

        # countdown
        timeElapsed = int(time.time() - startTime)
        timer.setText("Timer: {}".format(timeLimit - timeElapsed))
        # end game when time finishes
        if timeElapsed >= timeLimit:
            GameOver()
