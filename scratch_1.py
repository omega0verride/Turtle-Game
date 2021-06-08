import turtle
from PIL import Image
import json
import os


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


def createDB():
    db=open(db_file, 'w+')
    users=[]
    json.dump(users, db)

def addUser(users, username, points=0, time=-1):
    db = open(db_file, 'w')
    user={'username': username, 'points': points, 'time': time}
    users.append(user)
    json.dump(users, db)

def usernameValid(username):
    if len(username):
        file=open(db_file,)
        users=json.load(file)
        print(users)
        found=0
        for u in users:
            if u['username']==username:
                found=1
                break
        if not found:
            addUser(users, username)
            print('Added new user.', users)
            file.close()
            return 1
        return 0
    return 2

def getUsername(x=None, y=None, messgae=None):
    username=turtle.textinput("Username", messgae)
    valid=usernameValid(username)
    if valid==0:
        getUsername(messgae="Username already exists!")
    elif valid==2:
        getUsername(messgae="Username cannot be empty!")


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

    def changeScreen(self, x=None, y=None):
        getUsername(messgae="Please enter a unique username:")
        screen.clear()

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


