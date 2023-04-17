def function(input_list):
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
