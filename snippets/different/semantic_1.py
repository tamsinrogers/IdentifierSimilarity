def function(a, input):
    index = 0
    while index < len(a):
        print(index)
        if type(a[index]) == str:
            input.append(a[index])
            a.remove(a[index])
        elif type(a[index]) == float:
            input.append("0")
            a.remove(a[index])
        else:
            index += 1
    index = 0
    while index < len(input):
        if type(input[index]) == int:
            a.append(input[index])
            input.remove(input[index])
        elif type(input[index]) == float:
            a.append(0)
            input.remove(input[index])
        else:
            index += 1

    return a, input

a = [2, "three", "four", 5, 6.7, "seven", "eight", 9, "ten"]
input = ["zero", 1, "two", 4.5, 8, 16, "thirty-two", 64.0]
