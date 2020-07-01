'''
recursion and its limit
'''

import sys

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

count = 0
def greet():
    global count
    count += 1
    print("Hello", count)
    greet()

greet()

