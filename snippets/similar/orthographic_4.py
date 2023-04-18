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
