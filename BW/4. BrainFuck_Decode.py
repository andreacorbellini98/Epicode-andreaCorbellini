def brainfuck_interpreter(code):
    tape = [0] * 30000  # Inizializziamo un nastro con 30.000 celle
    pointer = 0         # Puntatore inizializzato alla prima cella
    output = []         # Lista per raccogliere l'output
    stack = []          # Stack per i loop
    i = 0               # Indice dell'istruzione corrente
    
    while i < len(code):
        command = code[i]
        
        if command == '>':
            pointer += 1
        elif command == '<':
            pointer -= 1
        elif command == '+':
            tape[pointer] += 1
        elif command == '-':
            tape[pointer] -= 1
        elif command == '.':
            output.append(chr(tape[pointer]))  # Aggiunge il carattere ASCII all'output
        elif command == ',':
            # Non gestiamo l'input in questo caso
            pass
        elif command == '[':
            if tape[pointer] == 0:
                # Salta alla fine del loop
                loop = 1
                while loop > 0:
                    i += 1
                    if code[i] == '[':
                        loop += 1
                    elif code[i] == ']':
                        loop -= 1
            else:
                stack.append(i)  # Salva l'indice corrente nello stack
        elif command == ']':
            if tape[pointer] != 0:
                i = stack[-1]  # Torna all'inizio del loop
            else:
                stack.pop()  # Rimuove l'indice del loop
            
        i += 1
    
    return ''.join(output)

# Codice Brainfuck da decifrare
brainfuck_code = input("Inserisci il codice che vuoi decriptare:\n")


# Esegui l'interprete
result = brainfuck_interpreter(brainfuck_code)
print("Output decifrato:", result)