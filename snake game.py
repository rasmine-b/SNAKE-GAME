import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0


#Set up the screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("pink")
window.setup(width=600, height=600)
window.tracer(0) 

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake Apple
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score:  0   High Score:  0", align="center", font=("Courier", 24, "normal"))

# Functions
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
     



def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

# Main game loop
while True:
    window.update()

    # Collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        # Clear the segments list
        segments = []

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        # Update the score
        pen.clear()
        pen.write("Score:  {}   High Score:  {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Collision with the food
    if head.distance(food) < 20:
        # Move the food
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase score
        score += 1

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score:  {}   High Score:  {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    
    # Move the end segments in reverse
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)





    move()

    # Head collisions with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments = []

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score
            pen.clear()
            pen.write("Score:  {}   High Score:  {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

     

window.mainloop()