#Caesar Cipher 8/1/23
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890!@#$%^&*()'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Do you wish to encrypt, decrypt or brute-force a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd', 'brute', 'b']:
            return mode
        else:
            print('Enter ether "encrypt", "decrypt" or "brute"')


def getMessage():
    print("Enter your message")
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key number 1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if(key>= 1 and key<= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
        
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: #symbol not found in SYMBOLS
            translated += symbol
        else:
            #Encrypt or decrypt
            symbolIndex += key
            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode()
message = getMessage()
if mode[0] != 'b':
    key = getKey()
print('Your translated text is:')
if mode[0] != 'b':
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE):
        print(key, getTranslatedMessage('decrypt', message, key))
            
