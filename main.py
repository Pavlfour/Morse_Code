from morse import morse_code

user_text = input("Give me a text to convert into morse code: ")

final_word = ''
for letter in user_text:
    for key in morse_code.keys():
        if letter.upper() == key:
            final_word += morse_code[key] + " " + " " + " "

print(final_word)