anno = int(input("Inserisci un anno per verificare se è bisestile: "))
if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
    print(anno, "è un anno bisestile")
else:
    print(anno, "non è un anno bisestile")