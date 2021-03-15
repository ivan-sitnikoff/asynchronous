def print_name(prefix):
    print(f'Searching prefix: {prefix}')
    try:
        while True:
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print('Closing coroutine!')

corou = print_name('Dear')
corou.__next__()
corou.send('James')
corou.send('Dear James')
corou.close()