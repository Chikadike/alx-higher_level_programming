#!/usr/bin/python3
# importing function
# defined in add_0.py

from add_0 import add

# calling function

a = 1
b = 2
add(a, b)
sum = a + b
print(f"{a} + {b} = {sum}".format(a, b, sum))
