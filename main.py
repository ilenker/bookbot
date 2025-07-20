from stats import get_word_count, get_char_count, sort_char_count
import sys

if not len(sys.argv) == 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    return file_contents                               

def main():
    text = get_book_text()
    char_count = get_char_count(text)
    sorted_char_count = sort_char_count(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}") 
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(text)} total words")
    print("--------- Character Count -------")
    for each in sorted_char_count:
        if each["char"].isalpha():
            print(f"{each["char"]}: {each["num"]}")
    print("============= END ===============")

    return

main()
