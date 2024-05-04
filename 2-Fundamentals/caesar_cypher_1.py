import string

def caesar_cypher(strings, offset):
    # Initialize an empty string to hold the result of the cipher
    new_string = ""
    # Access a string of all lowercase letters from the string module
    letters = string.ascii_lowercase

    # Iterate over each character in the input string
    for element in strings:
        # Get the current character's index in the alphabet
        index = letters.index(element)
        # Calculate the new index by subtracting the offset
        new_index = index - offset
        # Append the character at the new index to the new string
        new_string += letters[new_index]

    # Return the modified string after processing all characters
    return new_string
