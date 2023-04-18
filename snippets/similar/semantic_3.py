def function(param, string):
    lst = []
    for character in param:
        for letter in character:
            add = False
            if letter in string:
                add = True
            if character in string:
                add = False
            if add == True:
                lst.append(letter)
    return lst
