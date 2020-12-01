from VigenereBreaker import VigenereBreaker
from VigenereCipher import VigenereCipher

keys = [2, 3, 4]
vb = VigenereBreaker()
vc = VigenereCipher(keys)

input = 'using Vigenere breaker, we will decrypt the message successfully eeeeeeeeeeeeeeeeeee'

encrypted = vc.encrypt(input)

print (encrypted, vb.breakForAllLangs(encrypted))
