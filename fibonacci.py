import time


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2 - time1) * 1000.0)
        return ret
    return wrap


def fib_recursion(x):
    if x < 0:
        return 0
    elif x == 0 or x == 1:
        return x
    else:
        return fib_recursion(x - 1) + fib_recursion(x - 2)


@timing
def print_fib_recursion(x):
    l = list()
    for i in range(1, x):
        l.append(fib_recursion(i))
    print(l)
print('')




def fib_yield(x):
    num_current = 0
    num_next = 1
    for i in range(1, x):
        num_tmp = num_current
        num_current = num_next
        num_next += num_tmp
        yield num_current


@timing
def print_fib_yield(x):
    for i in fib_yield(x):
        print('%d, ' % i),
    print('')


print_fib_recursion(30)
print_fib_yield(5000)
