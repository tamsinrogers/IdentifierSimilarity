def function(str_list):
    short_string = False
    small_string = False
    for little_string in str_list:
        if len(little_string) < 5:
            short_string = True
        else:
            if len(little_string) < 10:
                small_string = True
        if short_string:
            print(little_string[0])
        elif small_string:
            print(short_string)
        else:
            print(little_string[1])
        short_string = False
        small_string = False
