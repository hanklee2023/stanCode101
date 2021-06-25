"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
import time
from collections import Counter

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variable
# dict for dictionary in vocabulary order dictionary is 2 layer dict:
# the first layer key is the first char, and the 2nd layer of key is the first 2 chars.
dict = {}
search_dict = {}

def main():
    found_dict = {}             # To store found Anagram in a dictionary

    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    read_dictionary()
    while True:
        key = input("Find anagrams for:")
        if key == EXIT:
            break
        else:
            find_anagrams(key, found_dict)


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    global dict

    # Local variable for list
    char1_lst = {}
    char2_lst = {}
    char3_lst = {}
    char4_lst = {}
    char5_lst = {}
    char6_lst = {}
    char7_lst = {}
    full_lst = {}

    with open(FILE, 'r') as r:
        for item in r:

            # 1 char lst
            if char1_lst.get(item[0]) is None:
                if len(item[0:len(item)-1]) == 1:
                    char1_lst[item[0]] = 1
                else:
                    char1_lst[item[0]] = 0

            # 2 char lst
            if len(item[0:len(item)-1]) > 1 and char2_lst.get(item[0:2]) is None:
                if len(item[0:len(item)-1]) == 2:
                    char2_lst[item[0:2]] = 1
                else:
                    char2_lst[item[0:2]] = 0

            # 3 char lst
            if len(item[0:len(item)-1]) > 2 and char3_lst.get(item[0:3]) is None:
                if len(item[0:len(item)-1]) == 3:
                    char3_lst[item[0:3]] = 1
                else:
                    char3_lst[item[0:3]] = 0

            # 4 char lst
            if len(item[0:len(item)-1]) > 3 and char4_lst.get(item[0:4]) is None:
                if len(item[0:len(item)-1]) == 4:
                    char4_lst[item[0:4]] = 1
                else:
                    char4_lst[item[0:4]] = 0

            # 5 char lst
            if len(item[0:len(item)-1]) > 4 and char5_lst.get(item[0:5]) is None:
                if len(item[0:len(item)-1]) == 5:
                    char5_lst[item[0:5]] = 1
                else:
                    char5_lst[item[0:5]] = 0

            # 6 char lst
            if len(item[0:len(item) - 1]) > 5 and char6_lst.get(item[0:6]) is None:
                if len(item[0:len(item) - 1]) == 6:
                    char6_lst[item[0:6]] = 1
                else:
                    char6_lst[item[0:6]] = 0

            # 6 char lst
            if len(item[0:len(item) - 1]) > 6 and char6_lst.get(item[0:7]) is None:
                if len(item[0:len(item) - 1]) == 7:
                    char7_lst[item[0:7]] = 1
                else:
                    char7_lst[item[0:7]] = 0

            # full lst
            full_lst[item[0:len(item)-1]] = True

    # print(char1_lst)
    # print(char2_lst)
    # print(char3_lst['amr'])
    # print(char4_lst)
    # print(full_lst)

    for char in char1_lst:
        dict[char] = {}
        if char1_lst[char] == 1:
            dict[char][char] = 1

    for char in char2_lst:
        dict[char[0]][char] = {}
        if char2_lst[char] == 1:
            dict[char[0]][char][char] = 1

    for char in char3_lst:
        dict[char[0]][char[0:2]][char] = {}
        if char3_lst[char] == 1:
            dict[char[0]][char[0:2]][char][char] = 1

    for char in char4_lst:
        dict[char[0]][char[0:2]][char[0:3]][char] = {}
        if char4_lst[char] == 1:
            dict[char[0]][char[0:2]][char[0:3]][char][char] = 1

    for char in char5_lst:
        dict[char[0]][char[0:2]][char[0:3]][char[0:4]][char] = {}
        if char5_lst[char] == 1:
            dict[char[0]][char[0:2]][char[0:3]][char[0:4]][char][char] = 1

    for char in char6_lst:
        dict[char[0]][char[0:2]][char[0:3]][char[0:4]][char[0:5]][char] = {}
        if char6_lst[char] == 1:
            dict[char[0]][char[0:2]][char[0:3]][char[0:4]][char[0:5]][char][char] = 1

    for char in char7_lst:
        dict[char[0]][char[0:2]][char[0:3]][char[0:4]][char[0:5]][char[0:6]][char] = {}
        if char7_lst[char] == 1:
            dict[char[0]][char[0:2]][char[0:3]][char[0:4]][char[0:5]][char[0:6]][char][char] = 1

    for voc in full_lst:
        if len(voc) > 7:
            dict[voc[0]][voc[0:2]][voc[0:3]][voc[0:4]][voc[0:5]][voc[0:6]][voc[0:7]][voc] = 1

    # print(len(dict['c']['co']['con']['cont']['conta']['contai']['contain']))
    # print(len(dict['c']['ca']['can']['cano']['canon']['canoni']['canonis']))
    # print(len(dict['a']['ac']['act']['acti']['actin']['actino']['actinon']))
    # print(len(dict['s']['so']['son']['sona']['sonan']['sonant']['sonanti']))
    # print(len(dict['s']['sa']['san']['sanc']['sanct']['sancti']['sanctio']))
    #
    # print((dict['c']['co']['con']['cont']))
    # print(len(dict['c']['ca']['can']['cano']))
    # print(len(dict['a']['ac']['act']['acti']))
    # print(len(dict['s']['so']['son']['sona']))
    # print(len(dict['s']['sa']['san']['sanc']))

            # if len(item[0:len(item)-1]) == 1:                   # Layer 0 - 1 char
            #     dict[item[0]] = {
            #         item[0:len(item)-1]: True
            #     }
            # elif item[0] in dict:                               # Layer 1 - 2 char
            #     if len(item[0:len(item)-1]) == 2:
            #         dict[item[0]][item[0:2]] = {
            #             item[0:len(item)-1]: True
            #         }
            #     else:
            #         if item[0:2] in dict[item[0]]:              # Layer 2 - 3 char
            #             if len(item[0:len(item)-1]) == 3:
            #                 dict[item[0]][item[0:2]] = {
            #                     item[0:len(item) - 1]: {
            #                         item[0:len(item) - 1]: True
            #                     }
            #                 }
            #             else:
            #                 if item[0:3] in dict[item[0]][item[0:2]]:
            #                     if item[0:4] in dict[item[0]][item[0:2]][item[0:3]]:
            #                         dict[item[0]][item[0:2]][item[0:3]][item[0:4]][item[0:len(item)-1]] = True
            #                     else:
            #                         dict[item[0]][item[0:2]][item[0:3]][item[0:4]] = {}
            #                         dict[item[0]][item[0:2]][item[0:3]][item[0:4]][item[0:len(item) - 1]] = True
            #                 else:
            #                     dict[item[0]][item[0:2]][item[0:3]] = {}
            #         else:
            #             dict[item[0]][item[0:2]] = {}
            #
            #
            # else:
            #     dict[item[0]] = {}


    # print(dict['c']['co'])

    # start_time = time.time_ns()  # To check execution time
    #
    # a = dict.get('abbbbb')
    # if dict['c']['co']['con'].get('contains') is not None:
    # if 'contains' in dict['c']['co']['con']:
    #     print("yes")
    # a = dict['abbbbb']
    #
    # end = time.time_ns()
    # print("--- %s nano-seconds ---" % (end - start_time))
    # start_time = time.time()  # To check execution time
    # count_char('contains', 'c')
    # end = time.time()
    # print("--- %s seconds ---" % (end - start_time))

def find_anagrams(s, found_dict):
    """
    This function is to find anagrams
    :param s            :(str) Key word to search Anagram
    :param found_dict   :(dict) to store found strings
    """
    start_time = time.time()  # To check execution time
    if s in found_dict:
        pass
    else:
        found_dict[s] = []
        find_anagrams_helper(s, "", len(s), found_dict)

    end = time.time()
    print("Searching...")
    print(f'{len(found_dict[s])} anagrams: {found_dict[s]}')
    print("--- %s seconds ---" % (end - start_time))


def find_anagrams_helper(string, current_string, len_string, found_result):
    """
    This is the helper function for find_anagrams
    :param string           :(str) Key word to search Anagram
    :param current_string   :(str) current combined string
    :param len_string       :(int) length of searched string
    :param found_result       :(dict) to store found strings
    """

    global dict

    if len(current_string) == len_string:
        # print(current_string)
        if len_string == 3:
            if dict[current_string[0]][current_string[0:2]].get(current_string).get(current_string):
                if dict[current_string[0]][current_string[0:2]][current_string][current_string] == 1:
                    print("Searching...")
                    print("Found: ", current_string)
                    found_result[string].append(current_string)
        elif len_string == 4:
            if dict[current_string[0]][current_string[0:2]][current_string[0:3]].get(current_string).get(current_string):
                if dict[current_string[0]][current_string[0:2]][current_string[0:3]][current_string][current_string] == 1:
                    print("Searching...")
                    print("Found: ", current_string)
                    found_result[string].append(current_string)
        elif len_string == 5:
            if dict[current_string[0]][current_string[0:2]][current_string[0:3]][current_string[0:4]].get(current_string).get(current_string):
                if dict[current_string[0]][current_string[0:2]][current_string[0:3]][current_string[0:4]][current_string][current_string] == 1:
                    print("Searching...")
                    print("Found: ", current_string)
                    found_result[string].append(current_string)

        else:
            if dict[current_string[0]][current_string[0:2]][current_string[0:3]]\
                    [current_string[0:4]][current_string[0:5]][current_string[0:6]][current_string[0:7]].get(current_string):
                print("Searching...")
                print("Found: ", current_string)
                found_result[string].append(current_string)

    else:
        for char in string:
            if char in current_string and string.count(char) == current_string.count(char):
                # count_char(string, char) == count_char(current_string, char):
                pass
            else:
                # Choose
                current_string += char
                # Explore
                if current_string not in found_result[string]:
                    if has_prefix(current_string):
                        find_anagrams_helper(string, current_string, len_string, found_result)
                # print(current_string)
                # Un-choose
                if len(current_string) > 1:
                    current_string = current_string[0:len(current_string)-1]
                else:
                    current_string = ""


def has_prefix(sub_s):
    """
    This function is find whether any string in dict contains sub string
    :param sub_s:(str) input for sub string to search in dictionary
    :return     :(bool) if get find string for start_with value
    """
    global dict
    global search_dict

    # for string in dict_set:
    #     if string.startswith(sub_s):
    #         return True
    #
    # return False

    # if dict.get(sub_s[0]):
    #     if len(sub_s) == 1:
    #         return True
    #     if dict[sub_s[0]].get(sub_s[0:2]):
    #         for string in dict[sub_s[0]][sub_s[0:2]]:
    #             if string.startswith(sub_s):
    #                 return True
    # return False

    if search_dict.get(sub_s) is not None:

        if search_dict[sub_s]:
            return True
        else:
            return False

    if dict.get(sub_s[0]):
        if len(sub_s) == 1:
            return True
        else:
            if dict[sub_s[0]].get(sub_s[0:2]):
                if len(sub_s) == 2:
                    search_dict[sub_s] = True
                    return True
                else:
                    if dict[sub_s[0]][sub_s[0:2]].get(sub_s[0:3]):
                        if len(sub_s) == 3:
                            search_dict[sub_s] = True
                            return True
                        else:
                            if dict[sub_s[0]][sub_s[0:2]][sub_s[0:3]].get(sub_s[0:4]):
                                if len(sub_s) == 4:
                                    search_dict[sub_s] = True
                                    return True
                                else:
                                    if dict[sub_s[0]][sub_s[0:2]][sub_s[0:3]][sub_s[0:4]].get(sub_s[0:5]):
                                        if len(sub_s) == 5:
                                            search_dict[sub_s] = True
                                            return True
                                        else:
                                            if dict[sub_s[0]][sub_s[0:2]][sub_s[0:3]][sub_s[0:4]][sub_s[0:5]].get(sub_s[0:6]):
                                                if len(sub_s) == 6:
                                                    search_dict[sub_s] = True
                                                    return True
                                                else:
                                                    if dict[sub_s[0]][sub_s[0:2]][sub_s[0:3]][sub_s[0:4]][sub_s[0:5]] \
                                                            [sub_s[0:6]].get(sub_s[0:7]):
                                                        if len(sub_s) == 7:
                                                            search_dict[sub_s] = True
                                                            return True
                                                        else:
                                                            any(string.startswith(sub_s) for string in \
                                                                dict[sub_s[0]][sub_s[0:2]][sub_s[0:3]][sub_s[0:4]] \
                                                                    [sub_s[0:5]][sub_s[0:6]][sub_s[0:7]])
                                                            search_dict[sub_s] = True
                                                            return True
                        # for string in dict[sub_s[0]][sub_s[0:2]][sub_s[0:3]]:
                        #     if string.startswith(sub_s):
                        #         search_dict[sub_s] = None
                        #         return True

    search_dict[sub_s] = False
    return False



if __name__ == '__main__':
    main()
