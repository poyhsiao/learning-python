def f(a, L=[]):
    '''it's really funny'''
    L.append(a)
    return L

print f(3)
print f(2)
print f(1)
print len(f(5))

''' the L will become a global(static) varible, it's really cool'''