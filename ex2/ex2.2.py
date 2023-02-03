import sys, json, time, matplotlib.pyplot as plt, pandas as pd, timeit, numpy as np
sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
    
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open('ex2/ex2.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
print(len(df))
print(df.iloc[9])


timings = {}

    
# for key in df.columns:
#     if np.isnan(df[key]).any():
#         continue
#     array = df[key].to_list()
#     time = timeit.timeit(lambda: func1(array, 0, len(array) - 1), number=1)
#     timings[key] = time

# x = list(timings.keys())
# y = list(timings.values())
# plt.bar(x, y)
# plt.xlabel('Array')
# plt.ylabel('Time (s)')
# plt.title('QuickSort Timing Results')
# plt.show()