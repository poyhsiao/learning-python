tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print tel
''' will return
{'sape': 4139, 'jack': 4098, 'guido': 4127}
you may add and modify items inside dictionary as javascript do
'''

print tel['jack']
''' will return
4098
also the way to read the item just like js and list do
'''

del tel['sape']
tel['irv'] = 4127
print tel
''' will return
{'jack': 4098, 'irv': 4127, 'guido': 4127}
del is also work
'''

print tel.keys()
''' will return
['jack', 'irv', 'guido']
it's a easy way to print keys inside the dictionary as a list
'''

print 'guido' in tel
''' will return
True
also may check if the key inside the dictionary with this easy way
'''

dict = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print dict
''' will return
{'sape': 4139, 'jack': 4098, 'guido': 4127}
with dict() will convert the pair data to dictionary
'''

res = {x: x**2 for x in (2, 4, 6)}
print res
''' will return
{2: 4, 4: 16, 6: 36}
it's also a convinent way if you want to define the key/value dictionary as numeric data
'''

#print dict(sape=4139, guido=4127, jack=4098)
''' fail
it should return a dictionary as the result above, but it fail
'''