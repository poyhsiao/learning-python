'''
Created on 2013/4/4

@author: kimhsiao

Title: Reading and writing files
'''

'''
open() returns a file object, and is most commonly used with two arguments:
open(filename, mode)

which is very similar to the other language to access file
'''

f = open('sampler.txt', 'w')
print f  # f is an object
# will return "<open file 'output_format2.py', mode 'w' at 0x7f6c455dded0>"
# this will write an empty file
f.close()

'''
Same as the other linux program like PHP, the flag can be "r", "r+", "w",
or in Windows can be "rb", "wb", even "r+b" as read/write an binary file.
Only one thing need to be awared is "r+" or "r+b", which can read and write
the file at the same time.
'''

f = open('sample.txt', 'r')
print f.read()
# this will read whole file

print f.readline()
# this will only read one line of the file
print f.readline()
f.close()

f = open('sample.txt', 'r')
print f.readlines()
# this will read all the lines of the file and return as a list
f.close()
