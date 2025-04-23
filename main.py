from stats import get_book_word_count
from stats import get_book_character_count
from stats import sort_character_count

def get_book_text(book):
    with open(book) as f:
        text = f.read()
        return text
    

def main():
    #num_words = get_book_word_count("books/frankenstein.txt")
    #print(f"{num_words} words found in the document")
    #print(get_book_character_count("books/frankenstein.txt"))
    character_count = get_book_character_count("books/frankenstein.txt")
    sorted_list = sort_character_count(character_count)
    


main()