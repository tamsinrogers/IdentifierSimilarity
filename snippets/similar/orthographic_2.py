def function(lst1):
    # sort the list in ascending order
    lst1 = sorted(lst1, reverse=False)
    l = len(lst1)
    lst2 = []
    lst3 = []
    for i in range(l):
        if lst1[i] % 2 == 0:
            lst2.append(lst1[i])
        else:
            lst3.insert(0, lst1[i])
    return lst2, lst3
