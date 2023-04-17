def function(input):
    # sort the list in ascending order
    input = sorted(input, reverse=False)
    length = len(input)
    lst = []
    t = []
    for index in range(length):
        if input[index] % 2 == 0:
            lst.append(input[index])
        else:
            t.insert(0, input[index])
    return lst, t
