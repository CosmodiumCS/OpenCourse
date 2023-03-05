# for this module's practice:
# we will make an encoder program

# created by : C0SM0

# to save us time
# we will create our 'encoded_alphabet' variable in a python shell
"""
>>> alphabet = "abcdefghijklmnopqrstuvwxyz"
>>> reversed_alph = alphabet[::-1]
>>> for index in range(26):
...  print(f"\t\"{alphabet[index]}\":\"{reversed_alph[index]}\",")
"""

# our alphabet we will use to encode text
encoded_alphabet = {
    "a":"z",
    "b":"y",
    "c":"x",
    "d":"w",
    "e":"v",
    "f":"u",
    "g":"t",
    "h":"s",
    "i":"r",
    "j":"q",
    "k":"p",
    "l":"o",
    "m":"n",
    "n":"m",
    "o":"l",
    "p":"k",
    "q":"j",
    "r":"i",
    "s":"h",
    "t":"g",
    "u":"f",
    "v":"e",
    "w":"d",
    "x":"c",
    "y":"b",
    "z":"a"
}
# symbols that can't be encoded
symbols = "~!@#$%^&*()_+=-0987654321`{}[]|\:;\"'?><,./"

# banner
print("Basic Encoder")

# option menu
print("Choose an Option:\n1) Encode\n2) Decode\n")
# user input, option
option = input("Option : ")
# user input, message
message = input("Enter text to translate : ")

# empty output variable
output = ""

# iterates through message characters
for character in message:
    # iterates through encoded alphabet dictionary
    for standard, encoded in encoded_alphabet.items():
        # encoding process
        if option == "1":
            # checks if character is lowercase
            if character.islower() and character == standard:
                output += encoded
                break
            # checks if character is uppercase
            if character.isupper() and character.lower() == standard:
                output += encoded.upper()
                break

        # decoding process
        if option == "2":
            # checks if character is lowercase
            if character.islower() and character == encoded:
                output += standard
                break
            # checks if character is uppercase
            if character.isupper() and character.lower() == encoded:
                output += standard.upper()

        # adds unrecognized characters to outpur, avoids exceptions
        if character in symbols:
            output += character
            break

# output endoded/decoded message
print(output)

# feel free to keep practicing, here are some more ideas
"""
- fake identity generator
- basic language translator
"""