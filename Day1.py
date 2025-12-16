import numpy as np

password = 0
angle = 50
rotations = np.loadtxt('rotations.txt', dtype=str)

for line in rotations:
    direction = ""
    amount = ""
    while i := 0 < len(line):
        if line[i].isalpha():
            direction += line[i]
        elif line[i].isdigit():
            amount += line[i]
    amount = int(amount)
    if direction == "L":
        angle -= amount
    elif direction == "R":
        angle += amount
    
    if angle % 100 ==0:
        password += 1

print(password)

