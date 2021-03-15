import multiprocessing

def print_func(continent='Asia'):
    print('The name of continent is : ', continent)
    
if __name__ == '__main__':
    names = ['Asia', 'America', 'Europe', 'Africa']
    procs = []
    
    for name in names:
        proc = multiprocessing.Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()
        
    for proc in procs:
        proc.join()