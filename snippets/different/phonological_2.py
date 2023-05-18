def function(points, func):

    err = 0

    for pt in points:
        y_approx = func(pt[0])
        err += (pt[1] - y_approx)**2

    return err/len(points)


def func(x): return 2*x


points = [(0, 1),
          (1, 1),
          (2, 3),
          (3, 6),
          (4, 10)]
