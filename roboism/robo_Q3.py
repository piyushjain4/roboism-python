def calculate(a,arith_op,b):
    if arith_op == "+":
        result = a +b
    elif arith_op =="-":
        result = a-b
    elif arith_op == "/":
        result = a/b
    else:
        result = a*b
    return result
