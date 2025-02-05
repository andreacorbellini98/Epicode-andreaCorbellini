s = input("Inserisci una stringa: ")
vocali = ["a","e","i","o","u"]
contatore = 0

for carattere in s.lower():
    if carattere in vocali:
        contatore +=1

print("Il numero di vocali è: ", contatore)