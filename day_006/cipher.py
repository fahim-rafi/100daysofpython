import string

alphabets = list(string.ascii_lowercase)
keep_play = True


def cipher(enc_text, shift):
    code_msg = ""
    for i in range(0, len(enc_text)):
        num = (alphabets.index(enc_text[i]) + shift) % 26
        code_msg += alphabets[num]
    print(f"Your decrypted text is: {code_msg}")


def decipher(code_msg, shift):
    enc_text = ""
    for i in range(0, len(code_msg)):
        num = (alphabets.index(code_msg[i]) - shift) % 26
        enc_text += alphabets[num]
    print(f"Your decrypted text is: {enc_text}")


while keep_play is True:
    mode_op = input(
        "Do you wish to encrypt (e) or decrypt (d) a message? [e/d]: ")
    if mode_op == 'e':
        enc_text = input("Please enter your text to encrypt: ").lower()
        shift = int(input("Please enter the code of encryption: "))
        cipher(enc_text, shift)
        ask = input("Do you wish to perform another operation? [y/n]: ")
        if ask == 'n':
            keep_play = False
    elif mode_op == 'd':
        dec_text = input("Please enter your text to decrypt: ").lower()
        shift = int(input("Please enter the code of decryption: "))
        decipher(dec_text, shift)
        ask = input("Do you wish to perform another operation? [y/n]: ")
        if ask == 'n':
            keep_play = False
