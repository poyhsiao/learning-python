'''
Created on 2013/4/3

@author: kimhsiao

Title:Fancier output formatting

Except for print, there are many ways to change the output format.
At least, you may use write() to replace print
'''

s = 'Hello world.'
print str(s)  # this will show "Hello world."

print repr(s)  # this will show "'Hello world.'"

print str(1.0 / 7.0)  # this will show "0.142857142857"

print repr(1.0 / 7.0)  # this will show "0.14285714285714285"

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print s  # will show "The value of x is 32.5, and y is 40000..."
'''
generally, to print out the string is as the same way as javascript, quite
different from php, use "+" to add string
'''

print 'The value of x is', repr(x), ', and y is', repr(y), '...'
# this will show "The value of x is 32.5 , and y is 40000 ..."
e = 'The value of x is', repr(x), ', and y is', repr(y), '...'
print e
# this will show "('The value of x is', '32.5', ', and y is', '40000', '...')"

hello = 'hello, world\n'
hellos = repr(hello)
print hello  # this will show "hello, world" with a new blank line above

print hellos  # this will show "'hello, world\n'" including slash and single-quote

v = repr((x, y, ('spam', 'eggs')))
print v  # this will show "(32.5, 40000, ('spam', 'eggs'))"
