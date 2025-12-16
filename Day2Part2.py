import numpy as np

ranges = np.loadtxt('ranges.txt', delimiter=",", dtype=str)
invalids = []

for r in ranges:
    start, end = map(int, r.split('-'))
    for num in range(start, end + 1):
        str_num = str(num)
        max_reps = len(str_num)
        for rep in range(2, max_reps + 1):
            if len(str_num) % rep  != 0:
                continue
            seqlength = len(str_num) / rep
            seqs = [str_num[int(i*seqlength):int((i+1)*seqlength)] for i in range(rep)]
            if all(seq == seqs[0] for seq in seqs):
                invalids.append(num)
                break
print(np.sum(invalids))