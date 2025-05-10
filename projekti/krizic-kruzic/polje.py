from turtle import *

P = [0, 2, 0, 1, 0, 0, 0, 0 , 0]

print("X", "O")

print("   | O | O ")
print("---+---+---")
print(" X | X | X ")
print("---+---+---")
print("   |   | O ")


# lijeva vertikalna crta
pu()
goto(-50, 150)
pd()
goto(-50, -150)
pu()

# desna vertikalna crta
goto(50, 150)
pd()
goto(50, -150)
pu()

# gornja horizontalna crta
goto(-150, 50)
pd()
goto(150, 50)
pu()

# donja horizontalna crta
goto(-150, -50)
pd()
goto(150, -50)
pu()

# krizic u srednjem polju (5)
# goto(-40, -40)
# pd()
# goto(40, 40)
# pu()
# goto(40, -40)
# pd()
# goto(-40, 40)
# pu()

# kruzic u srednjem polju (5) koristeci GOTO
# goto(0, -40)
# pd()
# circle(40)
# pu()

goto(0,-100) # pomak na centar zeljenog polja
# kruzic koristeci FD
rt(90)
fd(40)
lt(90)
pd()
circle(40)
pu()

goto(100,100) # pomak na centar zeljenog polja
# krizic koristeci FD
lt(45)
pd()
for i in range(4):
    fd(50) # ne 40 jer je u koso
    bk(50)
    rt(90)
rt(45)
pu()

exitonclick()