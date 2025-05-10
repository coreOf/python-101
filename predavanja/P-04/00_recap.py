# 3
# 5
# neparan
# 7
# neparan
# 10
# paran

n = int(input())
for i in range(n):
    x = int(input())
    if x % 2 == 1:
        print("neparan")
    else:
        print("paran")
        continue
    print("Korak petlje:", i)

print("Kraj")