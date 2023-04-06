# Code snippets to be used in the survey. Snippets should include either
# similar or different identifiers, validated using objective criteria
# from an IS paper. The relevant lines should be flagged with a comment

# orthographic, phonological, semantic


# FIX TO MAKE WITHOUT BUGS AND PROBABLY SIMPLER FOR MILO
# adding/rolling dice numbers
# splitting and appending lists
# last index in a list

# -------------------------------------------------------------------------- #
# SNIPPET 1: SENTENCE TO ALL CAPS
# ORTHOGRAPHIC
def func1(s):
    a = ""
    for b in s:
        if b.isalpha():
            # get ascii value of b
            c = ord(b)
            c -= 32
            # convert ascii number to char
            d = chr(c)
            a += d
        else:
            a += b

    return a

print(
    func1("In 2 years, I will get three new pets!")
)




# -------------------------------------------------------------------------- #
# SNIPPET 2: SORT EVENS ASCENDING, ODDS DESCENDING
# ORTHOGRAPHIC
def func2(lst1):
    # sort the list in ascending order
    lst1 = sorted(lst1, reverse=False)
    lst2 = []
    lst3 = []
    for number in lst1:
        if number % 2 == 0:
            lst2.append(number)
        else:
            lst3.insert(0, number)
    return lst2, lst3

print(
    func2(
        [6, 8, 35, 17, 0, 9, 45]
    )
)




# -------------------------------------------------------------------------- #
# SNIPPET 3: SEPARATE VOWEL WORDS
# ORTHOGRAPHIC
def separate_vowel_words(string):
    words1 = ""
    words2 = ""
    for word in string.split():
        if word[0] in ["a", "e", "i", "o", "u", "y"]:
            words1 = words1 + word + " "
        else:
            words2 = words2 + word + " "

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
            if scorecard_list[i][j] == 1:
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
# SNIPPET 5: 
# SEMANTIC