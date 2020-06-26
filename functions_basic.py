#function learning


def add_sub(x,y):
    c = x + y
    d = x - y
    return c,d


result1,result2 = add_sub(5,5)
# print(result1)
# print(result2)

def update(x):
    x += 10
    print("x value: ", x)

a = 99
update(a)
print("a value: ",a)