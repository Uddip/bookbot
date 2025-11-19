def get_num_words(contents):
    words = contents.split()
    return len(words)

def get_characters(contents):
    char_dict = {}
    lower_case_string = contents.lower()
    for char in lower_case_string:
      char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def dict_to_sorted_list(dict):
    sorted_list = []
    for key in dict:
        sorted_list.append({"char": key, "num": dict[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list 

def sort_on(item):
    return item["num"]