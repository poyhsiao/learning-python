squares = []
for x in range(10):
    squares.append(x**2)
    
print squares

squares2 = [x**2 for x in range(10)]

print squares2
''' the result is the same as the description above '''

squares3 = map(lambda x: x**2, range(10))

print squares3
''' these three statements are the same '''

pair1 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

print pair1
''' there are some idea inside this statement:
1. the list also can be pair numbers/items as its component
2. for-loop statement also can be written as the style above
'''

pair2 = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            pair2.append((x, y))
            
print pair2
''' this is the normal way to implement the code above, but looks tedisome'''

listr = [range(x, x**2) for x in range(1, 6) if x > 0]
print listr
''' also some operation can be contain within the list '''

from math import pi

pii = [str(round(pi, i)) for i in range(1, 10)]
print pii

matrix = [
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          ]

print [[row[i] for row in matrix] for i in range(4)]
''' this command will split the matrix from horizontal to vertical.
however, if the split size is smaller than the number of iterable, some information
will be lost. Also, if the split size is larger than the number of iterable, the exception
also will be raised
'''

