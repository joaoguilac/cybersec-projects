import argparse
import socket

# Menu da ferramenta com os argumentos, como se fosse o manual
parser = argparse.ArgumentParser(description="Port scanner tcp")
parser.add_argument("-i", "--ip", help="Alvo IPv4", required=True)
parser.add_argument("-s", "--start", help="Starting port", type=int, required=True)
parser.add_argument("-e", "--end", help="Ending port", type=int, required=True)
args = parser.parse_args()

# Variáveis que receberão a entrada
target = args.ip
start_port = args.start
end_port = args.end

# Iterar por cada porta no intervalo fornecido
for port in range(start_port, end_port+1):
    # Criar um socket com protocolo IPV4 e TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((target, port))
        print(f"Port {port} is open")
        banner = s.recv(1024)
        print("Entrou")
        if banner:
            print(f"Serviço {banner.decode().strip()}")
            s.close()
    except:
        pass