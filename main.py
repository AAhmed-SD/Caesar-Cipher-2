alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.

# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.


def caesar(original_text, shift_amount, encode_or_decode):
        output_text = ""
        for letter in original_text:

            if encode_or_decode == "decode":
                shift_amount *= -1
        else:
            shift_amount += 1

            shift_position = alphabet.index(letter) + shift_amount
            shift_position = shift_amount % len(alphabet)
            output_text += alphabet[shift_position]
            print(f"Here is the {encode_or_decode}d result {output_text}")




caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)





