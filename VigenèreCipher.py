def generateKey(string, key):
    key = list(key)
    if len(key) == len(string):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord("A")
        cipher_text.append(chr(x))
    return "".join(cipher_text)


def decryptText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord("A")
        orig_text.append(chr(x))
    return "".join(orig_text)


if __name__ == "__main__":
    string = "Nothing".upper()
    keyword = """ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAklOUpkRQrfHY17SbrmTIpNLTGK9Tjom/BWDSUGPl+nafzlHDTYW7hdI4yZ5ew18JH4JW9jbhUFrviQzM7xlELEVf4h9lFX5QVkbPppSwg0cda3Pbv7kOdJ/MTyBlWXFCR+HAo3FXRitBqxiX1nKhXpHAZsMciLq8V6RjsNAQwdsdMFvSlVK/7XAt3FaoJoAsncM1Q9x5+3V0Ww68/eIFmb1zuUFljQJKprrX88XypNDvjYNby6vw/Pb0rwert/EnmZ+AW4OZPnTPI89ZPmVMLuayrD2cE86Z/il8b+gw3r3+1nKatmIkjn2so1d01QraTlMqVSsbxNrRFi9wrf+M7Q== schacon@mylaptop.local"""
    # keyword = "great"
    key = generateKey(string, keyword)
    cipher_text = cipherText(string, key)
    print("Encrypted Text : ", cipher_text)
    print("Decrypted Text : ", decryptText(cipher_text, key))
