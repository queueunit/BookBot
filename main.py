import re
import sys
from stats import (
        get_book_text,
        get_num_words,
        get_letter_count,
        sort_on,
        chars_dict_to_sorted_list,
        )

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        num_words = get_num_words(text)
        letters = get_letter_count(text)
        sorted_characters = chars_dict_to_sorted_list(letters)
        print_report(sys.argv[1], num_words, sorted_characters)
    
def print_report(book: str, num_words: int, sorted_chars: list[tuple[str,int]]):
    print(f'''============ BOOKBOT ============
Analyzing book found at {book}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------''')

    for tup in sorted_chars:
        if tup[0].isalpha():
            print(f'{tup[0]}: {tup[1]}')

    print("============= END ===============")

main()

