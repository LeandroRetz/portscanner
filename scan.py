import socket

host = '162.241.49.132'
timeout = 1 

def portScan(porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((host, porta))
    s.close()
    if result == 0:
        print(f"Porta {porta} aberta")
    else:
        print(f"Porta {porta} fechada")

def portScanall():
    for i in range(1, 65000):
        print(f'Escaneando porta {i}:')
        portScan(i)

portScanall()