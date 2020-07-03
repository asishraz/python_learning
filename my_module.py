def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

def mult(a,b):
    return a*b


def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div = smart_div(div)


def smart_sub(func):
    def inner(a,b):
        if a < b:
            print("We are not printing the negative result, therefore swapping the values of both the variables")
            a,b = b,a
        return func(a,b)
    return inner
sub = smart_sub(sub)
