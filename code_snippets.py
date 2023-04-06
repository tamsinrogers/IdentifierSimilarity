# Code snippets to be used in the survey. Snippets should include either
# similar or different identifiers, validated using objective criteria
# from an IS paper. The relevant lines should be flagged with a comment

import math
import random


# -------------------------------------------------------------------------- #
# SNIPPET 1: SENTENCE TO ALL CAPS
# ORTHOGRAPHIC
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
# ORTHOGRAPHIC
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
# ORTHOGRAPHIC
def separate_vowel_words(string):
    words1 = ""
    words2 = ""
    for word in string.split():
        if word[0] in ["a", "e", "i", "o", "u"]:
            words1 = words1 + word + " "
        else:
            words1 = words2 + word + " " # here is the bug, should be words2 = ...

    return words1, words2

print(
    str(
        separate_vowel_words("the inclination angle of some galaxy will affect the component of the")
    )
)




# -------------------------------------------------------------------------- #
# SNIPPET 4: MOST HOLES IN ONE
# ORTHOGRAPHIC
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


# -------------------------------------------------------------------------- #
# SNIPPET ?:
# PHONOLOGICAL

def sort_table(table):

    table_rows = len(table)
    table_cols = len(table[0])

    labels = []
    for col in range(table_cols):
        labels.append(table[0][col])

    labels.sort()

    sort_idxs = []
    for label in labels:
        sort_idxs.append(table[0].index(label))

    sorted_table = []
    for row in range(table_rows):

        sorted_row = []
        for col in range(table_cols):
            sorted_row.append(table[row][sort_idxs[col]])

        sorted_table.append(sorted_row)

    return sorted_table


table = [['bannana', 'cat', 'apple'],
         [10, 4, 8],
         [2, 3, -9]]

print(sort_table(table))


# -------------------------------------------------------------------------- #
# SNIPPET ?:
# PHONOLOGICAL

def store_scores(csv, scores, names=None):

    try:
        store = open(csv, 'r')
    except FileNotFoundError:
        store = open(csv, 'w')
        if names is None:
            print('Error: path to file with headers OR list of name required')
            return None
        store.write(','.join(names))


# -------------------------------------------------------------------------- #
# SNIPPET ?:
# PHONOLOGICAL

def cast_cat(map, cats, to='int'):

    inv_map = {val: key for key, val in map.items()}

    cast_vals = []

    for cat in cats:

        if to == 'int':
            if type(cat) is int:
                cast_vals.append(cat)
            elif type(cat) is str:
                cast_vals.append(map[cat])

        elif to == 'str':
            if type(cat) is str:
                cast_vals.append(cat)
            elif type(cat) is int:
                cast_vals.append(inv_map[cat])

    return cast_vals

map = {'dog': 1, 'cat': 2, 'lizard': 3, 'bird': 4}
cats1 = [1, 3, 2, 1, 4]
cats2 = ['dog', 1, 3, 'bird']
print(cast_cat(map, cats1, 'str'))


import math

def wave(n_points, wave_nu):

    new = []

    for n in range(n_points):

        x = math.pi*n
        y = math.sin(wave_nu*x)
        new.append(round(y, 2))

    return new

print(wave(4, 0.5))


# ROW RHO
import random

def rand_sparse(n, rho):
    mat = []
    for row in range(n):
        new_row = []
        for col in range(n):
            if random.random() < rho:
                new_row.append(1)
            else:
                new_row.append(0)
        mat.append(new_row)

    return mat


mat = rand_sparse(3, 0.5)

for row in mat:
    print(row)

# question: something like "which of the following are plausible output"
