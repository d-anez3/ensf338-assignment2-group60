#better fibonacci sequence thats more efficent

def fib(n, memo_dict = {}):
    if n in memo_dict:
        return memo_dict[n]
    if n ==0 or n ==1:
        return n
    memo_dict[n] = fib(n-1, memo_dict) + fib(n-2, memo_dict)
    return memo_dict[n]
