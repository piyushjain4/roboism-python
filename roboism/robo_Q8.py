def sum_of_int(string):
    y = 0
    for i in string:
        if i.isdigit() == True:
            x = int(i)
            y+=x
    return y

p =sum_of_int( "h20 15 wa73r")
print(p)




