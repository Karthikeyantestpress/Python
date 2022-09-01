def Even_eenerator():
     n=0

     n+=2
     yield n

     n+=2
     yield n

     n+=2
     yield n

Numbers = Even_eenerator()
print(next(Numbers))
print(next(Numbers))
print(next(Numbers))
