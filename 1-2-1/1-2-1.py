# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "yellow"
spot_size = 2
spot_shape = "circle"
score = 0


#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
spot.pencolor("orange")
spot.penup()

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.speed(0)
score_writer.penup()
score_writer.goto(-350, 350)
score_writer.pendown()

counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(300,350)
font_setup = ("Arial", 20, "bold")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----game functions--------
def change_position():
    new_xpos = rand.randint(-400,400)
    new_ypos = rand.randint(-300,300)
    spot.goto(new_xpos,new_ypos)

def update_score():
    global score
    score += 100
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def spot_clicked (x,y):
    global timer_up
    if timer_up == False:
        update_score()
        change_position()
    else:
        spot.hideturtle()

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()