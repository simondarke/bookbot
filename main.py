from stats import get_num_words, count_characters, sort_character_counts
import sys

def get_book_text(bookPath):
    with open(bookPath) as f:
        return f.read()

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) > 1:
        file_contents = get_book_text(sys.argv[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(f"Analyzing book found at {sys.argv[1]}")

    get_num_words(file_contents)
    sort_character_counts(count_characters(file_contents))
    print("============= END ===============")

main()