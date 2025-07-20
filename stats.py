def get_word_count(book):
    word_list = book.split()
    return len(word_list)

def get_char_count(book):
    ascii_list = {}

    for char in book:
        if not char.lower() in ascii_list:
            ascii_list[char.lower()] = 1
        else:
            ascii_list[char.lower()] += 1
    return ascii_list

def sort_on(items):
    return items["num"]

def sort_char_count(char_count):
    sorted_list = []
    for each in char_count:
        sorted_list.append({"char": each, "num": char_count[each]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

