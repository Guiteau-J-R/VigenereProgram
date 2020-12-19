from VigenereCipher import VigenereCipher
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 6332        # Port to listen on (non-privileged ports are > 1023). port should be an integer from 1-65535 (0 is reserved)
keys = [2, 3, 4, 5]
vc = VigenereCipher(keys)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    encrypted = ''
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            encrypted += str (data, 'utf-8')
            if not data:
                print(vc.decrypt(encrypted))
                break
            conn.sendall(data)
