# U novcaniku imamo N kovanica
# Svaka od kovanica moze biti jedan
# od sljedecih iznosa:
#  - 10 c
#  - 20 c
#  - 50 c
#  - 1 €
#  - 2 €

# Za zadani unos kovanica izracunaj
# ukupan iznos u eurima.

n = int(input("Broj kovanica: "))
z = 0
for i in range(n):
    k = int(input("Iznos kovanice: "))
    if k > 2:
        k /= 100
    z += k
print(z)
