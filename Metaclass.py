def choose_class(name):
   if name == 'foo':
     class Foo(object):
           pass
     return Foo # return the class, not an instance
   else:
    class Bar(object):
     pass
    return Bar
MyClass = choose_class('foo')
print(MyClass) # the function returns a class, not an instance

print(MyClass()) # you can create an object from this class
