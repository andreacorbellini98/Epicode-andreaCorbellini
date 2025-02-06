def conta_parole(frase):
    frase = frase.lower().replace(',', '').replace('.', '')
    parole = frase.split()
    conteggio = {}

    for parola in parole:
        if parola in conteggio:
            conteggio[parola] += 1
        else:
            conteggio[parola] = 1

    return conteggio

frase = input("Inserisci una frase: ")
risultato = conta_parole(frase)
for parola, numero in risultato.items():
    print("Il numero di occorrenze di:", parola, "è: ", numero)