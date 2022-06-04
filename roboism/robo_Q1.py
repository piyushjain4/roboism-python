def sequence(list,order):
    if order=="asc":
        lis =list.sort()
    elif order =="desc":
        lis = list.sort(reverse = True)
    else:
        lis = list
    return list
    
sol = sequence([1,2,4,3,7],"asc")
print(sol)