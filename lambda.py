'''anonymous function also referred as lambda
'''

num = int(input("enter the number: "))

#lambda expressio for square of a number
sq = lambda x: x * x
print(sq(num))


#lambda expression for adding and subtracting two numbers
a = int(input("enter the number:"))
b = int(input("enter the number:"))

add = lambda a,b : a + b
print(add(a,b))
sub = lambda a,b : a - b
print(sub(a,b))
