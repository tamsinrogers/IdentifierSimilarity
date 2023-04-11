def function(points, func):

    err = 0

    for xy_pair in points:
        y_approx = func(xy_pair[0])
        err += (xy_pair[1] - y_approx)**2

    return err/len(points)


points = [(0, 0), (1, 1/2), (3, 4.5)]


def f(x): return 0.5*x**2


print(function(points, f))
