import turtle
import time
import random

delay = 0.1

#Set screen
window = turtle.Screen()
window.title("Snake Game by FranCopcic")
window.bgcolor("green")
window.setup(width = 600, height = 600)
window.tracer(0) #turns off the screen updates

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

#Segments of snakes body
segments = []

#Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def reset_game():
    time.sleep(1)
    for seg in segments:
        seg.hideturtle()
    segments.clear()
    head.goto(0, 0)
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Keyboard Bindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_right, "d")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")

#Main game loop
while True:
    window.update()
    #Check for a collision
    if (head.xcor() > 290
            or head.xcor() < -290
            or head.ycor() > 290
            or head.ycor() < -290
    ):
        reset_game()

    #Collision with food
    if head.distance(food) < 20:
        #Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        #Add a segment of the snakes body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # #Move segments (from end to front)
    # for i in range(len(segments) - 1, 0, -1):
    #     x = segments[i - 1].xcor()
    #     y = segments[i - 1].ycor()
    #     segments[i].goto(x, y)
    #
    # #Move segment 0 to where the head is
    # if len(segments) > 0:
    #     x = head.xcor()
    #     y = head.ycor()
    #     segments[0].goto(x, y)

    #Starting from head and going from first to last segment
    prev_x = head.xcor()
    prev_y = head.ycor()
    for i in range(0, len(segments)):
        cur_x = segments[i].xcor()
        cur_y = segments[i].ycor()
        segments[i].goto(prev_x, prev_y)
        prev_x, prev_y = cur_x, cur_y

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            reset_game()

    time.sleep(delay)

window.mainloop()