string1, string2, string3, string4, string5, string6 = '', 'Troneioad', 'Hammer Dance', 'DascTs', ' adf', 'asdfei '
non_null = string1 or string2 or string3 or string4 or string5 or string6
print non_null
''' will return
Troneioad
no matter what exists on each variable, the result will return the first one catch the value is not null
'''

''' Here are some example too when compare these data which ones are bigger than the others
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
'''