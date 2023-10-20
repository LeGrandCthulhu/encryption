from random import randint, choice
from math import gcd
from sympy import prime

def primeGen() -> tuple[int]:
    p = prime(randint(1000, 1500))
    q = prime(randint(1000, 1500))
    return p, q

def phi(p: int, q: int) -> int:
    return (p-1)*(q-1)

def phi2(n: int) -> int:
    result = n
    p = 2

    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n = int(n / p)
            result -= int(result / p)
        
        p += 1
    
    if n > 1:
        result -= int(result / n)
    
    return result

def genE(phiN: int) -> int: # on met phi(N) en paramètre pour éviter de recalculer à chaque fois
    L = []
    for i in range(3, phiN):
        if gcd(i, phiN) == 1:
            L.append(i)
    return choice(L[len(L)//2:])

def genD(e: int, phiN: int) -> int:
    for d in range(3, phiN):
        if (d * e) % phiN == 1:
            return d
    raise ValueError("d n'existe pas")

def genKeys() -> tuple[tuple[int]]:
    p, q = primeGen()
    N = p * q
    phiN = phi(p, q)
    e = genE(phiN)
    d = genD(e, phiN)

    return ((e, N), (d, N))

