def f(x):
    return x % 2 != 0 and x % 3 != 0 and x % 5 != 0

print filter(f, range(2, 30))
''' filter will only return true items as a list '''

def cube(x):
    return x*x*x

def dash(x):
    return '-' * x

seq = range(8)
def add(x, y):
    return x + y

print map(cube, range(1, 11))
''' map will calculate the result of the function and return as a list '''

print map(dash, range(1, 11))
''' of course the symbol is also work fine '''

print map(add, seq, seq)
''' if there are more than one args required for the function, just assign the
args as maps parameters of map function

if without the parameters match the given function, the exception will raise
'''

def add_two(x, y):
    return x + y

print reduce(add_two, range(1, 11))
''' reduce function is a funny function the action is opposite of its name. in fact
reduce will run the given function recursively until all the given parameter completed.
on the other hand, the exception will be raise if no parameter is given.
''' 
