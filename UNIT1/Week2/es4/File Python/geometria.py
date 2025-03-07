def perimetro():
    print("Il seguente programma calcola il perimetro di una data figura geometrica")
    print("*** "
          "- Quadrato: >> 1"
          "- Rettangolo >> 2"
          "- Cerchio >> 3"
          "***")

    print("Inserisci la scelta: ")
    scelta = int(input(">>> "))
    if scelta == 1:
        print("Hai selezionato il perimetro del Quadrato")
        lato = float(input("Inserisci il valore del lato del quadrato "))
        print("Il perimetro del Quadrato, avente lato", lato, "è:", lato * 4)
    elif scelta == 2:
        print("Hai selezionato il perimetro del Rettangolo")
        base = float(input("Inserisci il valore della base: "))
        altezza = float(input("Inserisci il valore della altezza: "))
        print("Il perimetro del Rettangolo, avente base", base, "e altezza", altezza , "è", base * 2 + 2 * altezza)
    elif scelta == 3:
        print("Hai selezionato la circonferenza del Cerchio")
        r = float(input("Inserisci il valore del raggio: "))
        print("Il perimetro del Cerchio di raggio: ", r, "é: ", 2 * r * 3.14)
    else:
        print("Inserire una scelta valida")

perimetro()