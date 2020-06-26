#difference between call by value and call by reference

'''
in python there is no concept of call by value and call by reference. you will understand with the below code/'''

def new_func(x,lst):
    print("before assiging something, the value of x is: ", x)
    print("before assigning, id of x is: ", id(x))
    print("till now id of x and global_var are same: ", id(global_var), id(x))
    #till this point x and global_var will points towards the same memory location
    #and the moment, we assign some value to x, the memory location will change
    #lets check the memory  location for both the varialbles before and after the operation
    x = 10
    
    print("value of x: ",x)
    print("after the value got assigned, id of x got changed: ",id(x))
    #we can see that the memory location got changed for x
    ''' now we will check for the list '''
    print("Before assignment, id of list is: ", id(lst))
    lst[2] = 99
    print("value of lst got changed: ",lst)
    print("id of lst remain unchanged: ", id(lst))


print("THIS IS THE CONCEPT OF IMMUTABLE")


global_var = 100
lst = [30,50,70]
print("id of global var: ", id(global_var))
print("value of global_var before going to function: ", global_var)
print("value of list before going to function: ", lst)
print("id of lst before going to function: ", id(lst))
new_func(global_var,lst)