'''
Created on 2013/4/8

@author: kim.hsiao
'''

if __name__ == "__main__":
    from fibo import fib
    import sys
    fib(int(sys.argv[1]))

'''
1. the code in the module will be executed, just as if you import it,
but with the "__name__" set to "__main__". That means that by adding
this code at the end of your module

2. you can make the file usable as a script as well as an importable
module, because the code that parses the command line only runs if
the module is executed as the "main" file

may issue following command:
$ python fibo2.py 50
1 1 2 3 5 8 13 21 34

3. the code is also importable. but now we do not re-duplicate the same
code from fibo, otherwise this file can be also importable from other
'''
