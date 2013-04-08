'''
Created on 2013/4/8

@author: kim.hsiao

'''
# Fabonacci numbers module

def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a + b

def fib2(n):  # return Fibnacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result
