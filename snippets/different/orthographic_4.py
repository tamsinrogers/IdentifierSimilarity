def function(a, input):
    length = len(a)
    num = 0
    integer = 1e9
    var = ""
    ret = ""
    for i in range(length):
        y = len(input[i])
        r = 0
        for index in range(y):
            if input[i][index] == 1:
                r += 1
        if r > num:
            var = a[i]
            num = r
        if r < integer:
            ret = a[i]
            integer = r

    return var, ret

a = ["Jerry", "George", "Newman"]
b = [
    [1, 2, 4, 3, 1, 1, 3],
    [4, 2, 1, 1, 1, 3, 1],
    [6, 2, 1, 3, 4, 3, 2]
]
