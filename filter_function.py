''' use of filter function, lambda and the map

'''


numbers = [1,2,4,1,3,2,4,2,5,6,4,6,7,8,8,9]

def is_even(num):
    return num % 2 == 0

even = list(filter(is_even,numbers))

print(even)

