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

#===============================================================================
# new study for file seek
#===============================================================================
f = open('workfile', 'r+')
f.write('0123456789abcdef')
f.seek(5)  # go to the 6th byte of the file
print f.read(1)  # will show "5"

f.seek(-3, 2)  # go to the 3rd byte before the end
print f.read(1)  # will show "d"

f.close()

# f.read()
'''
error message will raise since we have close the file already.
'''

with open('workfile', 'r') as f:
    read_data = f.read()
f.closed
'''
I think it's a better way to access the file, since we have wrapped all the code within the with statement.
I think it's much readable.
'''

print read_data  # will show "0123456789abcdef"
print f  # will show "<closed file 'workfile', mode 'r' at 0x025BB700>"
