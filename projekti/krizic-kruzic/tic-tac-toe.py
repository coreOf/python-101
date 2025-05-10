# Za kasnije:
#  1. provjeriti je li polje vec zauzeto cak i nakon pogresnog unosa
#  2. omoguciti izbor igra li prvo krizic ili kruzic

# 0 -> prazno polje, 1 -> krizic (x), 2 -> kruzic (o) 

from turtle import *

# indeksi       0  1  2  3  4  5  6  7  8
# broj polja    1  2  3  4  5  6  7  8  9
stanje_polja = [0, 0, 0, 0, 0, 0, 0, 0, 0]

na_potezu = 1  # krizic je prvi na potezu

# nacrtaj polje za igru
pu(); goto(-50, 150)
pd(); goto(-50, -150)
pu(); goto(50, 150)
pd(); goto(50, -150)
pu(); goto(-150, 50)
pd(); goto(150, 50)
pu(); goto(-150, -50)
pd(); goto(150, -50)
pu()

for i in range(9):
    # tko je trenutno na potezu
    if na_potezu == 1:
        print("Trenutno igra križić.")
    elif na_potezu == 2:
        print("Trenutno igra kružić.")

    x = int(input("Unesi broj polja: "))

    # provjeri je li potez dopusten
    if stanje_polja[x-1] == 0:
        # zabiljezi potez u stanje_polja
        stanje_polja[x-1] = na_potezu
    else:
        print("Odabrano polje je zauzeto!")
        x = int(input("Ponovno unesi broj polja: "))
        # zabiljezi potez u stanje_polja
        stanje_polja[x-1] = na_potezu

    if x == 1:
        goto(-100, 100)
    elif x == 2:
        goto(0, 100)
    elif x == 3:
        goto(100, 100)
    elif x == 4:
        goto(-100, 0)
    elif x == 5:
        goto(0, 0)
    elif x == 6:
        goto(100, 0)
    elif x == 7:
        goto(-100, -100)
    elif x == 8:
        goto(0, -100)
    elif x == 9:
        goto(100, -100)
    
    if na_potezu == 1:
        # nacrtaj krizic
        lt(45); pd()
        for i in range(4):
            fd(50)
            bk(50)
            rt(90)
        rt(45); pu()
        # promijeni tko je na potezu
        na_potezu = 2
    elif na_potezu == 2:
        #nacrtaj kruzic
        rt(90); fd(40); lt(90)
        pd(); circle(40); pu()
        # promijeni tko je na potezu
        na_potezu = 1
    
    print(stanje_polja)
    # exitonclick()

    
exitonclick()
