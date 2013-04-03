'''
Created on 2013/4/3

@author: kimhsiao

Title:Fancier output formatting cont.

Except for print, there are many ways to change the output format.
At least, you may use write() to replace print
'''

for x in range(1, 11):
    print repr(x).rjust(2), repr(x * x).rjust(3),
    # Note trailing comma on previous line
    print repr(x * x * x).rjust(4)

''' will return
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
'''

for x in range(1, 11):
    print '{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x)

''' will return
this will return the same format as the example above
'''

print '12'.zfill(5)  # this will show "00012"

print '-3.14'.zfill(7)  # this will show "-003.14"

print '3.14159265359'.zfill(5)  # this will show "3.14159265359"
'''
zfill() will add zero if the number is smaller than the given zfill width
'''

print 'We are the {} who say "{}!"'.format('knights', 'Ni')
# will show "We are the knights who say "Ni!""

print '{0} and {1}'.format('spam', 'eggs')
# will show "spam and eggs"

print '{1} and {0}'.format('spam', 'eggs')
# will show "eggs and spam"

print 'This {food} is {adjective}.'.format(food = 'spam', adjective = 'absolutely horrible')
# will show "This spam is absolutely horrible."

print 'The story of {0}, {1}, and {other}'.format('Bill', 'Manfred', other = 'George')
# will show "The story of Bill, Manfred, and George"

'''
format(*args, **kwargs) can accept both list and dictionary for *args and **kwargs
'''

import math
print 'The value of PI is approximately {}.'.format(math.pi)
# will show "The value of PI is approximately 3.14159265359."

print 'The value of PI is approximately {!r}.'.format(math.pi)
# will show "The value of PI is approximately 3.141592653589793."

'''
if we use {!s} is similar to str() and !r is simpilar to repr()
'''

print 'The value of PI is approximately {0:.3f}.'.format(math.pi)
# will show "The value of PI is approximately 3.142."

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# for name, phone in table.iteritems():
for name, phone in table.items():
    print '{0:10} ==> {1:10d}'.format(name, phone)
#===============================================================================
#  will show
# Dcab       ==>       7678
# Jack       ==>       4098
# Sjoerd     ==>       4127
#===============================================================================

'''
point:
1. iteritems() and items() are the same in python 2, and in python 3, will
no longer use iteritems(). The easier way is remember itmes() will be fine.

2. {0:10} means the first item like {0}, and spacing padding will be up to
10. And {1:10d} is the same as the 2nd item like {1} and :10d will be the
10 spacing padding with digit number output.
Thus, {0:10} can also be writen as {0:10s} means the output is as a string
'''

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print ('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))
# will show "Jack: 4098; Sjoerd: 4127; Dcab: 8637678"

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print ('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# will show "Jack: 4098; Sjoerd: 4127; Dcab: 8637678"

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#===============================================================================
# The following is "Old string formatting
#===============================================================================

print 'The value of PI is approximately %5.3f.' % math.pi
# will show "The value of PI is approximately 3.142."

