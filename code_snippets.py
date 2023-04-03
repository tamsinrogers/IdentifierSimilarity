# Code snippets to be used in the survey. Snippets should include either
# similar or different identifiers, validated using objective criteria
# from an IS paper. The relevant lines should be flagged with a comment




# -------------------------------------------------------------------------- #
# SNIPPET 1: SENTENCE TO ALL CAPS
# BUG MUST BE INTRODUCED
# IDENTIFIERS MUST BE REPLACED BY SIMILAR ONES
def sentence_to_all_caps(sentence):
    new_str = ""
    for letter in sentence:
        if letter.isalpha():
            ascii_num = ord(letter)
            ascii_num -= 32
            new_char = chr(ascii_num)
        else:
            new_char = letter
        new_str += new_char

    return new_str

print(
    sentence_to_all_caps("this sentence should be printed uppercase>>./1?")
)




# -------------------------------------------------------------------------- #
# SNIPPET 2: SORT NAMES ALPHABETICALLY BY LAST NAME
# IDENTIFIERS MUST BE REPLACED BY SIMILAR ONES
# BUG MUST BE INTRODUCED
def sort_by_last_name(names_list):
    l = len(names_list)
    for i in range(l):
        min_index = i
        for j in range(i + 1, l):
            j_last_name = names_list[j].split()[-1]
            min_last_name = names_list[min_index].split()[-1]
            check_index = 0
            while ord(j_last_name[check_index].lower()) == ord(min_last_name[check_index].lower()):
                check_index += 1
                if check_index > len(j_last_name) - 1 or check_index > len(min_last_name) - 1:
                    check_index = 0
                    break
            if ord(j_last_name[check_index].lower()) < ord(min_last_name[check_index].lower()):
                min_index = j
        if min_index != i:
            former_i = names_list[i]
            former_min = names_list[min_index]
            names_list[i] = former_min
            names_list[min_index] = former_i
    
    return names_list

print(
    "this list should be alphbetical by last name:" +
    str(
        sort_by_last_name(
            [
                "Ben Raivel",
                "Tamsin Rogers",
                "Someone Rogers",
                "Milo Lani-Caputo",
                "Alan Turing",
                "Nelson Mandela",
                "George W. Bush"
            ]
        )
    )
)




# -------------------------------------------------------------------------- #
# SNIPPET 2: WHICHEVER METHOD
# IDENTIFIERS MUST BE REPLACED BY SIMILAR ONES
# BUG MUST BE INTRODUCED
