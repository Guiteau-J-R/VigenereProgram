from CaesarCipher import CaesarCipher

class CaesarCracker:
    def __init__(self, char):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.mostCommonIdx = alphabet.find(char)	#The most common character in a given language

    def countLetters(self, message):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        counts = [0 for x in range(26)]
        for char in message:
            idx = alphabet.find(char.lower())
            if idx != -1:
                counts[idx] += 1
        return counts

    def getKey(self, encrypted):
        freqs = self.countLetters(encrypted)
        maxIdx = freqs.index(max(freqs))
        key = maxIdx - self.mostCommonIdx
        if maxIdx < self.mostCommonIdx:
            key = 26 - (self.mostCommonIdx - maxIdx)
        return key

    def decrypt(self, encrypted):
        key = self.getKey(encrypted)
        cc = CaesarCipher(key)
        return cc.decrypt(encrypted)
