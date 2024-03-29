def function(input, ker, pad=False):

    if len(ker) % 2 == 0:
        print('Kernel must have odd length!')
        return None

    data = input.copy()

    ker_pad = int((len(ker) - 1)/2)

    if pad:
        for _ in range(ker_pad):
            data.insert(0, 0)
            data.append(0)

    n_points = len(data)
    output = []
    for i in range(ker_pad, n_points - ker_pad):

        win = data[i - ker_pad: i + ker_pad + 1]
        value = 0
        for index in range(len(ker)):
            value += ker[index]*win[index]

        output.append(value)

    return output


input = [0, 1, 2, 3, 2, 1, 0]
ker = [1, 1, 1]
