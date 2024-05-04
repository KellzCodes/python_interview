def get_n_longest_unique_words(words, n):
    # Define a nested function to extract unique words from the list
    def get_unique_words(words):
        unique_words = []
        # Iterate through each word in the list
        for word in words:
            # Check if the word appears only once in the list
            if words.count(word) == 1:
                unique_words.append(word)
        return unique_words

    # Call the nested function to get a list of unique words
    unique_words = get_unique_words(words)
    # Initialize a list to store the longest words found
    longest_words = []

    # Continue until we have found 'n' longest words
    while len(longest_words) < n:
        current_longest = ""  # Start with an empty string to find the longest
        for word in unique_words:
            # Check if the current word is longer than the current longest word found
            if len(word) > len(current_longest):
                current_longest = word  # Update current longest word

        # Remove the longest word found from the unique words list to avoid re-selecting it
        unique_words.remove(current_longest)
        # Add the longest word to the list of longest words
        longest_words.append(current_longest)

    # Return the list of the 'n' longest unique words
    return longest_words