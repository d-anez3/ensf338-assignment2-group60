#testing code for the two functions

import timeit
import matplotlib.pyplot as plt


def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)


def fib(n, memo_dict = {}):
    if n in memo_dict:
        return memo_dict[n]
    if n ==0 or n ==1:
        return n
    memo_dict[n] = fib(n-1, memo_dict) + fib(n-2, memo_dict)
    return memo_dict[n]

def time_func(func, n):
    return timeit.timeit(lambda: func(n), number=1)

def fib_seq(n):
    return [func(i) for i in range(n+1)]

def plot_time_complexity(func):
    times = [time_func(func, i) for i in range(36)]
    plt.plot(range(36), times, label=func.__name__)
    plt.xlabel("n")
    plt.ylabel("Time (seconds)")
    plt.title("Time complexity of the Fibonacci sequence")
    plt.legend()


plot_time_complexity(func)
plot_time_complexity(fib)
plt.show()
