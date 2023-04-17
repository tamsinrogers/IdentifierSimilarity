def function(input_list, string):
    output_list = []
    for char in input_list:
        for letter in char:
            add = False
            if letter in string:
                add = True
            if char in string:
                add = False
            if add:
                output_list.append(letter)
    return output_list
