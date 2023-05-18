def function(points, func):

    pare = 0

    for pair in points:
        y_approx = func(pair[0])
        pare += (pair[1] - y_approx)**2

    return pare/len(points)


def func(x): return 2*x


points = [(0, 1),
          (1, 1),
          (2, 3),
          (3, 6),
          (4, 10)]
