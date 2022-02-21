import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('red')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

michDistance = random.randrange(1,101)     ## 5. My code
leoDistance = random.randrange(1,101)
michelangelo.down()
leonardo.down()
michelangelo.forward(michDistance)
leonardo.forward(leoDistance)
michelangelo.up()
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

michelangelo.down()
leonardo.down()
num = 10

for i in range(num):
    michDistance = random.randrange(1,101)    
    leoDistance = random.randrange(1,101)
    michelangelo.down()
    leonardo.down()
    michelangelo.forward(michDistance)
    leonardo.forward(leoDistance)

michelangelo.up()
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
michelangelo.clear()
leonardo.clear()

# Part B - complete part B here

num1 = 5
size = 20
sides = [3,4,6,9,12]
leonardo.goto(-120,-30)
leonardo.down()

for i in range(num1):
  for j in range(sides[i]):
    leonardo.forward(size)
    leonardo.left(360/sides[i])
  leonardo.up()
  leonardo.forward(70)
  leonardo.down()
  
window.exitonclick()