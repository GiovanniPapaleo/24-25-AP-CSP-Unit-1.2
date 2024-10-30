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
font_setup = ("Arial", 20, "bold")

#-----game functions--------
def change_position():
    new_xpos = rand.randint(-400,400)
    new_ypos = rand.randint(-300,300)
    spot.goto(new_xpos,new_ypos)

def update_score():
    global score
    score += 88
    score_writer.write(score, font=font_setup)

def spot_clicked (x,y):
    change_position()
    update_score()

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()