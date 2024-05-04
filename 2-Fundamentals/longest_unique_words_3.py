def get_n_longest_unique_words(words, n):
    # Define a nested function to extract unique words from the list
    def get_unique_words(words):
        unique_words = []
        # Iterate through each word in the list
        for word in words:
            # Check if the word appears only once in the list
            if words.count(word) == 1:
                unique_words.append(word)
        # Return the list of words that appear exactly once
        return unique_words

    # Retrieve the list of unique words using the nested function
    unique_words = get_unique_words(words)
    # Sort the unique words by length in descending order
    sorted_words = sorted(unique_words, key=len, reverse=True)
    # Return the top 'n' longest words from the sorted list of unique words
    return sorted_words[:n]