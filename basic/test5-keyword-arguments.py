def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    '''it's a keyword arguments of the from "kwarg=value" as an instance'''
    print "-- This parrot woldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"
    
#parrot(1000)
''' 1 positional argument'''
#parrot(voltage=1000)
''' 1 keyword argument '''
#parrot(voltage=1000, action='VOOOOM')
''' 2 keyword arguments '''
#parrot(action='VOOOOOM', voltage=100000)
''' 2 keyword arguments without in serial '''
#parrot('a million', 'bereft of life', 'jump')
''' 3 positional arguments '''
#parrot('a thousand', state='pushing up the daisies')
''' 1 positional argument, 1 keyword argument '''

''' the following methods are leaded to error '''
#parrot()
''' without any argument'''
#parrot(voltage=50, 'dead')
''' once the first argument used as keyword one, the other should set as keyword arguments as well ''' 
#parrot(110, voltage=220)
''' duplicate value for same argument '''
#parrot(actor='John Cleese')
''' no such keyword exists in the function '''