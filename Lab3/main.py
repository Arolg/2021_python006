import turtle
import math

turtle.shape('turtle')
L = 25
x = -100
y = 0


def print0():
    turtle.pendown()
    turtle.left(90)
    for i in range(2):
        turtle.forward(L * 2)
        turtle.left(90)
        turtle.forward(L)
        turtle.left(90)
    turtle.right(90)
    turtle.penup()


def print1():
    turtle.pendown()
    turtle.left(90)
    turtle.forward(L * 2)
    turtle.left(135)
    turtle.forward(L * math.sqrt(2))
    turtle.left(135)
    turtle.penup()


def print2():
    turtle.pendown()
    turtle.backward(L)
    turtle.left(45)
    turtle.forward(L * math.sqrt(2))
    turtle.left(45)
    turtle.forward(L)
    turtle.right(90)
    turtle.backward(L)
    turtle.penup()


def print3():
    turtle.backward(L)
    turtle.pendown()
    for i in range(2):
        turtle.left(45)
        turtle.forward(L * math.sqrt(2))
        turtle.right(45)
        turtle.backward(L)
    turtle.penup()


def print4():
    turtle.pendown()
    turtle.left(90)
    turtle.forward(L * 2)
    turtle.backward(L)
    turtle.left(90)
    turtle.forward(L)
    turtle.right(90)
    turtle.forward(L)
    turtle.right(90)
    turtle.penup()


def print5():
    turtle.backward(L)
    turtle.pendown()
    turtle.forward(L)
    turtle.left(90)
    turtle.forward(L)
    turtle.left(90)
    turtle.forward(L)
    turtle.right(90)
    turtle.forward(L)
    turtle.right(90)
    turtle.forward(L)
    turtle.penup()


def print6():
    turtle.pendown()
    for i in range(6):
        turtle.left(90)
        turtle.forward(L)
    turtle.right(135)
    turtle.forward(L * math.sqrt(2))
    turtle.right(45)
    turtle.penup()


def print7():
    turtle.backward(L)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(L)
    turtle.right(45)
    turtle.forward(L * math.sqrt(2))
    turtle.right(45)
    turtle.backward(L)
    turtle.penup()


def print8():
    turtle.pendown()
    for i in range(4):
        turtle.left(90)
        turtle.forward(L)
    turtle.left(90)
    turtle.forward(L)
    turtle.right(90)
    for i in range(4):
        turtle.left(90)
        turtle.forward(L)
    turtle.penup()


def print9():
    turtle.backward(L)
    turtle.left(90)
    turtle.forward(2 * L)
    turtle.left(90)
    print6()
    turtle.left(180)


def PrintIndex(a):
    if a == 0:
        print0()
    elif a == 1:
        print1()
    elif a == 2:
        print2()
    elif a == 3:
        print3()
    elif a == 4:
        print4()
    elif a == 5:
        print5()
    elif a == 6:
        print6()
    elif a == 7:
        print7()
    elif a == 8:
        print8()
    elif a == 9:
        print9()
    turtle.goto(x, y)
    turtle.goto(x + 27, y)


print("Введите число: ", end=' ')
a = int(input())
g = []
while a > 0:
    g.append(a % 10)
    a = a // 10

turtle.penup()
turtle.goto(x, y)

for i in range(len(g) - 1, -1, -1):
    print(g[i])
    PrintIndex(g[i])
    x = x + L * 1.2
input()
