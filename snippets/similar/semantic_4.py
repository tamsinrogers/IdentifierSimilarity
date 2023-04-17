def function(input):
    l = len(input)
    index = 0
    start = False
    begin = False
    stop = True
    end = False
    while index < l:
        if input[index] != 0 and stop == True:
            begin = True
        elif input[index] == 0 and stop == True:
            print(input[index])
        elif input[index] != 0 and start == True:
            print(input[index])
        elif input[index] == 0 and start == True:
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

        index += 1
