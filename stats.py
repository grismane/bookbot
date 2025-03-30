def get_num_words(book_text):
    return len(book_text.split())

def get_char_counts(book_text):
    # returns a dictionary of characters and their counts

    char_counts = {}
    for char in book_text:
        try:
            char_counts[char.lower()] += 1
        except:
            char_counts[char.lower()] = 1

    return (char_counts)

def sort_dict(dict):
    # takes a dictionary of characters and their counts and returns a sorted list of dictionaries
    
    char_list = []
    for item in dict:
        char_dict = {
            "char": item,
            "count": dict[item]
        }
        char_list.append(char_dict)
    def sort_on(dict):
        return dict["count"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list

