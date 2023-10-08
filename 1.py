def decorator(func):

    def new_func():
        print(123)
        func()
        print(456)
    
    return new_func



@decorator
def t():
    print("blablabla")


t()

import time

def count_time(func):
    def new_func(some_list):
        start_time = time.time()
        func(some_list)
        end_time = time.time()
        print(end_time - start_time)
    
    return new_func

@count_time
def sorting(some_list):
    return some_list.sort()

some_list = [i for i in range(10000000, 0, -1)]

sorting(some_list)