def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return(file_contents)

def get_num_words(file_path):
    book_txt = get_book_text(file_path)
    book_txt_array = book_txt.split()
    num_words = len(book_txt_array)
    return(num_words)

def get_num_chars(file_path):
    book_txt = get_book_text(file_path)
    book_txt_lowered = book_txt.lower()
    book_txt_array = list(book_txt_lowered)
    char_counts = {}
    for i in book_txt_array:
        if i in char_counts:
            char_counts[i] += 1
        else:
            char_counts[i] = 1
    return(char_counts)

def sort_dictionary_by_occurrence(file_path):
    dictionary = get_num_chars(file_path)
    sorted_by_value = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    remove_non_alpha = sorted_by_value.copy()
    for i in sorted_by_value:
        if not i.isalpha():
            remove_non_alpha.pop(i)
    return(remove_non_alpha)

def print_dict_by_occurrence(file_path):
    dictionary = sort_dictionary_by_occurrence(file_path)
    for k,v in dictionary.items():
        print(f"{k}: {v}")

def print_report(file_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print(f"----------- Word Count ----------\nFound {get_num_words(file_path)} total words")
    print("--------- Character Count -------")
    print_dict_by_occurrence(file_path)
    print("============= END ===============")
