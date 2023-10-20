import encryption_func as func
from math import pow

lettre = ord("B")
public, private = func.genKeys()
print(public, private)
encrypted = pow(lettre, public[0]) % public[1]
print(encrypted, chr(encrypted))
decrypted = pow(lettre, private[0]) % private[1]
print(decrypted, chr(decrypted))