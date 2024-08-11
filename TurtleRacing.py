import turtle
import time
import random

WIDTH = HEIGHT = 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'cyan', 'purple', 'brown', 'pink', 'violet', 'gray']

def get_no_of_racers():
  racers = 0
  while True:
    racers = input("Enter the no. of racers(2-10):")
    if racers.isdigit():
      racers = int(racers)
    else:
      print("Invalid input!..Enter a no.")
      continue
    if 2 <= racers <= 10:
      return racers
    else:
      print("Number not in range 2-10!")

def race(colors):
  turtles = create_turtles(colors)

  while True:
    for racer in turtles:
      distance = random.randrange(1, 20)
      racer.forward(distance)

      x, y = racer.pos()
      if y >= HEIGHT // 2 - 30:
        return colors[turtles.index(racer)]
  
def create_turtles(colors):
  turtles = []
  spacingx = WIDTH // (len(colors) + 1)
  for i, color in enumerate(colors):
    racer = turtle.Turtle()
    racer.color(color)
    racer.shape('turtle')
    racer.left(90)
    racer.penup()
    racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
    racer.pendown()
    turtles.append(racer)

  return turtles

def init_turtle():
  screen = turtle.Screen()
  screen.setup(WIDTH, HEIGHT)
  screen.title('Turtle Racing')


racers = get_no_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print("The winner is the turtle with color:", winner)
# Delay of 5 secs
time.sleep(5)