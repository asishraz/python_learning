

''' factorail = 5! = 5 *4 * 3 * 2 * 1

'''

def fact(a):
    mult = 1
    while a > 0:
        mult = mult * a
        a = a-1
    return mult


num = int(input("enter the number: "))
var = fact(num)
print(var)