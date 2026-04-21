import socket
import sys
import random

def server():
    # Taking in terminal argument for port
    port = int(sys.argv[1])
    # Creating UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', port))
    # confirming server up
    print(f"[server] : ready to accept data...")
    # loop for socket to listen continuosly and respond at the ip and port
    count = 0
    while count < 10:
        data, client_address = server_socket.recvfrom(1024)
        if data == b'PING':
            count += 1
            # Introduces the random packet drop
            if random.random() < 0.70:
                print(f"[client] : {data.decode()}")
                server_socket.sendto(b'PONG', client_address)
            else:
                print(f"[server] : packet dropped")


if __name__ == "__main__":
    server()
