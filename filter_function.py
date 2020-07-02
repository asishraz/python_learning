''' use of filter function


def is_even(num):
    return num%2 == 0
numbers = [1,12,3,53,5,64,64,62,62,646,42,63246,464,634,6464,36,3464]

evens = list(filter(is_even,numbers))
print(evens)

vowels = ['a','e','i','o','u']

strings = ['a','a','s','k','j','d','f','o','a','i','w','e','u','f','k','l','p','e','i','f','j','s','d','k','l','f','j','d','s','k','l','f']
def is_vowel(alpha):
    return alpha in vowels
    

result = list(filter(is_vowel,strings))

print(result)

'''


''' use of lambda function 

numbers = [1,12,3,53,5,64,64,62,62,646,42,63246,464,634,6464,36,3464]
vowels = ['a','e','i','o','u']
strings = ['a','a','s','k','j','d','f','o','a','i','w','e','u','f','k','l','p','e','i','f','j','s','d','k','l','f','j','d','s','k','l','f']



even_list = list(filter(lambda x:x%2==0, numbers))
print(even_list)

vowel_list = list(filter(lambda a:a in vowels, strings))
print(vowel_list)



'''

''' use of map function


# def is_onemore(num):
#     return num + 1

numbers = [1,2,3,4,55,6,6,545,2,532,252,56,62,6,7,8,6,4,3,2,4,56,7,9]

plus_one = list(map(lambda x: x + 1,numbers))
print(plus_one)

'''

''' use of reduce function in adding more than 2 numbers
'''
#we have to import reduce from functools
from functools import reduce

# def add_all(a,b):
#     return a+b
numbers = [1,2,3,4,55,6,6,545,2,532,252,56,62,6,7,8,6,4,3,2,4,56,7,9]

final = reduce(lambda a,b: a+b,numbers)
print(final)






