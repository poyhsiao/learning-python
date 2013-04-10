for k, v in enumerate(['tic', 'tac', 'toe']):
    print k, v
''' will return
0 tic
1 tac
2 toe
it's just look like return the key/value structure
'''

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print 'What is your {0}? It is {1}.' . format(q, a)
''' will return
What is your name? It is lancelot.
What is your quest? It is the holy grail.
What is your favorite color? It is blue.
this is the way that indicate something.
1. with 'zip' to combine/pair the list together
2. use {0} and {1} as the the format output
3. with both 2 list, use zip will joint both as a dictionary format
'''
    
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.iteritems():
    print k, ':', v
''' will return
gallahad : the pure
robin : the brave
this is quite different in javascript that if wanna return the dictionary pair key/value data,
we have to use iteritems(). or the error will be occured
'''

words = ['cat', 'window', 'defenestrate', 'book', 'looosop']
for w in words[:]:  # this will slice each entire list
    if len(w) > 6:
        words.insert(0, w)
        
print words
''' will return
['looosop', 'defenestrate', 'cat', 'window', 'defenestrate', 'book', 'looosop']
since we'd like to check if the length of each word in the list is larger than 6 chars,
the split way is still need to aware
'''