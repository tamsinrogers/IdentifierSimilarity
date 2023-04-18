def function(a):
    short_string = False
    boolean = False
    for little_string in a:
        if len(little_string) < 5:
            short_string = True
        else:
            if len(little_string) < 10:
                boolean = True
        if short_string:
            print(little_string[0])
        elif boolean:
            print(short_string)
        else:
            print(little_string[1])
        short_string = False
        boolean = False
