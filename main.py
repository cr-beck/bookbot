import sys
from stats import get_book_word_count
from stats import get_book_character_count
from stats import sort_character_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1]

def get_book_text(book):
    with open(book) as f:
        text = f.read()
        return text
    

def main():
    num_words = get_book_word_count(book)
    character_count = get_book_character_count(book)
    sorted_list = sort_character_count(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for dict in sorted_list:
        #print(dict["char"])
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")


main()