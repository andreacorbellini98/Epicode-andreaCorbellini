s = input("Inserisci una stringa: ")
contatore = 0

for carattere in s.lower():
    if carattere in s:
        contatore += 1

print("Il numero di caratteri è: ", contatore)