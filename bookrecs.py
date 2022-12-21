"""Used to Organize the Dictionary"""
from collections import OrderedDict

rating_list = []
reader_rating = []
book_list = []
key_list = []  # list_3
rating_list = []  # list_1
reader_rating = []  # list_2
reader_info = {}  # dictionary_1
reader_info_sorted = {}  # dictionary_2

def open_file(string, list_variable):
    """takes a string/filename turns file into list attached to listVariable."""
    with open(string, "r", encoding='utf-8') as file:
        file = file.readlines()
        for line in file:
            list_variable.append(line.strip())

def search_keys_by_val(dictionary, by_val):
    """compares values and ensures that the books with the correct rating conditions are met"""
    items_list = dictionary.items()
    for item in items_list:
        if symbol.strip() == "=":
            if item[1] == by_val:
                key_list.append(item[0])
        elif symbol.strip() == ">":
            if item[1] >= by_val:
                key_list.append(item[0])
        elif symbol.strip() == "<":
            if item[1] < by_val:
                key_list.append(item[0])
    return key_list

# Opens the files and pushes them into a listVariable
open_file("ratings.txt", rating_list)
open_file("booklist.txt", book_list)

def sort_and_print_logic(list_1, list_2, dictionary_1, list_3, dictionary_2):
    """The sorting logic"""
    for i, key in enumerate(rating_list):
        # Iterates through the rating list
        # checking the name in rating list is == to the name in lowercase.
        if list_1[i].lower().strip() == lname:
            list_2 = list(list_1[i+1].split(" "))
            dictionary_1 = dict(zip(book_list, list_2))
            print("Books for " + name + ":")
            # Organizes the dictionary alphabetically
            dictionary_2 = OrderedDict(
                sorted(dictionary_1.items(), key=lambda t: t[0]))
            list_3 = search_keys_by_val(dictionary_1, rating)
            # Pulling the items that match those sorted in the keyList
            if len(list_3) == 0:
                print("No Books Found!")
            else:
                for key in reversed(dictionary_2):
                    if key in list_3:
                        print(f"{key}\t{dictionary_2[key]}")
                break
        elif i+1 == len(list_1):
            print("No such reader " + name)

while True:
    #print("You will enter three inputs, name, symbol, rating. One at a time")
    name = input("Enter a reader's name: ")
    if name == '':
        print("bye!")
        break
    lname = name.lower().strip()
    symbol = input("Enter a symbol: ")
    if symbol == '':
        print("bye!")
        break
    rating = input("Enter a rating: ")
    if rating == '':
        print("bye!")
        break
    sort_and_print_logic(rating_list, reader_rating,reader_info, key_list, reader_info_sorted)

    #Could refactor once more on the exit statement and the inputs.
    #name, symbol, rating = input("Enter a reader's name: *separate using | * ").split("|")
