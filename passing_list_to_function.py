'''
take a list and input the element from the user and count the number of even and odd in that list


lst = [int(input()) for x in range(10)]

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even +=1
        else:
            odd += 1
    return even, odd

even, odd = count(lst)

print("Even {} and Odd {} ".format(even,odd))

'''


'''assignment :- take 10 names from the user and display the number of names whose length is more than five'''

user_name = [input() for x in range(5)]

def count_names(user_name):
    length_plus_5 = 0
    for i in user_name:
        if len(i) > 5:
            print(i)
            length_plus_5 += 1
    return length_plus_5

names = count_names(user_name)

print("Names length more than five {}".format(names))

