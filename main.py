def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        # print(file_contents)
        # print(f"Number of words: {get_words(file_contents)}")
        # print(f"Number of words: {get_characters(file_contents)}")
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{get_words(file_contents)} words found in the document")
        
        list_of_dict = dict_to_sorted_list(get_characters(file_contents))

        for item in list_of_dict:
            print(f"The '{item['char']}' character was foumd {item['num']} times")

        print("--- End report ---")
    return

def sort_on(item):
    return item["num"]

def get_words(contents):
    words = contents.split()
    return len(words)

def get_characters(contents):
    char_dict = {}
    lower_case_string = contents.lower()
    for char in lower_case_string:
        if (char.isalpha()):
            char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def dict_to_sorted_list(dict):
    sorted_list = []
    sorted_list = [{"char": k, "num": v} for k, v in dict.items()]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list 

main()
