def function(list, array):
    index = 0
    while index < len(list):
        print(index)
        if type(list[index]) == str:
            array.append(list[index])
            list.remove(list[index])
        elif type(list[index]) == float:
            array.append("0")
            list.remove(list[index])
        else:
            index += 1
    index = 0
    while index < len(array):
        if type(array[index]) == int:
            list.append(array[index])
            array.remove(array[index])
        elif type(array[index]) == float:
            list.append(0)
            array.remove(array[index])
        else:
            index += 1

    return list, array
