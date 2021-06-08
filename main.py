import turtle
import time
from PIL import Image
import os
import getpass
import json

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
            if game.t!=None:
                for o in game.t.objects:
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
        if game.t != None:
            for o in game.t.objects:
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
            if game.player0.distance(c) < 30:
                c.clear()
                c.ht()
                self.coins.remove(c)
                score = score + 10
                scoreLabel.setText("Score: {}".format(score))

        if self.ans1_ and self.i < 10:
            if time.time() - self.time0 >= 1:
                self.time0 = time.time()
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

class Button(turtle.Turtle):
    def __init__(self, shape):
        super().__init__(visible=False)
        self.shape(shape)
        self.penup()
        self.showturtle()


def updateUser(points=None, time=None):
    db = open(db_file, )
    users = json.load(db)
    username=users[-1]['username']
    if points==None:
        points=users[-1]['points']
    if time==None:
        points=users[-1]['time']
    db = open(db_file, 'w')
    user = {'username': username, 'points': points, 'time': time}
    users[-1]=user
    json.dump(users, db)

class Rules():
    def __init__(self):
        labels=[]
        screen._bgcolor('#121212')
        labels.append(Label("RULES", 0, height/2-45, textcolor='#BB86FC', font=("Comic Sans MS", 20, "bold")))
        labels.append(Label("1. You can use one username only once."
                            "\n2. You use 'A' and 'D' to move forward/backwards."
                            "\n3. Collect as many coins as possible."
                            "\n4. You may face multiple choice questions, choose your answer"
                            "\n    by clicking the corresponding number on your keyboard."
                            "\n5. You have 5 lives."
                            "\n6. You loose 1 life for each wrong answer you choose."
                            "\n7. For each fact you read you gain 1 life, but they are rare.", 0, height/2-300, textcolor='#CF6679', font=("Comic Sans MS", 15, "normal")))
        labels.append(Label("*Press any key to continue", height/2+100, -height/2+50, textcolor='#03DAC6', font=("Comic Sans MS", 12, "normal")))

        # press any key to continue
        screen.onkeyrelease(self.changeScreen, '')
        screen.onclick(self.changeScreen)
        screen.onclick(self.changeScreen, 2)
        screen.onclick(self.changeScreen, 3)

    def addUser(self, username, points=0, time=-1):
        db = open(db_file, 'w')
        user = {'username': username, 'points': points, 'time': time}
        self.users.append(user)
        json.dump(self.users, db)
        print('Added new user.', self.users)

    def usernameValid(self, username):
        if len(username):
            file = open(db_file, )
            self.users = json.load(file)
            found = 0
            for u in self.users:
                if u['username'] == username:
                    found = 1
                    break
            if not found:
                return 1
            return 0
        return 2

    def getUsername(self, x=None, y=None, messgae=None):
        username = turtle.textinput("Username", messgae)
        valid = self.usernameValid(username)
        if valid == 0:
            username=self.getUsername(messgae="Username already exists!")
        elif valid == 2:
            username=self.getUsername(messgae="Username cannot be empty!")
        return username

    def changeScreen(self, x=None, y=None):
        self.username=self.getUsername(messgae="Please enter a unique username:")
        print(self.username)
        self.addUser(self.username)
        screen.clear()
        global startGame
        startGame=1

class leaderBoard():
    def __init__(self):
        labels = []
        screen._bgcolor('#121212')
        labels.append(Label("LeaderBoard", 0, height / 2 - 45, textcolor='#BB86FC', font=("Comic Sans MS", 20, "bold")))

        self.table=turtle.Turtle()
        screen.tracer(0, 0)
        self.table.speed(0)
        w = width - 200 # row length
        h=30 # row height

        db=open(db_file,)
        users = json.load(db)
        users=sorted(users, key=lambda k: k['points'], reverse=True)[0:10]

        self.table.pensize(3)
        self.drawRow(-w/2-20, 150, w, h, color='#CF6679', header=1)
        self.table.pensize(1)
        for i in range(0, len(users)):
            self.drawRow(-w/2-20, 150-(1+i)*h-1, w, h, users[i])

        self.exit_btn_img = Image.open("exit0.gif")
        self.exit_btn_width = self.exit_btn_img.size[0]/2
        self.exit_btn_height = self.exit_btn_img.size[1]/2
        screen.addshape("exit0.gif")
        self.exit_btn = Button('exit0.gif')
        self.exit_btn.goto(width / 2 - 60, -height / 2 + 50)

        self.replay_btn_img = Image.open("replay0.gif")
        self.replay_btn_width = self.replay_btn_img.size[0]/2
        self.replay_btn_height = self.replay_btn_img.size[1]/2
        screen.addshape("replay0.gif")
        self.replay_btn = Button('replay0.gif')
        self.replay_btn.goto(width / 2 - 60, -height / 2 + 110)

        screen.onclick(self.btnClick)

    def btnClick(self, x, y):
        if x<=self.replay_btn.pos()[0]+self.replay_btn_width and x>=self.replay_btn.pos()[0]-self.replay_btn_width and y<=self.replay_btn.pos()[1]+self.replay_btn_height and y>=self.replay_btn.pos()[1]-self.replay_btn_height:
            print("Replay")
            screen.bye()
            Play()
        elif x<=self.exit_btn.pos()[0]+self.exit_btn_width and x>=self.exit_btn.pos()[0]-self.exit_btn_width and y<=self.exit_btn.pos()[1]+self.exit_btn_height and y>=self.exit_btn.pos()[1]-self.exit_btn_height:
            print("Exit")
            screen.bye()

    def drawRow(self, x, y, w, h, user=None, color='white', header=0):
        self.table.hideturtle()
        self.table.penup()
        self.table.goto(x, y)
        self.table.pendown()
        self.table.color(color)


        if header:
            l1=Label("Username", self.table.pos()[0]+0.3*w, self.table.pos()[1]-25, textcolor='white')
            self.table.forward(9 / 15 * w)
            self.table.right(90)
            self.table.forward(h)
            self.table.right(90)
            self.table.forward(9 / 15 * w)
            self.table.right(90)
            self.table.forward(h)
            self.table.right(90)
            self.table.forward(9 / 15 * w)

            l2=Label("Points", self.table.pos()[0]+0.1*w, self.table.pos()[1]-25, textcolor='white')
            self.table.forward(3 / 15 * w)
            self.table.right(90)
            self.table.forward(h)
            self.table.right(90)
            self.table.forward(3 / 15 * w)
            self.table.right(90)
            self.table.forward(h)
            self.table.right(90)
            self.table.forward(3 / 15 * w)

            l3=Label("Time", self.table.pos()[0]+0.1*w, self.table.pos()[1]-25, textcolor='white')
            self.table.forward(3 / 15 * w)
            self.table.right(90)
            self.table.forward(h)
            self.table.right(90)
            self.table.forward(3 / 15 * w)
            self.table.right(90)
            self.table.forward(h)
            self.table.right(90)
            self.table.forward(3 / 15 * w)

        else:
            l3=Label(user['username'], self.table.pos()[0]+0.3*w, self.table.pos()[1]-25, textcolor='white')
            self.table.right(90)
            self.table.forward(h)
            self.table.left(90)
            self.table.forward(9/15*w)
            self.table.left(90)
            self.table.forward(h)

            l3=Label(user['points'], self.table.pos()[0]+0.1*w, self.table.pos()[1]-25, textcolor='white')
            self.table.right(180)
            self.table.forward(h)
            self.table.left(90)
            self.table.forward(3/15*w)
            self.table.left(90)
            self.table.forward(h)

            l3=Label(user['time'], self.table.pos()[0]+0.1*w, self.table.pos()[1]-25, textcolor='white')
            self.table.right(180)
            self.table.forward(h)
            self.table.left(90)
            self.table.forward(3/15*w)
            self.table.left(90)
            self.table.forward(h)

            self.table.left(180)
            self.table.forward(h)
            self.table.right(90)
            self.table.forward(w)
            self.table.right(180)

class GameMode2():
    def __init__(self):
        screen.tracer(0, 0)  # update delay 0
        screen.listen()
        self.bg = Wall()
        self.timer = Label("Timer: {}".format(timeLimit), 130, 180)
        self.scoreLabel = Label("Score: {}".format(score), -width/2+60, height/2-30, textcolor='orange')
        self.lives = Lives(5, width / 2, height / 2)
        screen.onkeypress(self.lives.remove, 'f')
        screen.onkeypress(self.lives.add, 'g')
        run_qustion = 1

        self.triggers=[QuestionTrigger, None]

        trigger_index = 0
        self.t=self.triggers[0](width/2)
        self.player0 = Player()
        self.player0.goto(-400, -100)

class GameMode1():
    def __init__(self):
        screen.tracer(0, 0)  # update delay 0
        screen.listen()
        self.bg = Wall()
        self.timer = Label("Timer: {}".format(timeLimit), 130, 180)
        self.scoreLabel = Label("Score: {}".format(score), -width/2+60, height/2-30, textcolor='orange')
        self.lives = Lives(5, width / 2, height / 2)
        screen.onkeypress(self.lives.remove, 'f')
        screen.onkeypress(self.lives.add, 'g')
        run_qustion = 1

        self.triggers=[QuestionTrigger, None]

        trigger_index = 0
        self.t=self.triggers[0](width/2)
        self.player0 = Player()
        self.player0.goto(-400, -100)



def checkDB():
    if not os.path.exists(db_dir):
        os.mkdir(db_dir)
        print('Created database folder at: ', db_dir)

    if not os.path.exists(db_file):
        db = open(db_file, 'w+')
        users = []
        json.dump(users, db)
        print('Created database.')

def Play():
    global startGame
    startGame=0

    checkDB()

    # screen
    global screen
    screen = turtle.Screen()
    screen.tracer(0, 0)  # update delay 0
    screen.setup(width, height)
    screen.listen()

    rules_screen=Rules()

    screen.addshape("fox.gif")
    screen.addshape("coin.gif")
    screen.addshape("background.gif")



    while True:
        if startGame==1:
            gameStartTime=time.time()
            global game
            game=GameMode1()
            startGame=-1
        if startGame==-1:
            updateUser(None, int(time.time()-gameStartTime))
            # print(game.bg.position)
            if game.bg.position>500:
                # game=GameMode2()
                screen.clear()
                lb=leaderBoard()
                startGame=0
        screen.update()

if __name__ == "__main__":
    Play()


#     # stoplight=QuestionObject('stoplight@0.25x.gif')
#
#
#
#

#
#

#     while True:
#         screen.update()
#
#         print(bg.position)
#         if t!=None:
#             try:
#                 if bg.position>t.objects[0].pos()[0]+width-220:
#                      if run_qustion:
#                          print(0000)
#                          run_qustion = 0
#                          q1 = Question0(bg)
#
#                      q1.amimate()
#             except:
#                 q1.question.clear()
#                 q1.ans2_w.clear()
#                 trigger_index += 1
#                 t = triggers[trigger_index]
#                 bg.enableMovement()
#                 bg.position=0
#         # if bgddd.position > 100:
#
#
#         screen.onkeypress(lives.remove, 'f')
#         screen.onkeypress(lives.add, 'g')
#
#         # countdown
#         timeElapsed = int(time.time() - startTime)
#         timer.setText("Timer: {}".format(timeLimit - timeElapsed))
#         # end game when time finishes
#         if timeElapsed >= timeLimit:
#             GameOver()
