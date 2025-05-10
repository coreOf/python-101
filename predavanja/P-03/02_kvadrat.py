# Napisi program koji za ucitanu povrsinu kvadrata ispisuje duljinu stranice tog kvadrata P=a*a

# Ulaz: 144
# Izlaz: 12 (jer je 12*12 = 144)

from math import sqrt

p = int(input())
a = sqrt(p)
print(int(a))
