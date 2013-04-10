ori = {'primer': {'items': [], 'number': 0}, 'val': {'items': [], 'number': 0}}

for n in range(2, 200):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            ori['val']['number'] += 1
            ori['val']['items'] += [n]
            break
        else:
            ori['primer']['number'] += 1
            ori['primer']['items'] += [n]
            continue
            #print n, 'is a prime number'
            
print ori['val']