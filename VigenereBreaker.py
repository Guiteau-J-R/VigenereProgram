from CaesarCracker import CaesarCracker
from VigenereCipher import VigenereCipher
import string

class VigenereBreaker:
    languages = ['Danish', 'Dutch', 'English', 'French', 'German', 'Italian', 'Portuguese', 'Spanish']
    def __init__(self):
        self.dictionaries = {}
        for language in self.languages:
            self.dictionaries[language] = self.readDictionary(language)

    def sliceString(self, message, whichSlice, totalSlices):
        output = ''
        i = whichSlice
        while i < len(message):
            output += message[i]
            i += totalSlices
        return output

    def tryKeyLength(self, encrypted, keyLength, mostCommon):
        keys = [0] * keyLength
        cc = CaesarCracker(mostCommon)
        for i in range(0, keyLength):
            sliced = self.sliceString(encrypted, i, keyLength)
            keys[i] = cc.getKey(sliced)
        return keys

    def readDictionary(self, language):
        words = []
        with open("dictionaries/" + language, encoding = 'ISO-8859-1') as fp:
            lines = fp.readlines()
            for word in lines:
                words.append(word.lower().strip())
        return words

    def countWords(self, message, dictionary):
        count = 0
        for w in message.split():
            word = w.lower()
            if word in dictionary:
                count += 1
        return count

    def mostCommonCharIn(self, dictionary):
        max = 0
        counts = {}
        for word in dictionary:
            for char in word:
                if char in counts:
                    counts[char] += 1
                else:
                    counts[char] = 1

        char = ''
        for count in counts:
            if counts[count] > max:
                max = counts[count]
                char = count
        return char

    def breakForAllLangs (self, encrypted):
        max = 0
        keyLength = 0
        language = ''
        ch = ''
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for key in self.dictionaries:
            char = self.mostCommonCharIn(self.dictionaries[key])
            for klength in range(1, 100):
                keys = self.tryKeyLength(encrypted, klength, char)
                vc = VigenereCipher(keys)
                message = vc.decrypt(encrypted)
                for c in message:
                    if c in punc:
                        message = message.replace(c, '')
                count = self.countWords(message, self.dictionaries[key]);
                if count > max:
                    max = count
                    keyLength = klength
                    if language != key:
                        language = key
                        ch = char

        print("language: {}, valid word: {}, key length: {}".format(language, max, keyLength))
        keys = self.tryKeyLength(encrypted, keyLength, ch)

        vc = VigenereCipher(keys)
        return vc.decrypt(encrypted)
