def function(input):
    l = len(input)
    index = 0
    start = False
    begin = False
    x = True
    y = False
    while index < l:
        if input[index] != 0 and x is True:
            begin = True
        elif input[index] == 0 and x is True:
            print(input[index])
        elif input[index] != 0 and start is True:
            print(input[index])
        elif input[index] == 0 and start is True:
            y = True

        if y:
            x = True
            start = False
            begin = False
            y = False
        if begin:
            start = True
            x = False
            begin = False
            y = False

        index += 1
