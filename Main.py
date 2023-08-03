import socket

host = input('insira o IP que deseja: ')

def portScan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        return True
    except:
        return False

for port in range(1,65535):
    if portScan(port):
        print("Porta", port, "aberta")
    else:
        print("Porta", port, "fechada")
