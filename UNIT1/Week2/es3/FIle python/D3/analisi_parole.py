import re

def analizza_parole(testo):
    testo = re.sub(r'[^ \w\s]','',testo.lower())
    parole = testo.split()
    conteggio =  {}
    for parola in parole:
        if parola in conteggio:
           conteggio[parola] += 1
        else:
           conteggio[parola] = 1
    return conteggio

testo = "Ciao, ciao! Come stai? Stai bene?"
print(analizza_parole(testo))