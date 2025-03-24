x = int(input())
br = 0
while x > 0:
    print(x % 10)
    x = x // 10
    br = br + 1 # br += 1
print("Uneseni broj ima", br, "znamenki")