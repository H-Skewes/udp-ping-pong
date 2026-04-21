import socket
import sys


def client():
    # takes in ip and port
    IP = sys.argv[1]
    port = int(sys.argv[2])

    # makes udp socket and defining server address
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1.0)
    address = (IP, port)
    # loop to ping server 10 times
    for i in range(1, 11):
        print(f"{i:<2} : sent PING...", end=" ", flush=True)
        client_socket.sendto(b'PING', address)

        try:
            data, _ = client_socket.recvfrom(1024)
            print(f"received  {data}")
        except socket.timeout:
            print("Timed Out")

    client_socket.close()


if __name__ == "__main__":
    client()
