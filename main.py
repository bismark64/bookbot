import sys
from stats import book_words_counter, book_char_counter, sorted_dic

def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    char_counter_dictionary = book_char_counter(book_text) 
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(book_words_counter(book_text))
    print("--------- Character Count -------")
    dic_list = sorted_dic(char_counter_dictionary)
    for dic in dic_list:
        print(f"{dic['char']}: {dic['num']}")
    print("============= END ===============")


main()
