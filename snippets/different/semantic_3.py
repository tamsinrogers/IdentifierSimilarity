def function(a, param):
    lst = []
    for element in a:
        for y in element:
            boolean = False
            if y in param:
                boolean = True
            if element in param:
                boolean = False
            if boolean == True:
                lst.append(y)
    return lst
