"""
This script processes a text input by removing non-alphabetic characters 
and counting the length of each word.
"""

def long_cat_is_long(txt):
    """
    Processes a text to extract words and measure their length.

    :param txt: Input text.
    :return: Dictionary with words as keys and their lengths as values.
    """
    words = txt.lower().split()  # Split the text and convert to lowercase
    words = [''.join(char for char in word if char.isalpha()) for word in words]  # Remove non-alphabetic symbols
    words = [word for word in words if word]  # Filter out empty words
    word_count = {word: len(word) for word in words}  # Store words and their lengths

    return word_count

if __name__ == '__main__':
    INPUT_TEXT = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """

    print(long_cat_is_long(INPUT_TEXT))
