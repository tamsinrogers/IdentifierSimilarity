# Code snippets to be used in the survey. Snippets should include either
# similar or different identifiers, validated using objective criteria
# from an IS paper. The relevant lines should be flagged with a comment

# orthographic, phonological, semantic


# funcx_a -> function without identifier similarity
# funcx_b -> function with identifier similarity

# -------------------------------------------------------------------------- #
# SNIPPET 1: SENTENCE TO ALL CAPS
# ORTHOGRAPHIC
def func1_a(input_string):
    return_string = ""
    for current_char in input_string:
        if current_char.isalpha():
            # get ascii value of b
            ascii_value = ord(current_char)
            ascii_value -= 32
            # convert ascii number to char
            upper_char = chr(ascii_value)
            return_string += d
        else:
            return_string += current_char

    return return_string

def func1_b(s):
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

print("func1")
print(
    func1_b("in 2 years, i will get three new pets!")
)
print("\n\n")




# -------------------------------------------------------------------------- #
# SNIPPET 2: SORT EVENS ASCENDING, ODDS DESCENDING
# ORTHOGRAPHIC
def func2_a(input_list):
    # sort the list in ascending order
    input_list = sorted(input_list, reverse=False)
    l = len(input_list)
    evens = []
    odds = []
    for i in range(l):
        if input_list[i] % 2 == 0:
            evens.append(input_list[i])
        else:
            odds.insert(0, input_list[i])
    return evens, odds

def func2_b(lst1):
    # sort the list in ascending order
    lst1 = sorted(lst1, reverse=False)
    l = len(lst1)
    lst2 = []
    lst3 = []
    for i in range(l):
        if lst1[i] % 2 == 0:
            lst2.append(lst1[i])
        else:
            lst3.insert(0, lst1[i])
    return lst2, lst3

print("func2")
print(
    func2_b(
        [6, 8, 35, 17, 0, 9, 45]
    )
)
print("\n\n")




# -------------------------------------------------------------------------- #
# SNIPPET 3: SEPARATE VOWEL WORDS
# ORTHOGRAPHIC
def func3_a(input_string):
    vowel_words = ""
    cons_words = ""
    # for each word in the string
    for word in input_string.split():
        if word[0] in ["a", "e", "i", "o", "u", "y"]:
            vowel_words = vowel_words + word + " "
        else:
            cons_words = cons_words + word + " "

    return vowel_words, cons_words

def func3_b(string):
    words1 = ""
    words2 = ""
    # for each word in the string
    for word in string.split():
        if word[0] in ["a", "e", "i", "o", "u", "y"]:
            words1 = words1 + word + " "
        else:
            words2 = words2 + word + " "

    return words1, words2

print("func3")
print(
    str(
        func3_b("the inclination angle of some galaxy will affect the component of the")
    )
)
print("\n\n")




# -------------------------------------------------------------------------- #
# SNIPPET 4: MOST HOLES IN ONE
# ORTHOGRAPHIC
def func4_a(player_list, scorecard_list):
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

print("func4")
print(
    str(
        func4_a(
            ["Milo", "Ben", "Tamsin"],
            [
                [1, 2, 4, 3, 1, 1, 3],
                [4, 2, 1, 1, 1, 3, 1],
                [6, 2, 1, 3, 4, 3, 2]
            ]    
        ) # should print (Ben, Tamsin)
    )
)
print("\n\n")




# -------------------------------------------------------------------------- #
# SNIPPET 5: LIST VS ARRAY
# SEMANTIC
# list gets only int
# array gets only strs
# if it's a float, add zero to other list
def func5_b(input_list, input_array):
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

print("func5")
print(
    func5(
        [2, "three", "four", 5, 6.7, "seven", "eight", 9, "ten"],
        ["zero", 1, "two", 4.5, 8, 16, "thirty-two", 64.0]
    )
)
print("\n\n")




# -------------------------------------------------------------------------- #
# SNIPPET 6: SMALL STRING, SHORT STRING
# SEMANTIC
def func6_b(str_list):
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

print("func6")
func6(
    ["treble", "bass", "microphone", "amplifier", "guitar", "glasses", "anyone"]
)
print("\n\n")




# -------------------------------------------------------------------------- #
# SNIPPET 7: CHAR VS LETTER
# SEMANTIC
# if a character is in a string, but the full string isn't in the string, print the char
def func7_b(input_list, string):
    output_list = []
    for char in input_list:
        for letter in char:
            add = False
            if letter in string:
                add = True
            if char in string:
                add = False
            if add:
                output_list.append(letter)
    return output_list

print("func7")
print(
    func7(
        ["string", "forget", "about", "i got strings", "whoz dat"],
        "strings are what i got strings are what i need"
    )
)
print("\n\n")




# -------------------------------------------------------------------------- #
# SNIPPET 8: START AND BEGIN
# SEMANTIC
# if you begin while stopped, then start
# if you begin while started, print
# if you stop while started, then end
# if you stop while stopped, print
def func8_b(input_list):
    l = len(input_list)
    i = 0
    start = False
    begin = False
    stop = True
    end = False
    while i < l:
        if input_list[i] != 0 and stop == True:
            begin = True
        elif input_list[i] == 0 and stop == True:
            print(input_list[i])
        elif input_list[i] != 0 and start == True:
            print(input_list[i])
        elif input_list[i] == 0 and start == True:
            end = True

        if end:
            stop = True
            start = False
            begin = False
            end = False
        if begin:
            start = True
            stop = False
            begin = False
            end = False
        
        i += 1

print("func8")
func8(
    [0, 4, 5, 1, 0, 1, 0, 0, 9]
    )
print("\n\n")