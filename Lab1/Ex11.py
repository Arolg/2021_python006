import turtle

turtle.shape('turtle')
turtle.left(90)
n = 50


def circle(n):
    turtle.circle(n)
    turtle.circle(-n)


while True:
    circle(n)
    n += 5
