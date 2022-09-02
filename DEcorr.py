def sum (a,b):
  print(a+b)

def Work(func):
    def inner (x,y):
        if x>0 or y>0:
            x=x+1
            y=y+1
        return func(x,y)
    return inner

Calling =Work(sum)
Calling(2,3)    