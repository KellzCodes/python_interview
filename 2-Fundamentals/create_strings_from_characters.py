def create_strings_from_characters(frequencies, string1, string2):
    # Define a nested function to check if a string can be formed given the character frequencies
    def frequencies_can_form(frequencies, string):
        # Check each unique character in the string
        for character in set(string):
            # If the count of the character in the string exceeds what's available in frequencies, return False
            if string.count(character) > frequencies.get(character, 0):
                return False
        # If all characters can be matched, return True
        return True

    # Check if string1 can be formed from the available frequencies
    can_form_string1 = frequencies_can_form(frequencies, string1)
    # Check if string2 can be formed from the available frequencies
    can_form_string2 = frequencies_can_form(frequencies, string2)

    # Evaluate if either or both strings cannot be formed
    if not can_form_string1 or not can_form_string2:
        # If exactly one of the strings can be formed, return 1
        if can_form_string1 or can_form_string2:
            return 1
        # If neither string can be formed, return 0
        return 0

    # If both strings can potentially be formed, proceed to adjust the frequencies
    for character in string1 + string2:
        # Check if the character is in frequencies and if it has not been depleted
        if character not in frequencies or frequencies[character] == 0:
            # If any character runs out, return 1 (indicates only one string can be fully formed)
            return 1

        # Decrease the count of the character in frequencies for each usage
        frequencies[character] -= 1

    # If all characters needed have been used appropriately without depleting the supply, return 2
    return 2