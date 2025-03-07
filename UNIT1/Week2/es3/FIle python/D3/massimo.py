numeri = input("Inserisci una lista di numeri separati da spazi: ")
lista_numeri = [int(n) for n in numeri.split()]
massimo = max(lista_numeri)
print("Il numero più grande è:", massimo)