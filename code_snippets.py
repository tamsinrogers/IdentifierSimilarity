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
def func3(string):
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
        func3("the inclination angle of some galaxy will affect the component of the")
    )
)




# -------------------------------------------------------------------------- #
# SNIPPET 4: MOST HOLES IN ONE
# ORTHOGRAPHIC
def func4(player_list, scorecard_list):
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
        func4(
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
# SNIPPET 5: LIST VS ARRAY
# SEMANTIC
# list gets only int
# array gets only strs
# if it's a float, add zero to other list
def func5(input_list, input_array):
    i = 0
    while i < len(input_list):
        print(i)
        if type(input_list[i]) == str:
            input_array.append(input_list[i])
            input_list.remove(input_list[i])
        elif type(input_list[i]) == float:
            input_array.append("0")
            input_list.remove(input_list[i])
        else:
            i += 1
    j = 0
    while j < len(input_array):
        if type(input_array[j]) == int:
            input_list.append(input_array[j])
            input_array.remove(input_array[j])
        elif type(input_array[j]) == float:
            input_list.append(0)
            input_array.remove(input_array[j])
        else:
            j += 1
    
    return input_list, input_array

print(
    func5(
        [2, "three", "four", 5, 6.7, "seven", "eight", 9, "ten"],
        ["zero", 1, "two", 4.5, 8, 16, "thirty-two", 64.0]
    )
)




# -------------------------------------------------------------------------- #
# SNIPPET 6: SMALL STRING, SHORT STRING
# SEMANTIC
def func6(str_list):
    short_string = False
    small_string = False
    for little_string in str_list:
        if len(little_string) < 5:
            short_string = True
        else:
            if len(little_string) < 10:
                small_string = True
        if short_string:
            print(little_string[0])
        elif small_string:
            print(short_string)
        else:
            print(little_string[1])
        short_string = False
        small_string = False

func6(
    ["treble", "bass", "microphone", "amplifier", "guitar", "glasses", "anyone"]
)




# -------------------------------------------------------------------------- #
# SNIPPET 7: NUMBER VS INTEGER
# SEMANTIC
# if a character is in a string, but the full string isn't in the string, print the char
def func7(input_list, target):
    output_list = []
    for char in input_list:
        for letter in char:
            add = False
            if letter in target:
                add = True
            if char in target:
                add = False
            if add:
                output_list.append(letter)
    return output_list

print(
    func7(
        ["string", "forget", "about", "i got strings", "whoz dat"],
        "strings are what i got strings are what i need"
    )
)




# -------------------------------------------------------------------------- #
# SNIPPET 7: NUMBER VS INTEGER
# SEMANTIC