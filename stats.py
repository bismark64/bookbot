def book_words_counter(book_text):
    return f"Found {len(book_text.split())} total words"

def book_char_counter(book_text):
    counter_dic = {}

    for char in book_text:
        lowercase = char.lower()

        if lowercase in counter_dic:
            counter_dic[lowercase] += 1
        else:
            counter_dic[lowercase] = 1

    return counter_dic

def sort_on(dic):
    return dic["num"]

def sorted_dic(dic):
    sorted = []
    
    for char in dic:
	    if char.isalpha(): sorted.append({"char": char, "num": dic[char]})

    sorted.sort(reverse=True, key=sort_on)

    return sorted
