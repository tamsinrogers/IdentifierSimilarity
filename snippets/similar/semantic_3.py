def function(a, string):
    lst = []
    for char in a:
        for letter in char:
            add = False
            if letter in string:
                add = True
            if char in string:
                add = False
            if add == True:
                lst.append(letter)
    return lst
