def function(input):
    l = len(input)
    index = 0
    b = False
    boolean = False
    x = True
    y = False
    while index < l:
        if input[index] != 0 and x is True:
            boolean = True
        elif input[index] == 0 and x is True:
            print(input[index])
        elif input[index] != 0 and b is True:
            print(input[index])
        elif input[index] == 0 and b is True:
            y = True

        if y:
            x = True
            b = False
            boolean = False
            y = False
        if boolean:
            b = True
            x = False
            boolean = False
            y = False

        index += 1


input = [0, 4, 5, 1, 0, 1, 0, 0, 9]
