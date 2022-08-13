from fnmatch import translate
import pyperclip

#This is string is to be encrypted/decrypted
message = "This is my secret message"

#Encryption key
key = 13

#Whether the program encrypts or decrypts
mode = 'encrypt'

# Every possible symbols
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Store te encrypted/decrypted form of the message
translated = ''

for symbol in message:
    # Note : Only symbols in the SYMBOLS string can be encypted/decrypted
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        #Perform encryption/decryption
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # Handle wraparound, if needed
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex <= 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
        
        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypt/decrypt
        translated = translated + symbol

print(translated)
pyperclip.copy(translated)
