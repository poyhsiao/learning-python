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
finally:
    print 'Goodbye world'
