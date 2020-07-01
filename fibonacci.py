'''
fibonacci sequence
0 1 1 2 3 5 8 13 21 ...


0+1 = 1 #the next number
1+1 = 2 #the next number
2+1 = 3
and so on ...

'''

'''
first assignment: taking input from the user and validate the range

def fibonacci(num):
    a = 0
    b = 1

    if num == 1:
        print(a)
    elif num > 1:
        print(a)
        print(b)

        for i in range(2,num):
            c = a + b
            print(c)
            a = b
            b = c
    else:
        print("enter the valid range from zero")
        

num = int(input("Enter the range: "))
var = fibonacci(num)
'''

''' second assignment: take the input from the user and print the series less than the input number
'''

def fibonacci(range_value,last_num):
    a = 0
    b = 1
    if range_value == 1:
        print(a)
    elif range_value > 1:
        print(a)
        print(b)
        for i in range(2,range_value):
            c = a + b
            if c < last_num:
                print(c)
                a = b
                b = c
            else:
                print("Can't print beyond the last number which is {}".format(last_num))
                break

    else:
        print("Enter non-negative number")

    

range_value = int(input("enter the range for the fibonacci series: "))
last_num = int(input("enter the number till which the fibonaaci series will print: "))
fibonacci(range_value,last_num)