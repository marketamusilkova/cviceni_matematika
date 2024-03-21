# Pokud máš ráda matematiku a nebojíš se výzvy, načti od uživatele číslo n a:

# Vypočti faktoriál n! (součin všech celých čísel od 1 do n).
# Zjisti, jestli je n prvočíslo.
# Vypiš prvních n členů Fibonacciho posloupnosti (1, 1, 2, 3, 5, 8, 13, 21, …).

import math
n = int(input("Napiš číslo:"))


faktorial = math.factorial(n)
print("Faktoriál čísla", n, "je", faktorial)


def je_prvocislo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if je_prvocislo(n):
    print(f"{n} je prvočíslo.")
else:
    print(f"{n} není prvočíslo.")


def Fibonacciho_posloupnost(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacciho_posloupnost(n - 1) + Fibonacciho_posloupnost(n - 2)

for i in range(n):
    print(Fibonacciho_posloupnost(i), end=" ")
