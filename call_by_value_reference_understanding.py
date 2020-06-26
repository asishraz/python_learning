#difference between call by value and call by reference

'''
in python there is no concept of call by value and call by reference. you will understand with the below code/'''

def new_func(x):
    print("before assiging something, the value of x is: ", x)
    print("before assigning, id of x is: ", id(x))
    #till this point x and global_var will points towards the same memory location
    #and the moment, we assign some value to x, the memory location will change
    #lets check the memory  location for both the varialbles before and after the operation
    x = 10
    print(x)
    print("after the value got assigned: ",id(x))
    #we can see that the memory location got changed for x



global_var = 100
print("id of global var: ", id(global_var))
new_func(global_var)