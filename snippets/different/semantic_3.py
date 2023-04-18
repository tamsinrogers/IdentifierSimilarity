def function(a, param):
    lst = []
    for element in a:
        for y in element:
            boolean = False
            if y in param:
                boolean = True
            if element in param:
                boolean = False
            if boolean is True:
                lst.append(y)
    return lst


a = ["string", "forget", "about",
     "i got strings", "who is that"]
param = "strings are what i got strings are what i need"
