from stats import *
import sys

def get_book_text(filepath):
    print(f"Analyzing book found at {filepath}...")
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    arguments = sys.argv
    if len(arguments) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = arguments[1]
    book_text = get_book_text(book_path)
    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_characters = sort_character_count(count_characters(book_text))

    for char in sorted_characters:
        if char["name"].isalpha() == False:
            continue
        print(f"{char["name"]}: {char["num"]}")
    print("============= END ===============")
    return 0

main()