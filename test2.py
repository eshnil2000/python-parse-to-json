import ast
import astor

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

g=add(4,5)
h=sub(5,4)

add(4,5)
sub(5,4)

print(g)
print(h)
