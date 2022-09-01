def Star(func):#func===printer
    def inner(args):
        print("*"*30)
        func(args)
        print("*"*30)
    return inner

def percent(func):#f
    def inner(args):
        print("%"*30)
        func(args)
        print("%"*30)
    return inner 

@Star
@percent
def printer(Message):
    print(Message)

printer("We are in Decorator")