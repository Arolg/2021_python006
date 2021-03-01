import turtle
import random as r


turtle.shape('turtle')
for i in range(100):
    s = r.random()*90
    turtle.left(s)
    d = r.random()*100
    turtle.forward(d)
