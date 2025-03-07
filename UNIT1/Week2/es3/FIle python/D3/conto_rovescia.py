import time
n = int(input("Inserisci un numero da cui iniziare il conto alla rovescia: "))
secondi = int(input("Inserisci il numero di secondi che deve passare tra un numero e il successivo: "))
for i in range(n, -1, -1):
    print(i)
    time.sleep(secondi)
print("Conto alla rovescia completato!")