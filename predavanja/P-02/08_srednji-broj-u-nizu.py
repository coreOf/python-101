n = int(input())
if n % 2 == 0:
    print("Program ne radi sa parnim brojem brojeva.")
else:
    srednji = 0
    for i in range(n):
        b = int(input())
        if i == n // 2:
            srednji = b
    print("Srednji broj je", srednji)
