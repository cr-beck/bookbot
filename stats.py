def get_book_word_count(book):
    with open(book) as f:
        text = f.read()
        words = text.split()
        word_count = 0
        for word in words:
            word_count +=1
        return word_count
    
def get_book_character_count(book):
    with open(book) as f:
        text = f.read()
        words = text.split()
        character_count = {}
        for word in words:
            for character in word:
                character = character.lower()
                if character in character_count:
                    character_count[character] += 1
                else:
                    character_count[character] = 1
        return character_count