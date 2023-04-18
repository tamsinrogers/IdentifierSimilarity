def function(param, string):
    lst = []
    for character in param:
        for letter in character:
            add = False
            if letter in string:
                add = True
            if character in string:
                add = False
            if add is True:
                lst.append(letter)
    return lst


a = ["string", "forget", "about",
     "i got strings", "who is that"]
param = "strings are what i got strings are what i need"
