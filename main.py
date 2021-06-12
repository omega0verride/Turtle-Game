import turtle
import time
from PIL import Image
import os
import getpass
import json
from random import randint
from playsound import playsound
from threading import Thread
import webbrowser

db_filename = 'database.json'
try:
    db_dir = os.path.join("C:/Users/", getpass.getuser(), "AppData/Local/PythonGame")
except:
    db_dir="Files"
db_file = os.path.join(db_dir, db_filename)

# global variables
score = 0
timeLimitGameMode2 = 70
startTime = time.time()

img = Image.open("Files/Images/background.gif")
width = img.size[0] + 200
height = img.size[1] + 10
print("w: ", width, " h: ", height, img.size)


def emptyKeypressHandler(x=None, y=None):
    pass

def playSound(file):
    T = Thread(target=lambda: playsound(file))
    T.start()

def openLink(link):
    webbrowser.open(link, new=1, autoraise=True)

def checkDB():
    if db_dir!="Files":
        try:
            if not os.path.exists(db_dir):
                os.mkdir(db_dir)
                print('Created database folder at: ', db_dir)
        except:
            global db_file
            db_file = db_filename

    if not os.path.exists(db_file):
        db = open(db_file, 'w+')
        users = []
        json.dump(users, db)
        print('Created database.')

def updateUser(points=None, time=None):
    db = open(db_file, )
    users = json.load(db)
    username = users[-1]['username']
    if points == None:
        points = users[-1]['points']
    if time == None:
        points = users[-1]['time']
    db = open(db_file, 'w')
    user = {'username': username, 'points': int(points), 'time': int(time)}
    users[-1] = user
    json.dump(users, db)



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

class Coin(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='circle', visible=False)
        self.shape("Files/Images/coin.gif")
        self.color('red')
        self.penup()
        self.showturtle()
        self.coin_img = Image.open("Files/Images/coin.gif")
        self.coin_width = self.coin_img.size[0] / 2
        self.coin_height = self.coin_img.size[1] / 2

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.step = 20
        self.shape("Files/Images/fox.gif")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.enableJump()

        self.playerImg = Image.open("Files/Images/fox.gif")
        self.player_width = self.playerImg.size[0] / 2
        self.player_height = self.playerImg.size[1] / 2

    def moveRight(self):
        (x, y) = self.pos()
        if x < width / 2 - 50:
            self.shape("Files/Images/fox.gif")
            self.setx(x + self.step)

    def moveLeft(self):
        (x, y) = self.pos()
        if x > -width / 2 + 40:
            self.shape("Files/Images/foxflipped.gif")
            self.setx(x - self.step)

    def moveUp(self):
        if self.ycor() < height / 2:
            self.forward(self.step)

    def moveDown(self):
        if self.ycor() > -height / 2 + 160:
            self.backward(self.step)

    def jumpBack(self):
        self.backward(100)

    def jump(self, x, y):
        self.forward(100)
        screen.ontimer(self.jumpBack, 200)

    def enableJump(self):
        screen.onclick(self.jump)

    def disableJump(self):
        screen.onclick(emptyKeypressHandler)

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

class Heart(turtle.Turtle):
    def __init__(self, size, x, y):
        super().__init__(visible=1)
        self.penup()
        self.size = size
        self.x = x
        self.y = y
        self.goto(self.x, self.y)
        self.pensize(1)
        self.color('red', 'red')
        self.begin_fill()
        self.left(140)
        self.forward(111.65 * size)
        self.func()
        self.left(120)
        self.func()
        self.forward(111.65 * size)
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
        self.x = x - num_lives * self.space
        self.y = y - self.size * 240
        self.numLives = num_lives
        self.constNumLives = num_lives
        self.currentNumLives = self.numLives
        self.hearts = []
        for i in range(self.numLives):
            h = Heart(self.size, self.x + self.space * i, self.y + 0)
            self.hearts.append(h)

    def addManually(self):
        playSound('Files\Audio\extralife.mp3')
        self.numLives+=1
        self.currentNumLives += 1
        self.hearts.insert(0, Heart(self.size, self.hearts[0].pos()[0] - self.space, self.y + 0))

    def add(self):
        if len(self.hearts):
            self.currentNumLives += 1
            self.hearts.insert(0, Heart(self.size, self.hearts[0].pos()[0] - self.space, self.y + 0))

    def remove(self):
        if len(self.hearts):
            self.hearts[0].clear()
            self.hearts.pop(0)
            self.currentNumLives -= 1

    def animateRemove(self):
        playSound('Files\Audio\health.mp3')
        for i in range(5):
            screen.ontimer(self.remove, i*200+300)
            screen.ontimer(self.add, i*200+350)
        screen.ontimer(self.remove, 5*200+400)

class leaderBoard():
    def __init__(self):
        updateUser(score, time.time()-startTime)

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

        self.exit_btn_img = Image.open("Files/Images/exit0.gif")
        self.exit_btn_width = self.exit_btn_img.size[0]/2
        self.exit_btn_height = self.exit_btn_img.size[1]/2
        screen.addshape("Files/Images/exit0.gif")
        self.exit_btn = Button('Files/Images/exit0.gif')
        self.exit_btn.goto(width / 2 - 60, -height / 2 + 50)

        self.replay_btn_img = Image.open("Files/Images/replay0.gif")
        self.replay_btn_width = self.replay_btn_img.size[0]/2
        self.replay_btn_height = self.replay_btn_img.size[1]/2
        screen.addshape("Files/Images/replay0.gif")
        self.replay_btn = Button('Files/Images/replay0.gif')
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
    def update(self):
        pass



class StartScene():
    def __init__(self):
        labels=[]
        screen._bgcolor('#121212')
        labels.append(Label("RULES", 0, height/2-45, textcolor='#BB86FC', font=("Comic Sans MS", 20, "bold")))
        labels.append(Label("1. You can use one username only once."
                            "\n2. You use 'A' and 'D' to move forward/backwards."
                            "\n3. You may face multiple choice questions, choose your answer"
                            "\n    by clicking the corresponding number on your keyboard."
                            "\n4. With each correct answer you gain 10 points."
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
        global scene
        scene=1


class Wall(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square', visible=0)
        self.img = Image.open("Files/Images/background.gif")
        self.position = 0
        self.bgtracker = 0
        self.step = 10
        self.bgArray = []

        for i in range(4):
            self.bg0 = turtle.Turtle(shape='square', visible=1)
            self.bg0.shape("Files/Images/background.gif")
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
            if game.currQuestion!=None:
                for o in game.currQuestion.objects:
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
        if game.currQuestion != None:
            for o in game.currQuestion.objects:
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



# ---------------------------------------------------------------------------------------------------------------------
class coinsArray():
    def __init__(self, baseclass, pos, shape=None):
        self.baseclass=baseclass
        self.image_width = 0
        self.image_height = 0
        self.objects = []
        self.pos=pos
        self.i=0
        for i in range(0, 10):
            coin = Coin()
            x = pos + i * 30
            y = -100
            coin.goto(x, y)
            self.objects.append(coin)

    def removeObject(self):
        if len(self.objects):
            playSound('Files/Audio/coin.wav')
            self.baseclass.bg.moveRight(30)
            c = self.objects[0]
            c.clear()
            c.ht()
            self.objects.remove(c)
            self.baseclass.ans0.setText("for i in range(0, 10):\n\ti = {}".format(self.i))
            self.i=self.i+1
            screen.ontimer(self.removeObject, 1000)

    def animate(self):
        if len(self.objects):
            self.baseclass.ans0=Label("", 0, 100, textcolor='green')
            self.removeObject()

class QuestionObject(turtle.Turtle):
    def __init__(self, shape, pos):
        super().__init__(visible=False)
        self.shape(shape)
        self.penup()
        self.goto(pos, -100)
        self.showturtle()

class ObjectPoint():
    def __init__(self, baseclass, pos, shape=None):
        self.baseclass=baseclass
        self.pos=pos
        self.objects = []
        screen.addshape(shape)
        if shape!=None:
            self.img = Image.open(shape)
            self.image_width = self.img.size[0] / 2
            self.image_height = self.img.size[1] / 2
        else:
            self.image_width=0
            self.image_height=0
        self.objects.append(QuestionObject(shape, width/2))

    def animate(self):
        for i in range(0, 10):
            screen.ontimer(lambda: self.baseclass.bg.moveRight(10), i*50)
        self.objects[0].hideturtle()
        self.objects.pop(0)

class GameMode1():
    def __init__(self):
        screen.tracer(0, 0)  # update delay 0
        screen.listen()

        self.bg = Wall()
        self.scoreLabel = Label("Score: {}".format(score), int(-width/2+60), height/2-30, textcolor='orange')


        self.questions=[[["How can the Fox get all the coins?", "\n[1]Using an if statement", "\n[2]Using 10 nested if statements", "\n[3]Using a for loop until 10", 3], [coinsArray, None], 0],
                        [["How can the fox check if the light is green.", "\n[1]Using an if statement", "\n[2]Using a for loop", "\n[3]Using an array", 1], [ObjectPoint, "Files/Images/stoplight@0.25x.gif"], 0],
                        [["What do we get if we convert the number 65 to a character? \nprint(chr(65))", "\n[1]The number 65", "\n[2]An error", "\n[3]The letter A", 3], [ObjectPoint, "Files/Images/ascii.gif"], 0],
                        [["Did you know that computer codes had an important role in ending WWII", "https://www.iwm.org.uk/history/how-alan-turing-cracked-the-enigma-code"], [ObjectPoint, 'Files/Images/facts.gif'], 1]]
        self.factsNum=1 # facts must always be inserted at the end

        self.onQuestion=0
        self.running=1

        self.lives = Lives(5, width / 2, height / 2)
        self.player0 = Player()
        self.player0.goto(-400, -100)


        self.index = randint(0, len(self.questions) - 1-self.factsNum) # randomly select question but make sure the first one is not a fact
        self.question=self.questions[self.index]
        self.currQuestion=self.question[1][0](self, width/2, self.question[1][1])

    def endFact(self):
        self.questionLabel.color('green')
        self.questionLabel.setText("You won 1 life!")
        openLink(self.question[0][-1])
        self.player0.enableJump()
        self.player0.enableMovement()
        self.bg.enableMovement()
        self.lives.addManually()
        self.ans = None
        screen.ontimer(self.questionLabel.clear, 1000)
        screen.ontimer(self.currQuestion.animate, 1000)

    def generateFact(self):
        self.player0.disableMovement()
        self.player0.disableJump()
        self.bg.disableMovement()
        s=self.questions[self.index][0][0]
        print(s)
        self.questionLabel = Label(s, 0, 0 + 100, "black")
        screen.ontimer(self.endFact, 3000)

    def generateQuestion(self):
        if len(self.questions):
            self.player0.disableMovement()
            self.player0.disableJump()
            self.bg.disableMovement()
            q = ''.join(self.questions[self.index][0][0:len(self.questions[self.index][0]) - 1])
            print(q)
            if len(self.questions[self.index][0][0].split("\n"))==1:
                self.questionLabel = Label(q, 0, 0 + 85, "black")
            else:
                self.questionLabel = Label(q, 0, 50, "black")
            self.enable_answers()
        else:
            print("OUT of Questions!")
            global score
            score+=10
            if self.ans == None:
                playSound('Files\Audio\completed.mp3')
                self.player0.disableMovement()
                self.player0.disableJump()
                self.bg.disableMovement()
                self.ans = Label("You finished all questions!", 0, 0, textcolor="red", font=("Comic Sans MS", 30, "bold"))
                screen.ontimer(self.changeScene, 4000)

    def clearMessage(self):
        self.ans0.clear()
        self.enable_answers()

    def checkAns(self, choice):
        self.disable_answers()
        if choice == self.questions[self.index][0][-1]:
            playSound('Files\Audio\correct.mp3')
            self.ans0 = Label("")
            self.ans = Label("Correct!", 0, 50, "green")
            global score
            score+=10
            self.scoreLabel.setText("Score: {}".format(score))
            screen.ontimer(self.endQuestion, 1500)
        else:
            self.ans0 = Label("Wrong!", 0, 50, "red")
            self.lives.animateRemove()
            screen.ontimer(self.clearMessage, 1500)

    def endQuestion(self):
        self.disable_answers()
        self.questionLabel.clear()
        self.ans.clear()
        self.ans = None

        self.currQuestion.animate()


    def enable_answers(self):
        screen.onkeypress(lambda: self.checkAns(1), "1")
        screen.onkeypress(lambda: self.checkAns(2), "2")
        screen.onkeypress(lambda: self.checkAns(3), "3")
        screen.onkeypress(lambda: self.checkAns(4), "4")

    def disable_answers(self):
        screen.onkeypress(emptyKeypressHandler, "1")
        screen.onkeypress(emptyKeypressHandler, "2")
        screen.onkeypress(emptyKeypressHandler, "3")
        screen.onkeypress(emptyKeypressHandler, "4")

    def exitPrep(self):
        try:
            self.ans.clear()
        except:
            pass
        try:
            self.ans0.clear()
        except:
            pass
        try:
            self.questionLabel.clear()
        except:
            pass
        self.disable_answers()
        self.bg.disableMovement()
        self.player0.disableJump()

    def changeScene(self):
        global scene
        scene = 2

    def outOfLives(self):
        self.exitPrep()
        self.label = Label("You Lost All Your Lives!", 0, 0, textcolor="red", font=("Comic Sans MS", 30, "bold"))
        screen.ontimer(self.changeScene, 3000)

    def update(self):
        if self.currQuestion!=None:
            if len(self.currQuestion.objects)==0:
                self.ans0.clear()
                self.bg.enableMovement()
                self.player0.enableJump()
                self.onQuestion = 0
                self.bg.position=0

                self.questions.pop(self.index)
                if len(self.questions):
                    self.index = randint(0, len(self.questions) - 1)
                    self.question = self.questions[self.index]
                    if self.question[2]==1:
                        self.currQuestion = self.question[1][0](self, width / 2, self.question[1][1])
                    else:
                        self.currQuestion = self.question[1][0](self, width / 2, self.question[1][1])
                else:
                   self.currQuestion = ObjectPoint(self, width / 2, 'Files/Images/finishPoint@0.25x.gif')
                   self.question=[0,0,0]


        if not self.onQuestion:
            if self.bg.position>=self.currQuestion.pos+abs(self.player0.pos()[0]+self.player0.player_width+20)-self.currQuestion.image_width:
                playSound("Files/Audio/object.mp3")
                self.bg.position=0
                self.onQuestion=1
                if self.question[2]:
                    self.generateFact()
                else:
                    self.generateQuestion()
        if self.running:
            if self.lives.currentNumLives <= 0:
                self.running=False
                self.outOfLives()

class RulesGameMode2():
    def __init__(self):
        screen.tracer(0, 0)  # update delay 0
        screen.listen()
        labels=[]
        screen._bgcolor('#121212')
        labels.append(Label("RULES", 0, height/2-45, textcolor='#BB86FC', font=("Comic Sans MS", 20, "bold")))
        labels.append(Label("1. Use W,A,S,D to move around."
                            "\n2. Collect as many coins as possible."
                            "\n3. You can answer a question only once."
                            "\n4. For each correct answer you get +10 points."
                            "\n5. You have 5 lives."
                            "\n6. For each wrong answer you lose 1 life."
                            "\n7. If the time ends or you lose all your lives the game ends."
                            "\n8. If you answer all the questions before the timer you can move "
                            "\n   freely and gather coins with a value of +1."
                            "\n9. For each fact you read you gain 1 life, but they are rare.", 0, height/2-350, textcolor='#CF6679', font=("Comic Sans MS", 15, "normal")))
        labels.append(Label("*Press any key to continue", height/2+100, -height/2+20, textcolor='#03DAC6', font=("Comic Sans MS", 12, "normal")))

        self.doubleClicked=0
        # press any key to continue
        screen.onkeyrelease(self.changeScreen, '')
        screen.onclick(self.changeScreen)
        screen.onclick(self.changeScreen, 2)
        screen.onclick(self.changeScreen, 3)

    def changeScreen(self, x=None, y=None):
        if self.doubleClicked:
            screen.clear()
            global scene
            scene=3
        self.doubleClicked+=1

class GameMode2():
    def __init__(self):
        self.questionHeight = 200
        self.width = width
        self.height = height + self.questionHeight
        screen.setup(self.width, self.height)
        screen.tracer(0, 0)  # update delay 0
        screen.listen()
        screen.bgcolor('#121212')
        self.startTime = time.time()
        self.timer = Label("Timer: {}".format(timeLimitGameMode2), 130, self.height / 2 - 30, textcolor='red')
        self.scoreLabel = Label("Score: {}".format(score), -self.width / 2 + 60, self.height / 2 - 30, textcolor='orange')
        self.lives = Lives(5, self.width / 2, self.height / 2)

        self.running=True

        self.currentCoins = 0
        # self.currentQuestionRand=randint(2, 8)
        self.currentQuestionRand = 1

        self.line = turtle.Turtle()
        self.line.pencolor('white')
        self.line.penup()
        self.line.hideturtle()
        self.line.goto(-self.width / 2, -self.height / 2 + self.questionHeight)
        self.line.pendown()
        self.line.forward(self.width)

        self.coin = Coin()

        self.player0 = Player()
        self.moveCoinToRandLocation()
        self.player0.enableMovement()
        self.questions = [
            ["How do you access the first element of an array?", "\n[1] array[]", "\n[2] array[0]", "\n[3] array[1]", 2],
            ["The action of doing something over and over again, repeating code?", "\n[1] Program", "\n[2] Bug", "\n[3] Loop", "\n[4] Code", 3],
            ["A set of instructions that can be performed with or without a computer:", "\n[1] Bug", "\n[2] Debug", "\n[3] Loop", "\n[4] Algorithm", 4],
            ["An error, or mistake, that prevents the program from being run correctly:", "\n[1] Bug", "\n[2] Debug", "\n[3] Loop", "\n[4] Algorithm", 1],
            ["Finding and fixing errors or mistakes in programs:", "\n[1] Sequencing", "\n[2] Debugging", "\n[3] Looping", "\n[4] Decomposing", 2]
        ]

    def moveCoinToRandLocation(self):
        self.coin.goto(randint(-self.width / 2 + 30, self.width / 2 - 30), randint(-self.height / 2 + 25 + self.questionHeight, self.height / 2 - 45 - int(self.coin.coin_height)))
        if self.player0.pos()[0] - self.player0.player_width <= self.coin.pos()[0] + self.coin.coin_width and self.player0.pos()[0] + self.player0.player_width >= self.coin.pos()[0] - self.coin.coin_width and \
                self.coin.pos()[1] + self.player0.player_height >= self.player0.pos()[1] >= self.coin.pos()[1] - self.player0.player_height: #make sure the coin does not go to the same location as before
            self.moveCoinToRandLocation()

    def generateQuestion(self):
        playSound('Files/Audio/coin.wav')
        if len(self.questions):
            self.player0.disableMovement()
            self.player0.disableJump()
            self.index = randint(0, len(self.questions) - 1)
            q = ''.join(self.questions[self.index][0:len(self.questions[self.index]) - 1])
            print(q)
            self.question = Label(q, 0, -height / 2 - 25, "white")
            self.enable_answers()
        else:
            print("OUT of Questions!")
            global score
            score+=1
            if self.ans == None:
                self.ans = Label("You finished all questions!\nCollect as many coins as you want.", 0, -height / 2, "gold")
                playSound('Files\Audio\completed.mp3')

    def endQuestion(self):
        self.question.clear()
        self.ans.clear()
        self.ans = None
        self.ans0.clear()
        self.questions.pop(self.index)
        self.player0.enableMovement()
        self.player0.enableJump()

    def checkAns(self, choice):
        if choice == self.questions[self.index][-1]:
            self.disable_answers()
            playSound('Files\Audio\correct.mp3')
            self.ans0 = Label("")
            self.ans = Label("Correct!", 0, -height / 2 - 50, "green")
            global score
            score+=10
            screen.ontimer(self.endQuestion, 1500)
        else:
            self.disable_answers()
            self.ans0 = Label("Wrong!", 0, -height / 2 - 50, "red")
            self.ans = Label("Correct answer: " + self.questions[self.index][self.questions[self.index][-1]].lstrip('\n'), 0, -height / 2 - 70, "green")
            self.lives.animateRemove()
            screen.ontimer(self.endQuestion, 2000)

    def enable_answers(self):
        screen.onkeypress(lambda: self.checkAns(1), "1")
        screen.onkeypress(lambda: self.checkAns(2), "2")
        screen.onkeypress(lambda: self.checkAns(3), "3")
        screen.onkeypress(lambda: self.checkAns(4), "4")

    def disable_answers(self):
        screen.onkeypress(emptyKeypressHandler, "1")
        screen.onkeypress(emptyKeypressHandler, "2")
        screen.onkeypress(emptyKeypressHandler, "3")
        screen.onkeypress(emptyKeypressHandler, "4")

    def exitPrep(self):
        try:
            self.ans.clear()
        except:
            pass
        try:
            self.ans0.clear()
        except:
            pass
        try:
            self.question.clear()
        except:
            pass
        self.disable_answers()
        self.player0.disableMovement()
        self.player0.disableJump()

    def changeScene(self):
        global scene
        scene = 5

    def ranOutOfTime(self):
        print("Out of time")
        playSound("Files/Audio/finish.mp3")
        self.exitPrep()
        self.label=Label("Your Time Is Over!", 0, -height/2, textcolor="red", font=("Comic Sans MS", 30, "bold"))
        screen.ontimer(self.changeScene, 3000)

    def outOfLives(self):
        print("Out of lives")
        self.exitPrep()
        playSound("Files/Audio/finish.mp3")
        self.label=Label("You Lost All Your Lives!", 0, -height/2, textcolor="red", font=("Comic Sans MS", 30, "bold"))
        screen.ontimer(self.changeScene, 3000)


    def update(self):
        self.scoreLabel.setText("Score: {}".format(score))
        self.currentTimerVal=timeLimitGameMode2 - int(time.time() - self.startTime)
        if self.currentTimerVal>=0:
            self.timer.setText("Timer: {}".format(self.currentTimerVal))
        if self.player0.pos()[0] - self.player0.player_width <= self.coin.pos()[0] + self.coin.coin_width and self.player0.pos()[0] + self.player0.player_width >= self.coin.pos()[0] - self.coin.coin_width and \
                self.coin.pos()[1] + self.player0.player_height >= self.player0.pos()[1] >= self.coin.pos()[1] - self.player0.player_height:
            self.moveCoinToRandLocation()
            self.currentCoins += 1
            if self.currentCoins >= self.currentQuestionRand:
                # self.currentQuestionRand=randint(2, 8)
                self.currentQuestionRand = 1
                self.generateQuestion()
                self.currentCoins = 0
        if self.running:
            if (self.currentTimerVal) <= 0:
                self.running=False
                self.ranOutOfTime()
            if self.lives.currentNumLives <= 0:
                self.running=False
                self.outOfLives()


def Play():
    checkDB()

    # Screen setup
    global screen
    screen = turtle.Screen()
    screen.bgcolor('#121212')
    screen.tracer(0, 0)  # update delay 0
    screen.setup(width, height)
    screen.cv._rootwindow.resizable(False, False)
    screen.listen()


    screen.addshape("Files/Images/fox.gif")
    screen.addshape("Files/Images/foxflipped.gif")
    screen.addshape("Files/Images/coin.gif")
    screen.addshape("Files/Images/background.gif")

    rulesScreen=StartScene()

    # Current game scene
    global scene, game
    scene=0

    while True:
        try:
            game.update()
        except:
            pass
        screen.update()

        if scene==1:
            scene=-1
            gameStartTime=time.time()
            game=GameMode1()
        if scene==2:
            scene=0
            screen.clear()
            game=RulesGameMode2()
        if scene==3:
            scene=0
            screen.clear()
            game=GameMode2()
        if scene==5:
            scene=0
            screen.clear()
            screen.setup(width, height)
            game=leaderBoard()

if __name__ == "__main__":
    Play()