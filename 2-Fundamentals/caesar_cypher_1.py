import string
def caesar_cipher(strings, offset):
    new_string = ""
    letters = string.ascii_lowercase
    for element in strings:
        index = letters.index(element)
        new_string += letters[index - offset]
    return new_string