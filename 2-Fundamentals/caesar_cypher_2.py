def caesar_cipher(string, offset):
    # Define the alphabet as a list of characters in order
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Initialize an empty string to store the encoded result
    encoded_string = ''

    # Iterate over each character in the input string
    for character in string:
        # Find the index of the current character in the alphabet list
        position = alphabet.index(character)
        # Calculate the new position by subtracting the offset
        offset_position = position - offset
        # Get the character at the new position in the alphabet
        encoded_character = alphabet[offset_position]
        # Append the encoded character to the result string
        encoded_string += encoded_character

    # Return the fully encoded string
    return encoded_string
