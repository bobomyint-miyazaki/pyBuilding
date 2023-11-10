# import timeit
# print(timeit.timeit('"-".join(str(n) for n in range(10000))', number=10000))

#%load_ext Cython

def cy_fib(n):
    a, b = 0.0, 1.0
    for i in range(n):
        a, b = a+b, a
        return a