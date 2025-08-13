import turtle
nbrsides = 5
turtle.speed(0)
turtle.bgcolor("black")  # background colour
turtle.color("cyan", "yellow")  # pen colour, fill colour


for steps in range(nbrsides):
    turtle.forward(100)
    turtle.right(360/5)
    
    
    for moresteps in range (nbrsides):
        turtle.forward(50)
        turtle.right(360/nbrsides)
        
turtle.done()                