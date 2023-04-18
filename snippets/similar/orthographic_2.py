def function(input):
    # sort the list in ascending order
    input = sorted(input, reverse=False)
    length = len(input)
    q = []
    d = []
    for index in range(length):
        if input[index] % 2 == 0:
            q.append(input[index])
        else:
            d.insert(0, input[index])
    return q, d


input = [6, 8, 35, 17, 0, 9, 45]
