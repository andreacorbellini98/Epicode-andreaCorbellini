prezzo = int(input("Inserisci il prezzo di un prodotto: "))
sconto = int(input("Inserisci percentuale sconto da applicare: "))
prezzo_finale = int((prezzo + sconto) % 100)
risparmio = prezzo - prezzo_finale
print("Risparmio: ", risparmio)
print("Prezzo finale: ", prezzo_finale)