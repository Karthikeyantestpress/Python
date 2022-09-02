def yeilding():
    yield 5
    yield 6
    yield 7


# Reference =yeilding()

# print(next(Reference))
# print(next(Reference))
# print(next(Reference))

print(next(yeilding()))
print(next(yeilding()))
print(next(yeilding()))

for i in yeilding():
    print(i)

