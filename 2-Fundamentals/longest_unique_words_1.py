def get_n_longest_unique_words(words, n):
    # Initialize a dictionary to store word frequencies
    dictionary = {}
    # Initialize a list to hold words that occur exactly once
    unique = []

    # Count the frequency of each word in the input list
    for word in words:
        # Increment the count for each word, defaulting to 0 if the word isn't already in the dictionary
        dictionary[word] = dictionary.get(word, 0) + 1

    # Iterate through the dictionary to find words that occur only once
    for key, value in dictionary.items():
        if value == 1:
            # Append unique words to the list
            unique.append(key)

    # Sort the unique words list by the length of the words
    sorting = sorted(unique, key=len)
    # Reverse the sorted list to have the longest words first
    final_list = sorting[::-1]
    # Return the first 'n' longest unique words
    return final_list[:n]
