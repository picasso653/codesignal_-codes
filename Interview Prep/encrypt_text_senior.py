# The function should take two parameters: the text to encrypt and the shift amount
def encrypt_text(text, shift):
    encrypted = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted += char
    return encrypted


print(encrypt_text("Pablo is a god!", 2))

