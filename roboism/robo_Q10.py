def swap(a,b):
    a = a^b
    b = a^b
    a = a^b
    return a,b

p = swap(3,10)
print(p)