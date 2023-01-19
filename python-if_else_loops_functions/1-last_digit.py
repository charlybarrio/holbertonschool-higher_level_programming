#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if (number < 0):
    number * -1
    lastdigit = number % 10
    lastdigit *= -1
else:
    lastdigit = number % 10

print(f"Last digit of {number} is {lastdigit}", end=" ")

if (lastdigit > 5):
    print(f"and is greater than 5")
elif (lastdigit == 0):
    print(f"and is 0")
else:
    print(f"and is less than 6 and not 0")
