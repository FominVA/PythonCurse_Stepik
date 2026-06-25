class CaesarCipher:


    def __init__(self, shift):
        self.shift = shift
        self.chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    def encode(self, word):
        new_word = ''
        for letter in word:
            if letter == letter.upper() and letter.isdigit() != True and letter in self.chars:
                new_word += chr((ord(letter) - 65 + self.shift) % 26 + 65)
            elif letter == letter.lower() and letter.isdigit() != True and letter in self.chars:
                new_word += chr((ord(letter) - 97 + self.shift) % 26 + 97)
            else:
                new_word += str(letter)
        return new_word

    def decode(self, word):
        new_word = ''
        for letter in word:
            if letter == letter.upper() and letter.isdigit() != True and letter in self.chars:
                new_word += chr((ord(letter) - 65 - self.shift) % 26 + 65)
            elif letter == letter.lower() and letter.isdigit() != True and letter in self.chars:
                new_word += chr((ord(letter) - 97 - self.shift) % 26 + 97)
            else:
                new_word += letter
        return new_word

cipher = CaesarCipher(5)

print(cipher.encode('Биgeek123'))
print(cipher.decode('Биljjp123'))

#Для encode заглавные (ord(c) - 65 + self.shift) % 26 + 65, для строчных (ord(c) - 97 + self.shift) % 26 + 97
#Для decode заглавные (ord(c) - 65 - self.shift) % 26 + 65, строчных (ord(c) - 97 - self.shift) % 26 + 97