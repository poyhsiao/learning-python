'''
Created on 2013/4/9

@author: kim.hsiao

Title: Handling Exceptions

Description: The idea is very similar to the other language, some call it as try-catch or try-catch-final handling.
'''

while True:
    try:
        x = int(raw_input('Please enter a number:'))
        break
    except ValueError:
        print "Ooops! That was not valid number. Try again..."

'''
normally, the except type/name based on the exception output
'''

import sys

try:
    f = open('myfile.txt', 'r')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error ({0}): {1}".format(e.errno, e.strerror)
    print e
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexcepted error:", sys.exc_info()[0]
    raise

'''
Here are some points need to aware
1. may use "except xxx as y:": xxx is the exception type, and y is the short name/error message of the exception.
2. here is an except statement without any type, means the other exceptions are not listed above will execute following program.
'''

# for arg in sys.argv[1:]:
x = str(raw_input('plz choose your file'))
try:
    f = open(x, 'r')
except IOError:
    print 'cannot open', x
else:
    print x, 'has', len(f.readlines()), 'lines'
    f.close()

'''
Here are some points need to aware:
1. str() ... for raw_input is unnecessary since the raw_input always return string.
2. else ... the program will execute this part if everything is ok without any exception occurs.
I have changed the code to fulfill the console input mode
'''

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print type(inst)  # the exception instance
    print inst.args  # arguments stored in .args
    print inst  # __str__ allows args to printed directly
    x, y = inst.args
    print 'x =', x
    print 'y =', y

''' will return
<type 'exceptions.Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
Here are something need to be awared.
1. "raise xxx" will occur one user-defined exception
2. this exception has two parameters 'spam' and 'eggs' which are assigned by user predefined
'''
