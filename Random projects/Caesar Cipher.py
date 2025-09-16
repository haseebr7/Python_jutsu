alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(encode_or_decode, message, shift_number):

    final_word = ""
    if encode_or_decode == "decode":
        shift_number = -shift_number
        print("Your shifted number: ", shift_number)
    for i in message:
        if i not in alphabet:
            final_word += i
        else:
            var = (alphabet.index(i) + shift_number) % 26
            final_word += alphabet[var]
    print(f"You {encode_or_decode}d message is: {final_word}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(encode_or_decode=direction, message=text, shift_number=shift)
    check = input('Press "Y" to try again and "N" to exit.\n').upper()
    if check == "N":
        should_continue = False
        print("Bye bro 👋")