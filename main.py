import turtle
import random
import time

score = 0
timelimit = 999999
startTime = time.time()

#screen
screen = turtle.Screen()
screen.tracer(0)
screen.addshape("fox.gif")
screen.addshape("coin.gif")

#score
scoreTurtle = turtle.Turtle()
scoreTurtle.hideturtle()
scoreTurtle.penup()
scoreTurtle.goto(-130,180)
scoreTurtle.write("Score: {}".format(score), align ="center",font=("Courier",15,"normal"))

#timer
timer = turtle.Turtle()
timer.hideturtle()
timer.penup()
timer.goto(130,180)
timer.write("Timer: {}".format(timelimit), align ="center", font=("Courier",15,"normal"))

#game over
gameover = turtle.Turtle()
gameover.hideturtle()
gameover.penup()

#player fox
fox = turtle.Turtle()
fox.shape("fox.gif")
fox.penup()
fox.speed(0)
fox.setheading(90)


def moveRight():
  (x,y) = fox.pos()
  if x < 400:
    fox.setx(x+30)

def moveLeft():
  (x,y) = fox.pos()
  if x > -400:
    fox.setx(x-30)

def moveUp():
  if fox.ycor() < 400:
    fox.forward(30)

def moveDown():
  if fox.ycor() > -400:
    fox.backward(25)

class Coin(turtle.Turtle):
  def __init__(self):
    super().__init__(shape='circle', visible=False)
    self.shape("coin.gif")
    self.color('red')
    self.penup()
    self.showturtle()

coins=[]
for i in range(0, 10):
  coin=Coin()
  x = 42+i*30
  y = 0
  coin.goto(x,y)
  coins.append(coin)

#keyboard bindings
screen.listen()
screen.onkeypress(moveRight, "d")
screen.onkeypress(moveLeft,"a")
screen.onkeypress(moveUp,"w")
screen.onkeypress(moveDown,"s")

global time0
time0 = time.time()
global ans1_
ans1_=0

def wrong_ans():
  print("Add wrong answer handler")

def ans1():
  ans.write("Correct! +10 points\n", align ="center",font=("Courier",15,"normal"))
  ans1_w = turtle.Turtle()
  ans1_w.hideturtle()
  ans1_w.penup()
  ans1_w.color('green')
  ans1_w.goto(0, -320)
  ans1_w.write("for (i=1; i<=10; i=i+1)\n", align ="center",font=("Courier",15,"normal"))
  global time0
  time0 = time.time()
  global ans1_
  ans1_=1

def ans2():
  wrong_ans()
def ans3():
  wrong_ans()
def ans4():
  wrong_ans()

screen.onkeypress(ans1,"1")
screen.onkeypress(ans2,"2")
screen.onkeypress(ans3,"3")
screen.onkeypress(ans4,"4")



question = turtle.Turtle()
question.hideturtle()
question.penup()
question.goto(0,-180)
question.write("How can the Fox get all the coins?\n[1]Using an if statement?\n[2]Using 10 nested if statements?\n[3]Using a for loop until 10", align ="center",font=("Courier",15,"normal"))

ans = turtle.Turtle()
ans.hideturtle()
ans.penup()
ans.color('green')
ans.goto(0,-300)
#main game loop

i=0
ans2_w = turtle.Turtle()
ans2_w.hideturtle()
ans2_w.penup()
ans2_w.color('green')
ans2_w.goto(0, -320)



while True:
  screen.update()
  #fox coin collision
  for c in coins:
    if fox.distance(c) < 30:
      c.clear()
      c.ht()
      coins.remove(c)
      score = score + 10
      scoreTurtle.clear()
      scoreTurtle.write("Score: {}".format(score), align ="center",font=("Courier",15,"normal"))

  timeElapsed = int(time.time() - startTime)

  if ans1_ and i<10:
    if time.time() - time0 >= 1:
      time0=time.time()
      moveRight()
      ans2_w.clear()
      ans2_w.write("\ti = {}".format(i + 1), align="center", font=("Courier", 15, "normal"))
      i=i+1
      print(i)

    #countdown
  timer.clear()
  timer.write("Timer: {}".format(timelimit - timeElapsed), align ="center", font=("Courier",15,"normal"))

    #end game when time finishes
  if timeElapsed >= timelimit:
    break