def highest_frequency_word_length(input_string):
    """
    Counts word frequencies in a string and returns the length of the most frequent word.
    """

    word_counts = {}  # Dictionary to store word frequencies

    # Split the string into words and count their occurrences
    for word in input_string.split():
        word_counts[word] = word_counts.get(word, 0) + 1

    # Find the word with the highest frequency
    highest_frequency_word = max(word_counts, key=word_counts.get)

    # Return the length of the highest-frequency word
    return len(highest_frequency_word)

# Get input string from the user
input_string = input("Enter a string: ")

# Get the length of the highest-frequency word
result = highest_frequency_word_length(input_string)

# Print the result
print("Length of the highest-frequency word:", result)