a = "hello"
b = "hello"
print(id(a))
print(id(b))
c = b.upper()
print(c)
print(id(a))
print(id(b))
print(id(c))

print (a is b)


c = 1
d = 1
print(id(c))
print(id(d))
print(c is d)