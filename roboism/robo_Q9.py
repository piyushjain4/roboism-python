def sort(string):
    lst = list(string)
    lst.sort()
    stri =""
    for i in range(len(string)):
        stri += lst[i]

    return stri 
