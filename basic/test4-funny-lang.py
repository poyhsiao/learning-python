i = 5

def f(arg=i):
    '''it\'s really funny '''
    print arg*arg
    
i = 6
o = f
o()
''' no matter what i change to, the result should be 5*5 = 25 '''