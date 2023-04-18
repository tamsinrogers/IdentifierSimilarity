def function(input):
    string = ""
    for b in input:
        if b.isalpha():
            # get ascii value of b
            x = ord(b)
            x -= 32
            # convert ascii number to char
            d = chr(x)
            string += d
        else:
            string += b

    return string


input = "in 2 years, i will get three new pets!"
