def sequence(list,order):
    if order=="asc":
        lis =list.sort()
    elif order =="desc":
        lis = list.sort(reverse = True)
    else:
        lis = list
    return list
