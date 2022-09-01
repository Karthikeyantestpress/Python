def inc(x):
    return x+1+x

def onemore(fun,x):
    result= fun(x)
    return result 

print(onemore(inc,3))
