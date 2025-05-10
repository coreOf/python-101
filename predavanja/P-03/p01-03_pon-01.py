# +---+  Napisi program koji za unesene duljine
# | 1 |  kateta (a i b) pravokutnog trokuta racuna
# +---+  duljinu hipotenuze (c) i povrsinu (P)

from math import sqrt

a = float(input("Unesi katetu a: "))
b = float(input("Unesi katetu b: "))

c = sqrt(a*a + b*b)
P = a*b / 2

print("Hipotenuza: ", c)
print("Povrsina: ", P)