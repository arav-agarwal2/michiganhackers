def encrypt_neat(plaintext):
    ciphertext = ""
    for character in plaintext.lower():
        ciphertext += chr((25-(ord(character)-97))%26 + 97)
    print(ciphertext)
    return ciphertext

plaintext = input("What would you like to 'encrypt'?\n")
ciphertext = encrypt_neat(plaintext)
