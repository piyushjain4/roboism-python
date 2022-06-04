def duplicate_no(array):
    array.sort()
    for i in range(len(array) -1):
        if array[i] == array[i+1]:
            print(array[i])
