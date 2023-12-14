alphabet = [chr(i) for i in range(97, 123)]

keepGoing = True
while keepGoing:

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
        userContinue = input("Do you want to keep going?y/n ").lower()

        if userContinue == "y":
            continue
        else:
            keepGoing = False


    elif direction == "decode":
        decrypted_text = decrypt(text, shift)
        print("Decrypted message:" + decrypted_text)
        userContinue = input("Do you want to keep going?y/n ").lower()

        if userContinue == "y":
            continue
        else:
            keepGoing = False
    else:
        
        userContinue = input("Invalid direction. Do you want to keep going?y/n ").lower()

        if userContinue == "y":
            continue
        else:
            keepGoing = False



