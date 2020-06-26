''' 
class = blueprint  and object = properties
class is the combination of methods(functions) and variables 
functions in OOPS called methods

a class class have many objects

everything in python is object
in order to create your own class, we use the keyword 'class'



class Computer:
    def config(self):
        print("something something")

com1 = Computer() #com1 is the object for the class Computer

print(type(com1))
x = 9
y = 'str'
print(type(x))
print(type(y))


now we will call the object of the class and in order to call the config method inside the class, we need to mention the object(com1) by the time of calling
'''

class Computer:
    def config(self):
        print("something something")

com1 = Computer()

Computer.config(com1) #this config will go inside the class as function which has the argument 'com1' and will print the next line  
#and another way of calling the method 'config':

com1.config()





