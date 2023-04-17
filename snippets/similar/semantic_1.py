def function(input_list, input_array):
    i = 0
    while i < len(input_list):
        print(i)
        if type(input_list[i]) == str:
            input_array.append(input_list[i])
            input_list.remove(input_list[i])
        elif type(input_list[i]) == float:
            input_array.append("0")
            input_list.remove(input_list[i])
        else:
            i += 1
    j = 0
    while j < len(input_array):
        if type(input_array[j]) == int:
            input_list.append(input_array[j])
            input_array.remove(input_array[j])
        elif type(input_array[j]) == float:
            input_list.append(0)
            input_array.remove(input_array[j])
        else:
            j += 1
    
    return input_list, input_array
