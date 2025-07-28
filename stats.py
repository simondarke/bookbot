def get_num_words(book):
    print("----------- Word Count ----------")
    num_words = book.split()
    print(f"Found {len(num_words)} total words")

def count_characters(words):
    allowed = "abcdefghijklmnopqrstuvwxyz"
    character_dict = {}
    for word in words:
        for char in word.lower():
            if char in allowed:
                character_dict[char] = character_dict.get(char, 0) + 1
    return character_dict

def sort_on(items):
    return items["num"]

def sort_character_counts(character_dict):
    print("--------- Character Count -------")
    character_list = [];
    for character in character_dict:
        character_list.append({"char": character, "num": character_dict[character]})
    character_list.sort(reverse=True, key=sort_on)
    for character in character_list:
        print(f"{character['char']}: {character['num']}")