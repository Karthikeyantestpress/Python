class Even:

    def __init__(self,Max):
        self.n=2
        self.Max=Max
    
    def __iter__(self):
        return self 

    def __next__(self):
      if self.n<=self.Max:
         result=self.n
         self.n +=2
      return result
    

Numbers=Even(10)
print(next(Numbers))
print(next(Numbers))
print(next(Numbers))
print(next(Numbers))
print(next(Numbers))
