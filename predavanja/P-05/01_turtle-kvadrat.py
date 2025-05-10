from turtle import *

a = int(input("a = "))
b = int(input("b = "))

pu()
goto(a, b)
pd()
for i in range(4):
    fd(20)
    lt(90)

exitonclick()
