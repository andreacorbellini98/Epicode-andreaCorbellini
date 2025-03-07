n = int(input("Inserisci un numero: "))

def Fibonacci(n):
    if n < 0:
        print("Input non valido")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

for numeri in range(n):
    print(Fibonacci(n))
