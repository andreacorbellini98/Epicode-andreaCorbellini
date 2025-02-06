def media(numeri):
    return sum(numeri) / len(numeri)

def mediana(numeri):
    numeri.sort()
    n = len(numeri)
    if n % 2 == 1:
        return numeri[n // 2]
    else:
        return (numeri[n // 2 - 1] + numeri[n // 2]) / 2

def moda(numeri):
    freq = {}
    for num in numeri:
        freq[num] = freq.get(num, 0) + 1
    max_freq = max(freq.values())
    mode = [num for num, count in freq.items() if count == max_freq]
    return mode[0] if len(mode) == 1 else mode

def main():
    numeri = list(map(float, input("Inserisci una lista di numeri separati da spazi: ").split()))
    print(f"Media: {media(numeri)}")
    print(f"Mediana: {mediana(numeri)}")
    print(f"Moda: {moda(numeri)}")

if __name__ == "__main__":
    main()
