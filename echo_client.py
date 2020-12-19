from VigenereCipher import VigenereCipher
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 6332        # The port used by the server
keys = [2, 3, 4, 5]


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    input = """Message crypted with Vigenere Cipher"""

    vc = VigenereCipher(keys)
    encrypted = vc.encrypt(input)
    print ("Message: {}\n Encrypted: {}".format(input, encrypted))
    message = bytes (encrypted, 'utf-8')

    s.sendall(message)
    data = s.recv(1024)

print('Received', repr(data))
