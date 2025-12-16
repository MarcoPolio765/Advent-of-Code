import numpy as np

ranges = np.loadtxt('ranges.txt', delimiter=",", dtype=str)
invalids = []

for r in ranges:
    start, end = map(int, r.split('-'))
    for num in range(start, end + 1):
        if len(str(num)) % 2 != 0:
            continue
        str_num = str(num)
        mid = len(str_num) // 2
        left = str_num[:mid]
        right = str_num[mid:]
        if left == right:
            invalids.append(num)

print(np.sum(invalids))
