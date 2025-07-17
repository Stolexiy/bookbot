import argparse

from stats import count_words, count_chars, sort_chars_count
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    args = get_arguments()
    book_path = args[0]

    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_num = count_chars(book_text)
    sorted_chars = sort_chars_count(char_num)
    print_report(book_path, num_words, sorted_chars)

def get_arguments():
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1:]

def print_report(path, words_count, chars_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for item in chars_count:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
