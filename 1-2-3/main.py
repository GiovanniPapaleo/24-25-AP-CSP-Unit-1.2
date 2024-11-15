#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"
ground_height = -200
apple_letter_x_offset = -10
apple_letter_y_offset = -30

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

drawer = trtl.Turtle()

wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
wn.addshape(pear_image)

apple = trtl.Turtle()
pear = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  draw_an_a()
  wn.update()


def drop_apple():
  apple.penup()
  apple.goto(apple.xcor(), ground_height)
  apple.pendown()


def draw_an_a():
  drawer.color("blue")
  drawer.penup()
  drawer.goto(apple_letter_x_offset, apple_letter_y_offset)
  drawer.pendown()
  drawer.write("A", font=("Arial", 33, "bold"))


#-----function calls-----
wn.onkeypress(drop_apple, "a")

wn.listen()

draw_apple(apple)



wn.mainloop()
