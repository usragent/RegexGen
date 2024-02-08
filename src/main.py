import random
import re

class RegexGenerator:
    def __init__(self, data, customChars=None):
        self.data = data
        self.customChars = customChars if customChars else {}

    def appendChars(self, length=5):
        if isinstance(self.data, str):
            chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            prefix = ''.join(random.choice(chars) for _ in range(length))
            suffix = ''.join(random.choice(chars) for _ in range(length))
            return prefix + self.data + suffix
        elif isinstance(self.data, bytes):
            randomBytes = bytes(random.getrandbits(8) for _ in range(length))
            return randomBytes + self.data + randomBytes

    def test(self, regex, input=None):
        if input is None:
            testStr = self.appendChars()
        else:
            testStr = input

        print(f"[!] Using \033[93m> {testStr} <\033[0m for regex testing!")

        pattern = re.compile(regex, re.DOTALL)
        match = pattern.search(testStr)

        if match:
            return match.group()
        return ""

    def escapeSpecialChar(self, char):
        special = b".^$*+?()[]{}|\\" if isinstance(char, bytes) else ".^$*+?()[]{}|\\"
        return b"\\" + char if char in special else char

    def generate(self):
        pattern = b'' if isinstance(self.data, bytes) else ''
        dataLength = len(self.data)
        i = 0
        
        while i < dataLength:
            char = self.data[i:i+1] if isinstance(self.data, bytes) else self.data[i]
            if isinstance(self.data, str) and char.isalpha():
                start = i
                while i < dataLength and self.data[i].isalpha():
                    i += 1
                if i - start > 1:
                    pattern += '[a-zA-Z]{' + str(i - start) + '}'
                else:
                    pattern += '[a-zA-Z]'
            elif isinstance(self.data, str) and char.isdigit():
                start = i
                while i < dataLength and self.data[i].isdigit():
                    i += 1
                if i - start > 1:
                    pattern += r'\d{' + str(i - start) + '}'
                else:
                    pattern += r'\d'
            elif isinstance(self.data, str) and char.isspace():
                start = i
                while i < dataLength and self.data[i].isspace():
                    i += 1
                if i - start > 1:
                    pattern += r'\s{' + str(i - start) + '}'
                else:
                    pattern += r'\s'
            elif isinstance(self.data, bytes):
                count = 1
                while i + count < dataLength and self.data[i] == self.data[i + count]:
                    count += 1
                if count == 1:
                    pattern += b'\\x' + format(self.data[i], '02x').encode('utf-8')
                else:
                    pattern += b'\\x' + format(self.data[i], '02x').encode('utf-8') + b'{' + str(count).encode('utf-8') + b'}'
                i += count
            else:
                pattern += self.escapeSpecialChar(char)
                i += 1
        return pattern

"""
if __name__ == "__main__":
    print("-" * 50)

    
    # 📌 Test Case 1: BYTES

    dataBytes = b'\x00\x00\x00N\x00\t$\x93\x8d\x86S-|\xd94\xa2\x99@\x00\x00\x00'
    rgBytes = RegexGenerator(dataBytes)
    regexBytes = rgBytes.generate()
    print(f"\033[94m[*] Original bytes data ->\033[0m {dataBytes}")
    print(f"\033[94m[*] Generated Regex Pattern for text ->\033[0m \033[92m{regexBytes}\033[0m ")
    extractedTextBytes = rgBytes.test(regexBytes)
    print(f"\033[92m[*] Extracted Text for bytes ->\033[0m {extractedTextBytes}")
    print("-" * 50)


    # 📌 Test Case 2: TEXT

    dataText = "Hello123  World!"
    rgText = RegexGenerator(dataText)
    regexText = rgText.generate()
    print(f"\033[94m[*] Original text data ->\033[0m {dataText}")
    print(f"\033[94m[*] Generated Regex Pattern for text ->\033[0m \033[92m{regexText}\033[0m ")
    extractedTextText = rgText.test(regexText)
    print(f"\033[92m[*] Extracted Text for text ->\033[0m {extractedTextText}")
    print("-" * 50)



    # 📌 Test Case 3: CUSTOM

    customChars = {'H': '[Hh]', 'e': '[eE]', '!': '[!1]'}
    rgCustom = RegexGenerator(dataText, customChars)
    regexCustom = rgCustom.generate()
    print(f"\033[94m[*] Original text data with custom characters ->\033[0m {dataText}")
    print(f"\033[94m[*] Generated Regex Pattern for text ->\033[0m \033[92m{regexCustom}\033[0m ")
    extractedTextCustom = rgCustom.test(regexCustom)
    print(f"\033[92m[*] Extracted Text for text with custom characters ->\033[0m {extractedTextCustom}")
    print("-" * 50)
"""
