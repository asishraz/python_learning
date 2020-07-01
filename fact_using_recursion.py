''' finding a factorial of a number using recursion'
'''

def fact(num):
    if num == 0:
        return 1
    return num * fact(num-1)


num = int(input("enter the number: "))
print(fact(num))