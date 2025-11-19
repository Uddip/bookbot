from stats import (
    get_num_words,
    get_characters,
    dict_to_sorted_list
)
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    text = get_book_path(path_to_file)
    num_words = get_num_words(text)
    chars_dict = get_characters(text)
    chars_sorted_list = dict_to_sorted_list(chars_dict)
    print_report(path_to_file, num_words, chars_sorted_list)

def get_book_path(path):
    with open(path) as f:
        return f.read()
    
def print_report(book_path, num_words, chars_sorted_list):
    # print(file_contents)
    # print(f"Number of words: {get_words(file_contents)}")
    # print(f"Number of words: {get_characters(file_contents)}")
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for item in chars_sorted_list:
        if not item['char'].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print(f"============= END ===============")

main()
