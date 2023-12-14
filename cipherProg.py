alphabet = [chr(i) for i in range(97, 123)]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    cipherText = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            newPosition = (position + shift) % 26
            newLetter = alphabet[newPosition]
            cipherText += newLetter
        else:
            cipherText += letter
    return cipherText

def decrypt(text, shift):
    plainText = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            newPosition = (position - shift) % 26
            newLetter = alphabet[newPosition]
            plainText += newLetter
        else:
            plainText += letter
    return plainText

if direction == "encode":
    encrypted_text = encrypt(text, shift)
    print("Encrypted message:" + encrypted_text)
elif direction == "decode":
    decrypted_text = decrypt(text, shift)
    print("Decrypted message:" + decrypted_text)
else:
    print("Invalid direction. Please try again.")




