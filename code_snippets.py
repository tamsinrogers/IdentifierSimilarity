# Code snippets to be used in the survey. Snippets should include either
# similar or different identifiers, validated using objective criteria
# from an IS paper. The relevant lines should be flagged with a comment




# -------------------------------------------------------------------------- #
# SNIPPET 1: SENTENCE TO ALL CAPS
# BUG MUST BE INTRODUCED
# IDENTIFIERS MUST BE REPLACED BY SIMILAR ONES
def sentence_to_all_caps(s):
    a = ""
    for b in s:
        if b.isalpha():
            c = ord(b)
            c -= 32
            d = chr(c)
            a += b # here is the bug, should be a += d
        else:
            a += b

    return a

print(
    sentence_to_all_caps("this sentence should be printed uppercase>>./1?")
)




# -------------------------------------------------------------------------- #
# SNIPPET 2: SORT NAMES ALPHABETICALLY BY LAST NAME, DISREGARDING FIRST NAME
# IDENTIFIERS MUST BE REPLACED BY SIMILAR ONES
# BUG MUST BE INTRODUCED
def sort_by_last_name(names_list):
    l = len(names_list)
    for i in range(l):
        minindex = i
        for myindex in range(i + 1, l):
            my_last_name = names_list[minindex].split()[-1] # bug here, should be names_list[myindex]
            min_last_name = names_list[minindex].split()[-1]
            check_index = 0
            if ord(my_last_name[check_index].lower()) < ord(min_last_name[check_index].lower()):
                minindex = myindex
        if minindex != i:
            former_i = names_list[i]
            former_min = names_list[minindex]
            names_list[i] = former_min
            names_list[minindex] = former_i
    
    return names_list

print(
    "this list should be alphbetical by last name: " +
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
# SNIPPET 3: SEPARATE VOWEL WORDS
# IDENTIFIERS MUST BE REPLACED BY SIMILAR ONES
# BUG MUST BE INTRODUCED
def separate_vowel_words(string):
    vowel_words = ""
    consonant_words = ""
    for word in string.split():
        if word[0] in ["a", "e", "i", "o", "u"]:
            vowel_words = vowel_words + word + " "
        else:
            consonant_words = consonant_words + word + " "

    return vowel_words, consonant_words

print(
    str(
        separate_vowel_words("the inclination angle of some galaxy will affect the component of the")
    )
)




# -------------------------------------------------------------------------- #
# SNIPPET 4: MOST HOLES IN ONE
# IDENTIFIERS MUST BE REPLACED BY SIMILAR ONES
def most_least_holes_in_one(player_list, scorecard_list):
    l = len(player_list)
    most_holes = 0
    least_holes = 1e9
    most_holes_player = ""
    least_holes_player = ""
    for i in range(l):
        k = len(scorecard_list[i])
        num_hole_in_ones = 0
        for j in range(k):
            if scorecard_list[i][i] == 1: # here is bug, should be [i][j]
                num_hole_in_ones += 1
        if num_hole_in_ones > most_holes:
            most_holes_player = player_list[i]
            most_holes = num_hole_in_ones
        if num_hole_in_ones < least_holes:
            least_holes_player = player_list[i]
            least_holes = num_hole_in_ones

    return most_holes_player, least_holes_player

print(
    str(
        most_least_holes_in_one(
            ["Milo", "Ben", "Tamsin"],
            [
                [1, 2, 4, 3, 1, 1, 3],
                [4, 2, 1, 1, 1, 3, 1],
                [6, 2, 1, 3, 4, 3, 2]
            ]    
        ) # should print (Ben, Tamsin)
    )
)