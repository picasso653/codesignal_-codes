def solution(input_str):
    def word_to_number(word):
        """Convert a letter to its corresponding number (a=1, b=2, etc)"""
        return str(ord(word) - ord('a') + 1)

    def number_to_word(number):
        """Convert a number to its corresponding letter (1=a, 2=b, etc)"""
        return chr(int(number) + ord('a') - 1)

    # Split the input string into words
    words = input_str.split('-')

    # Transform each word
    transformed_words = []
    for word in words:
        if word.isdigit():
            # Convert number to letter if it's in valid range (1-26)
            number = int(word)
            if 1 <= number <= 26:
                transformed_words.append(number_to_word(word))
            else:
                raise ValueError(f"Number {number} is out of valid range (1-26)")
        else:
            # Convert letter to number
            if word.islower() and len(word) == 1:
                transformed_words.append(word_to_number(word))
            else:
                raise ValueError(f"Invalid word: {word}. Must be a single lowercase letter.")

    # Join the transformed words with hyphens
    return "-".join(transformed_words)
