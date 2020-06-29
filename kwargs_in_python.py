
''' 
here we learn the concept of variable length argument with keyword. In the below example, the output will be:
gareeb
(26, 'patna', 9879879870)
but we want to specify what 'patna' is, and what is '987...'
we need to give keywords in the below code


def person(name,*data):
    print(name)
    print(data)


person('gareeb', 26, 'patna', 9879879870)
********************************************************************************
But the moment we give keywords like age=26 or city='patna', we get an error:
"TypeError: person() got an unexpected keyword argument 'age'"
Because the below code will not accept the arguments with keywords, in order to solve this, we have to ** to data,
 for accepting the multiple arguments with keywords. 

def person(name, *data):
    print(name)
    print(data)


person('gareeb', age=26, city='patna', mob=9879879870)

*******************************************************************************

Therefore, if we want to pass the multiple data with the help of kewywords, we can use kwargs, i.e. '**'
Also called as keyword variable length arguments


def person(name, **data):
    print(name)
    print(data)


person('gareeb', age=26, city='patna', mob=9879879870)


************************************************************************************

TO fetch the data from the dictionary, we can iterate over the ** data in the following way:

'''

def person(name, **data):
    print(name)

    for i,j in data.items():
        print(i,j)

person('gareeb',age=26,city='Patna',mob=9879879870)
