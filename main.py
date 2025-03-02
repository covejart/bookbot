from stats import num_words, num_chars
import sys


def get_book_text(filepath: str) -> str:

    '''
    Prints out a given text file

    Arguments:
        filepath (str): the relative file path to a textfile

    Returns:
        str: the text contained at the given file path
    '''

    with open(filepath) as f:
        content = f.read()
    
    return content


if __name__ == "__main__":
    FILEPATH = sys.argv[1]

    text = get_book_text(FILEPATH)
    word_count = num_words(text)
    chars = num_chars(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {FILEPATH}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    # sorted(iterable, key=None, reverse=True)
    sorted_chars = sorted(chars.items(), key=lambda item: item[1], reverse=True)

    for (char, count) in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}") 
