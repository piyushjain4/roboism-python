def duplicate_no(array):
    array.sort()
    for i in range(len(array) -1):
        if array[i] == array[i+1]:
            print(array[i])
    


arr = duplicate_no([1,5,7,3,9,4,5,2,8,6])
print(arr)