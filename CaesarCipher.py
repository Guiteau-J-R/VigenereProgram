class CaesarCipher:
    def __init__(self, key):
        self.key = key
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.shiftedAlphabet = self.alphabet[key:] + self.alphabet[:key]
        self.alphabet = self.alphabet + self.alphabet.lower()
        self.shiftedAlphabet = self.shiftedAlphabet + self.shiftedAlphabet.lower()

    def transformLetter(self, char, fromStr, toStr):
        idx = fromStr.find(char)
        if idx != -1:
            return toStr[idx]
        return char

    def encryptLetter(self, char):
        return self.transformLetter(char, self.alphabet, self.shiftedAlphabet)

    def decryptLetter(self, char):
        return self.transformLetter(char, self.shiftedAlphabet, self.alphabet)

    def transform(self, input, fromStr, toStr):
        output = ''
        for char in input:
            output = output + self.transformLetter(char, fromStr, toStr)
        return output

    def encrypt(self, input):
        return self.transform(input, self.alphabet, self.shiftedAlphabet)

    def decrypt(self, input):
        return self.transform(input, self.shiftedAlphabet, self.alphabet)

    def __str__(self):
        return 'CaesarCipher, key: ' + str(self.key)
