def is_valid_string(string):
  """
  Checks if a string is valid based on character frequencies.

  Args:
    string: The input string.

  Returns:
    "YES" if the string is valid, "NO" otherwise.
  """

  # Count character frequencies
  char_counts = {}
  for char in string:
    char_counts[char] = char_counts.get(char, 0) + 1

  # Check if all frequencies are equal
  if len(set(char_counts.values())) == 1:
    return "YES"

  # Try removing one character and checking again
  for i, char in enumerate(string):
    new_counts = char_counts.copy()
    del new_counts[char]
    if len(set(new_counts.values())) == 1:
      return "YES"

  # No valid string found
  return "NO"

# Get input string from the user
input_string = input("Enter a string: ")

# Check if the string is valid
result = is_valid_string(input_string)

# Print the result
print(result)