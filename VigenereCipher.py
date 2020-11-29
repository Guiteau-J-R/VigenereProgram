from CaesarCipher import CaesarCipher

class VigenereCipher:
    def __init__(self, keys):
        self.ciphers = []
        for key in keys:
            self.ciphers.append(CaesarCipher(key))

    def encrypt(self, input):
        output = ''
        for i in range(len (input)):
            idx = i % len (self.ciphers)
            output += self.ciphers[idx].encryptLetter(input[i])
        return output

    def decrypt(self, input):
        output = ''
        for i in range(len (input)):
            idx = i % len (self.ciphers)
            output += self.ciphers[idx].decryptLetter(input[i])
        return output

    def __str__(self):
        return "\n". join(map (str, self.ciphers))
