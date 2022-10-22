def kökal(x):
    return int(x**0.5)


print(max(list(map(kökal,[4,1,9,16,64,36,49,25,81,100]))))
print(min(list(map(kökal,[4,1,9,16,64,36,49,25,81,100]))))
print(len(list(map(kökal,[4,1,9,16,64,36,49,25,81,100]))))
print(sum(list(map(kökal,[4,1,9,16,64,36,49,25,81,100]))))
print((list(map(kökal,[4,1,9,16,64,36,49,25,81,100]))))