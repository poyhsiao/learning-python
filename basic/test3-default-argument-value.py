def ask_ok(prompt, retries=4, complaint='Yes or not, Please!'):
    '''it\'s a test that try default argument value like php and some language defined'''
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        elif ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint
        
tryo = ask_ok('try out!')
tryo