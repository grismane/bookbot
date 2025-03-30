from stats import get_num_words
from stats import get_char_counts
from stats import sort_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Report
    file_path = f"{sys.argv[1]}"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(get_book_text(file_path))
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_characters = sort_dict(get_char_counts(get_book_text(file_path)))
    for i in sorted_characters:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["count"]}")
    print("============= END ===============")
main()
