def Fibo():
    n1=0
    n2=1
    while True:
       yield n1
       n1,n2=n2,n1+n2

Output = Fibo()
   
print(next(Output))
print(next(Output))
print(next(Output))
print(next(Output))
print(next(Output))
