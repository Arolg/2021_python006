import turtle
import math

turtle.shape('turtle')
x = 0
while True:
    turtle.forward(x / 2 * math.pi)
    turtle.left(2 * math.pi)
    x += 0.01
