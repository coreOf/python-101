n = int(input("Broj ocjena: ")) # koliko ima ocjena
z = 0
for i in range(n):
    o = int(input("Ocjena: " ))
    z += o # z = z + o
print(z/n)
