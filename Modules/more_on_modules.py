'''
Created on 2013/4/8

@author: kim.hsiao
'''
# try to access the module more

# from fibo import fib, fib2 # import both fib and fib2 modules
# print fib(500)

from fibo import *  # it's another way to import all the modules
print fib(500)


'''
1. it looks good that if we only use fib() without fib2(), eclipse will show a
breakpint at the import line. let you know "unused in wild import: fib2".

2. with "from xxx import yyy", we don't have to write the fibo.fib() just use the fib()
will fine.

3. for efficiency reasons, each module is only imported once per interpreter session.
Therefore, if you change your modules, you must restart the interpreter - or, if
it's just one module you want to test interactively, use "reload()", e.g.
reload(modulename)
'''
