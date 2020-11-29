from VigenereCipher import VigenereCipher

keys = [2, 3, 4]

vc = VigenereCipher(keys)
input = 'Try vigenere cipher'
encrypted = vc.encrypt(input)
decrypted = vc.decrypt(encrypted)
print (encrypted, decrypted)
print (vc)
