'''
Created on 2013/4/10

@author: kimhsiao

Title: Handling exceptions cont.
'''

#===============================================================================
# Raising Exceptions
#===============================================================================

# raise NameError('HiThere')
''' will return
Traceback (most recent call last):
  File "/Errors-and-Exceptions/handling_exceptions2.py", line 13, in <module>
    raise NameError('HiThere')
NameError: HiThere

This is the basic way to raise a exception
'''

#===============================================================================
# User-defined Exceptions
#===============================================================================

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2 * 2)
except MyError as e:
    print 'My exception occured, value:', e.value

# raise MyError('oops!')

''' will return
My exception occured, value: 4
Traceback (most recent call last):
  File "/learning-python/Errors-and-Exceptions/handling_exceptions2.py", line 38, in <module>
    raise MyError('oops!')
__main__.MyError: 'oops!'

here are some idea need to be awared:
1. the Class part do not need to afread right now, will have some discussion later.
2. the exceptions also can be defined and assigned by user ourselves including its format, input/output value, and even the timing to raise.
3. if we just raise an exception without any try/except, the program will be suspended right away once the exception raise.
'''

try:
    raise KeyboardInterrupt
except:  # add these two lines for keep running this program
    pass
finally:
    print 'Goodbye world'


''' will show
Goodbye world

"finally" is very the same as the other language which always runs the statement no matter it's the exception occured or runs normally.
'''

class Error(Exception):
    '''Base class for exceptions in this module. '''
    pass  # do not need to do anything if such exception occured

class InputError(Error):
    ''' Exception raised for errors in the input.

    Attributes:
        expr -- input expression in which the error occured
        msg --- explantion of the error
    '''
    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg

class TransitionError(Error):
    ''' Raised when an operation attempts a state transitition that's not
    allowed.

    Attributes:
        prev -- state at beginning of transition
        next -- attempted new state
        msg -- explanation of why the specific transition is not allowed
    '''

    def __init__(self, prev, next, msg):
        self.prev = prev
        self.next = next
        self.msg = msg

'''
    Most exceptions are defined with names that end in "Error", similar to the naming of the standard exceptions.

    Many standard modules define their own exceptions to report errors that may occur in functions they define. More information on
    classes is presented later in Classes
'''

#===============================================================================
# Defining Clean-up Actions
#===============================================================================

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print "division by zero!"
    except:
        pass
    else:
        print "result is", result
    finally:
        print "executing finnaly clause"

divide(2, 1)
''' will show
result is 2
executing finnaly clause
'''

divide(2, 0)
''' will show
division by zero!
executing finnaly clause
'''

divide("2", "1")
''' will show
executing finnaly clause
Traceback (most recent call last):
  File "/learning-python/Errors-and-Exceptions/handling_exceptions2.py", line 130, in <module>
    divide("2", "1")
  File "//learning-python/Errors-and-Exceptions/handling_exceptions2.py", line 110, in divide
    result = x / y
TypeError: unsupported operand type(s) for /: 'str' and 'str'

some points that need to be awared:
1. "finially" will execute before the other exception raising
2. if some other exception occurs without pre-defined handle process, the exception will still interrupt
current program
'''

#===============================================================================
#  PRedefined Clean-up Actions
#===============================================================================

for line in open('handling_exceptions.py'):
    print line

with open('handling_exceptions.py') as f:
    for line in f:
        print line
