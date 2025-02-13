def rotate_characters(s: str) -> str:
    """
    Rotates characters in words to their opposite in the alphabet and reorders words.

    Args:
        s (str): Input string containing words separated by spaces

    Returns:
        str: Transformed string with rotated characters and reordered words
    """
    # Create mapping for lowercase and uppercase letters
    lower_map = str.maketrans(
        'abcdefghijklmnopqrstuvwxyz',
        'zyxwvutsrqponmlkjihgfedcba'
    )
    upper_map = str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    )

    # Split the string into words
    words = s.split()

    # Transform each word
    transformed_words = []
    for word in words:
        # Transform lowercase and uppercase characters separately
        new_word = ''
        for char in word:
            if char.islower():
                new_word += char.translate(lower_map)
            else:
                new_word += char.translate(upper_map)
        transformed_words.append(new_word)

    # Reorder words: last word first, followed by others in original order
    if transformed_words:
        result = [transformed_words[-1]] + transformed_words[:-1]
        return ' '.join(result)
    return ''


# Test cases
test_cases = [
    "CapitaL letters",
    "Hello World",
    "abcDEF",
    "Testing OneTwoThree",
    "A"
]

# Run test cases
for test in test_cases:
    result = rotate_characters(test)
    print(f"Input:  {test}")
    print(f"Output: {result}\n")