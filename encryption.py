import encryption_func as func

#lettre = ord("B")
public, private = func.genKeys()
print(public, private)
for lettre in range(private[1] + 20): 
    encrypted = (lettre**public[0]) % public[1]
#print(encrypted, chr(encrypted))
    decrypted = (encrypted**private[0]) % private[1]
    print(lettre == decrypted)
#print(decrypted, chr(decrypted))