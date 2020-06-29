'''


scope in python

You can see the scope of variable 'a' is inside the function something. 


a = 10 #global variable

def something():
    a = 15 #local variable
    b = 23 #local variable
    print("the value of 'a' inside this function is: ", a) #preference always given to the local variable

something()

print("the value of 'a' outside the function is: ", b)


To use the global variable inside the function, we just need to pass 'global' keyword before the variable

a = 10
def something():
    #a = 15
    #to change the value of a, we need to pass the keyword global and the variable name 
    global a
    #then we can write the above statement
    a = 15
    print("the value of 'a' inside this function is: ", a) #here 'a' is global variable

something()
print("value of 'a' outside the function: ", a)

*************************************************************************************\


we can't have local and gloabl variable inside a function, to achieve this we have a function called 'globals()' , we can access the global variable address

'''
a = 20
print(id(a))


def something():
    a = 10
    x = globals()['a']
    #globals() will access all the global variable, and we need to specify which variable we need to fetch.
    print(id(x))
    print("inside the function ,the value of a is: ", a)
    #to change the global variable, without affecting the local variable
    globals()['a'] = 33 #now the value of the global variable will get change

something()

print("the value of 'a' outside the function is: ", a)