import turtle

turtle.shape('turtle')
n = int(input())


def stars(n):
    turtle.left(180 - 180 / n)
    turtle.forward(100)


x = 0
while x < n:
    stars(n)
    x += 1
