class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        res = ''
        i = 0
        for c in text:
            if c in self.alphabet:
                res += chr(ord(self.key[i]) + ord(c) - 2 * ord(self.alphabet[0]))
                i = (i + 1) % len(self.key)
            else:
                res += c
        return res

    def decode(self, text):
        pass
# TODO
