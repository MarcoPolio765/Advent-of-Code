import numpy as np

angle = 50
password = 0
rotations = np.loadtxt('rotations.txt', dtype=str)
print(rotations)

for line in rotations:
    direction = ""
    amount = ""
    for char in line:
        if char.isalpha():
            direction += char
        elif char.isdigit():
            amount += char
    amount = int(amount)

    if direction == "L":
        for i in range(abs(amount)):
            angle -= 1
            if angle % 100 == 0:
                password += 1
    elif direction == "R":
        for i in range(abs(amount)):
            angle += 1
            if angle % 100 == 0:
                password += 1
print(password)
