def media_mobile(lista , n):
    risultato = []
    for i in range(len(lista)):
        if i < n - 1:
            media = sum(lista[:i + 1]) / (i + 1)
        else:
            media = sum(lista[i - n + 1:i + 1]) / n
        risultato.append(media)
    return risultato

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
print(media_mobile(numeri, n))