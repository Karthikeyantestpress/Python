class Jarvis():

    def __init__(self, data):
        self.data = data

    def train_sum(self, newX):
        self.data = [x + newX for x in self.data]
        
        return self # This is what allows chaining
    
    def train_prod(self, beta):
        self.data = [x*beta for x in self.data]
        return self


# initialize the object:
jv = Jarvis([1,2,3,4])

# use its methods 
jv.train_sum(4)
jv.train_prod(10)
print(jv.data)


# the same thing with method chaining:
jv = Jarvis([1,2,3,4])

print(jv.train_sum().train_prod(10).data)