import encryption_func as func

lettre = ord("B")
public, private = func.genKeys()
encrypted = (lettre**public[0]) % public[1]
print(encrypted, chr(encrypted))
decrypted = (encrypted**private[0]) % private[1]
print(decrypted, chr(decrypted))