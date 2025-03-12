import threading
import socket

def handle_connection(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f'Received: {data.decode()}')
    conn.close()

def receive(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", port))
    s.listen(1)
    print(f'Listening on port {port}')

    while True:
        conn, addr = s.accept()
        print(f'Connected by {addr}')
        threading.Thread(target=handle_connection, args=(conn,)).start()

def send(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    while True:
        message = input("> ")
        s.sendall(message.encode())

    s.close()

# Configuration
local_port = 62641
remote_ip = '192.168.1.36'  # Adresse IP du pair
remote_port = 62641  # Même port pour envoyer et recevoir

# Démarrer les threads
receiver_thread = threading.Thread(target=receive, args=(local_port,))
sender_thread = threading.Thread(target=send, args=(remote_ip, remote_port))

receiver_thread.start()
sender_thread.start()
