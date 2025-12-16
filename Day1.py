import numpy as np

angle = 50
password = 0
rotations = np.loadtxt('rotations.txt', dtype=str)

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
        angle -= amount
    elif direction == "R":
        angle += amount

    while angle > 99:
            angle -= 100
            password += 1 # part two

    while angle < 0:
            angle += 100
            password += 1 # part two

    if angle == 0:
        password += 1

print(password)
