import ipaddress
import socket
import subprocess
import platform

def scan_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def ip_reachable(ip):
    param="-n" if platform.system().lower()== "windows" else "-c"
    command= ["ping", param, "1", ip]

    try:
        result=subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.returncode==0
    except Exception:
        return False
    
def scan_ports(ip,start_port=0, end_port=65535):
    open_ports=[]
    for port in range(start_port, end_port+1):
        print(f"Sto scansionando la porta {port}",end="\r")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((ip,port))==0:
                open_ports.append(port)
    return open_ports

ip=input("Inserisci un indirizzo IP: ")

if not scan_ip(ip):
    print("Codice IP non valido.")
elif not ip_reachable(ip):
    print(f"L'IP {ip} non e' raggiungibile.")
else:
    porte_aperte=scan_ports(ip)
    if porte_aperte:
        print(f"Porte aperte su {ip}: {porte_aperte}")
    else:
        print(f"Nessuna porta aperta trovata su: {ip}.")
        