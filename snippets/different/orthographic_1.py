def function(input):
    string = ""
    for u in input:
        if u.isalpha():
            # get ascii value of b
            x = ord(u)
            x -= 32
            # convert ascii number to char
            l = chr(x)
            string += l
        else:
            string += u

    return string

input = "in 2 years, i will get three new pets!"
