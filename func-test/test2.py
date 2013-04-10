print range(3, 6)

args = [3, 6]
print range(*args)

def parrot(voltage, state='a stiff', action='voom'):
    ''' it's a test for parrot with **key input '''
    print "-- This parrot wouldn't", action,
    ''' if you wanna print something with line break, you have to add "," at the end of each print line '''
    print "if you put", voltage, "volts through it.",
    print "E's", state, "!"
    
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOOOM"}
parrot(**d)
''' make the dictionary as keyword veriables, it may very useful to get json input or export
also, no matter you wanna define the function with *arg or **key, or the opposite way to insert
arguments, all of them are flexible for programmer '''

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42) 
print f(2)
print f(3)

print parrot.__doc__