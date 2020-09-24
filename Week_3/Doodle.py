import turtle

notebook = turtle.Screen()

Minnie = turtle.Turtle() #Capital is important as distinguishment --> is a class

Minnie.forward(50)
Minnie.stamp()
Minnie.penup()
Minnie.forward(30)
Minnie.pendown()
Minnie.stamp()
Minnie.forward(40)


Minnie.left(35)
Minnie.forward(70)
Minnie.backward(20)

notebook.exitonclick() #drawing sticks around until we click on it