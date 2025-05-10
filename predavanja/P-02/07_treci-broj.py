# Unosimo N brojeva
# Zelimo ispisati treci uneseni brjoj

n = int(input())
treci = 0
for i in range(n):
    b = int(input())
    if i == 2:
        treci = b
print("Treci uneseni broje je", treci)
