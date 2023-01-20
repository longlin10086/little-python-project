import art


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, cipher_direction):
    cipher_text = ""
    if cipher_direction[0] == "d":
        shift_amount *= -1
    for char in plain_text:
        if char in alphabet:
            i = alphabet.index(char)
            i = (i+shift_amount) % 26
            cipher_text += alphabet[i]
        else:
            cipher_text += char
    print(f"The {cipher_direction} text is:")
    print(f"{cipher_text}")


if __name__ == '__main__':
    print(art.logo)
    flag = True
    while flag:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(text, shift, direction)

        answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if answer[0] == "n":
            flag = False
            print("Goodbye")