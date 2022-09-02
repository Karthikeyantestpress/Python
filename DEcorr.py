def sqrt(exponent):
    def another(base):
        return pow(base,exponent)
    return another

Check=sqrt(2)
print(Check(3))
print(Check(4))
