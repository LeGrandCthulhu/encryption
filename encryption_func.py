from random import randint
from math import gcd
from sympy import prime

def primeGen() -> tuple[int]:
    p = prime(randint(3, 10))
    q = prime(randint(3, 10))
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

def genE(N: int, phiN: int) -> int: # on met phi(N) en paramètre pour éviter de recalculer à chaque fois
    for i in range(2, phiN + 1):
        if gcd(i, N) == gcd(i, phiN) == 1:
            return i

def genD(e: int, phiN: int, N: int) -> int:
    return (randint(2, (N-e)//phiN)*phiN) + e

def genKeys() -> tuple[tuple[int]]:
    p, q = primeGen()
    N = p * q
    phiN = phi(p, q)
    e = genE(N, phiN)
    d = genD(e, phiN, N)

    return ((e, N), (d, N))

