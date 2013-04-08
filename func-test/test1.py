def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, that we're all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40
    ''' it's special way for python that can create duplicate symble'''
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ':', keywords[kw]
        
res = cheeseshop("Limbuger",
                 "It's very runny, sir.",
                 "It's very, VERY runny, sir.",
                 shopkeeper='Michael Palin',
                 client="John Cleese",
                 sketch="Cheese Shop Sketch")
