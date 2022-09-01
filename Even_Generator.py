def Even_eenerator(max):
     n=2

     while (n<+max):
       yield n
       n+= 2
       
       

Numbers = Even_eenerator(100)
print(next(Numbers))
print(next(Numbers))
print(next(Numbers))
print(next(Numbers))
print(next(Numbers))
print(next(Numbers))
print(next(Numbers))