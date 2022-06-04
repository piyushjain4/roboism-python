def find_elem(arr):
    elem = max(arr,key =arr.count )
    return elem


p = find_elem([1,5,1,1,2,3,4,4,7,8,1,1,9,9,9,9,9,9])
print(p)