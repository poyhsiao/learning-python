'''
Created on 2013/4/8

@author: kim.hsiao
'''

# it's a file for fibo testing

import fibo  # import fibo which name is fibo.py

print fibo.fib(1000)  # import from fibo.py and execute the module within

print fibo.fib2(100)  # import from fibo.py and execute its module within

print fibo.__name__  # show the module name
