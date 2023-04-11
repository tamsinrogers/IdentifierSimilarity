# Code snippets to be used in the survey. Snippets should include either
# similar or different identifiers, validated using objective criteria
# from an IS paper. The relevant lines should be flagged with a comment

# orthographic, phonological, semantic


# funcx_a -> function without identifier similarity
# funcx_b -> function with identifier similarity

# -------------------------------------------------------------------------- #
# SNIPPET 1: SENTENCE TO ALL CAPS
# ORTHOGRAPHIC
def func1_a(t):
    a = ""
    for u in t:
        if u.isalpha():
            # get ascii value of b
            x = ord(u)
            x -= 32
            # convert ascii number to char
            z = chr(x)
            a += z
        else:
            a += u

    return a

def func1_b(p):
    q = ""
    for b in p:
        if b.isalpha():
            # get ascii value of b
            g = ord(b)
            g -= 32
            # convert ascii number to char
            d = chr(g)
            q += d
        else:
            q += b

    return q

print("func1")
print(
    func1_b("in 2 years, i will get three new pets!")
)
print("\n\n")




# -------------------------------------------------------------------------- #
# SNIPPET 2: SORT EVENS ASCENDING, ODDS DESCENDING
# ORTHOGRAPHIC
def func2_a(a):
    # sort the list in ascending order
    a = sorted(a, reverse=False)
    l = len(a)
    u = []
    t = []
    for i in range(l):
        if a[i] % 2 == 0:
            u.append(a[i])
        else:
            t.insert(0, a[i])
    return u, t

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
def func3_a(t):
    x = ""
    u = ""
    # for each word in the string
    for z in t.split():
        if z[0] in ["a", "e", "i", "o", "u", "y"]:
            x = x + z + " "
        else:
            u = u + z + " "

    return x, u

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
def func4_a(a, b):
    l = len(a)
    u = 0
    m = 1e9
    c = ""
    x = ""
    for i in range(l):
        k = len(b[i])
        r = 0
        for j in range(k):
            if b[i][j] == 1:
                r += 1
        if r > u:
            c = a[i]
            u = r
        if r < m:
            x = a[i]
            m = r

    return c, x

def func4_b(player_list, scorecard_list):
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
def func5_a(a, b):
    i = 0
    while i < len(a):
        print(i)
        if type(a[i]) == str:
            b.append(a[i])
            a.remove(a[i])
        elif type(a[i]) == float:
            b.append("0")
            a.remove(a[i])
        else:
            i += 1
    j = 0
    while j < len(b):
        if type(b[j]) == int:
            a.append(b[j])
            b.remove(b[j])
        elif type(b[j]) == float:
            a.append(0)
            b.remove(b[j])
        else:
            j += 1
    
    return a, b

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
    func5_a(
        [2, "three", "four", 5, 6.7, "seven", "eight", 9, "ten"],
        ["zero", 1, "two", 4.5, 8, 16, "thirty-two", 64.0]
    )
)
print("\n\n")




# -------------------------------------------------------------------------- #
# SNIPPET 6: SMALL STRING, SHORT STRING
# SEMANTIC
def func6_a(a):
    b = False
    c = False
    for x in a:
        if len(x) < 5:
            b = True
        else:
            if len(x) < 10:
                c = True
        if b:
            print(x[0])
        elif c:
            print(b)
        else:
            print(x[1])
        b = False
        c = False

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
func6_a(
    ["treble", "bass", "microphone", "amplifier", "guitar", "glasses", "anyone"]
)
print("\n\n")




# -------------------------------------------------------------------------- #
# SNIPPET 7: CHAR VS LETTER
# SEMANTIC
# if a character is in a string, but the full string isn't in the string, print the char
def func7_a(a, b):
    output_list = []
    for substring in a:
        for char in c:
            x = False
            if char in b:
                x = True
            if c in b:
                x = False
            if x:
                output_list.append(char)
    return output_list
    
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
    func7_a(
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
def func8_a(a):
    l = len(a)
    i = 0
    b = False
    c = False
    x = True
    y = False
    while i < l:
        if a[i] != 0 and x == True:
            c = True
        elif a[i] == 0 and x == True:
            print(a[i])
        elif a[i] != 0 and b == True:
            print(a[i])
        elif a[i] == 0 and b == True:
            y = True

        if y:
            x = True
            b = False
            c = False
            y = False
        if c:
            b = True
            x = False
            c = False
            y = False
        
        i += 1

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
func8_a(
    [0, 4, 5, 1, 0, 1, 0, 0, 9]
    )
print("\n\n")
