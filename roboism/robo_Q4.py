def doubled_str(string):
    new_str =""
    for i in range( len(string)):
        new_str += string[i]*2
    return new_str

stri = doubled_str("now")
print(stri)

stri2 = doubled_str("123!")
print(stri2)



