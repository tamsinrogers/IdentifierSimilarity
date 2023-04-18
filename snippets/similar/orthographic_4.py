def function(param, input):
    length = len(param)
    g = 0
    q = 1e9
    var = ""
    ret = ""
    for elem in range(length):
        value = len(input[elem])
        num = 0
        for index in range(value):
            if input[elem][index] == 1:
                num += 1
        if num > g:
            var = param[elem]
            g = num
        if num < q:
            ret = param[elem]
            q = num

    return var, ret


a = ["Jerry", "George", "Newman"]
b = [
    [1, 2, 4, 3, 1, 1, 3],
    [4, 2, 1, 1, 1, 3, 1],
    [6, 2, 1, 3, 4, 3, 2]
]
