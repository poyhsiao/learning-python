a = [66.25, 333, 333, 1, 1234.5]
print a.count(333), a.count(62), a.count(66.25), a.count('x')

a.insert(2, -1)
''' insert "-1" on the 2nd position of the list '''
a.append(333)
print a

print a.index(333)

a.remove(333)
print a

a.reverse()
print a

a.sort()
print a

a.reverse()
print a