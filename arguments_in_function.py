#we will be learning different type of arguments in function

'''
firstly, we have two arguments, formal and actual arguments in function
def func(a,b) =>Here a,b are formal arguments, where we are defining it
func(5,6) => this is actual arguments, as the name suggests, we are passing actual arguments as 5 and 6


Actual arguments itself has four types:
1. position, 2. keyword , 3.default, 4.variable length

1. position arguments
def add_name(name,age):
    print(name)
    print(age)

add_name('GareebCODER',26)

Here in the formal arguments, we are passing first the name and then the age. So, when are calling the function, we have to specify the same order.
Means, add_name('anyname',age) and not add_name(age,'name')
Position are very important here

we can try here:

def add_name(name,age):
    print(name)
    print(age+5)

add_name('asish',25) # => It will print asish 30
add_name(26,'asish') # => this will throw an error


2.keyword
in case you don't know the order and want to print the output of the function, try to give keyword to the arguments when you are calling that function
Take the above code only

def add_name(name,age):
    print(name)
    print(age+5)

add_name(age=26,name='gareeb')

We are giving the keyword to the arguments 

3. default
in case you haven't passed any argument in the function, the default will take care of that argument and assign the default value to it, 
even if you haven't passed any value.

def add_name(name,age=18):
    print(name)
    print(age+2)

add_name('gareeb')

This default argument

4. variable length
In case the number of arguments are not fixed. Lets say, we want to add multiple numbers. Here we don't know how many numbers we have to pass to the function.
In that case, we can define any one argument as variable lenght, to accept multiple values


def add_num(a, *b):  #=> here 'b' is having variable length argument 
    c = a + b
    print(c)


add_num(4,5,6,7)

in the above code, it will throw an error as we can't add INT and TUPLE together.  Because  a is INT and b is TUPLE.
you can print the above value for your reference. 


def add_num(a, *b):
    print(a)  #=> 4
    print(b)  # => b =(5,6,7)

add_num(4,5,6,7)

for solving the above code, we can do like this:
'''
def add_num(a,*b):
    c = a
    for i in b:
        c += i

    print(c)

add_num(4,5,6,7)








