import string
def encrypt_neat(plaintext):
    plaintext = plaintext.split(' ')
    total = []
    for word in plaintext:
        ciphertext = ""
        for character in word:
            if character in set(string.ascii_lowercase):
                ciphertext += chr((25-(ord(character)-97))%26 + 97)
            else:
                ciphertext += character
        total.append(ciphertext)
    return total

plaintext = input("What would you like to 'encrypt'?\n")
ciphertext = encrypt_neat(plaintext)
print(' '.join(ciphertext))
