'''
dir() is the build-in function
which is used to find out which names a module defines.
it returns a sorted list of strings.

Created on 2013/4/8

@author: kim.hsiao
'''

import fibo, sys

print dir(fibo)
print fibo.__file__  # this will show the file path
print fibo.__doc__
 #==============================================================================
 # this will show the comments wrapped with ''' or """
 #==============================================================================


print dir(sys)
