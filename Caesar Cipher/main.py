
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == 'decode':
        shift_amount *= -1
    elif encode_or_decode=='encode':
        shift_amount*=1


    for letter in original_text:
        if letter==" ":
            output_text+=" "
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")



    def user_in():
        user_input = input("Type 'yes👍🏻' if you want to go again. Otherwise, type 'no👎🏻'. ").lower()
        if user_input=="yes":
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
            if direction == "encode" or direction == "decode":
                text = input("Type your message:\n").lower()
                if text == "":
                    print("Invalid input❌,please enter text")
                else:
                    shift = input("Type the shift number:\n")
                    if shift == '':
                        shift = 0
                        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
                    else:
                        shift = int(shift)
                        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

            else:
                print("Invalid input❌,Please enter 'encode' or 'decode' ")


        elif user_input=="no":
            print("goodbye")
        else:
            print("Invalid input❌,Please enter 'yes' or 'no' ")
            user_in()
    user_in()


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
if direction=="encode" or direction=="decode" :
    text = input("Type your message:\n").lower()
    if text=="":
        print("Invalid input❌,please enter text")
    else:
        shift =input("Type the shift number:\n")
        if shift=='':
            shift=0
            caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
        else:
            shift=int(shift)
            caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

else:
    print("Invalid input❌,Please enter 'encode' or 'decode' ")







